import logging
import os
import socket
import time
from functools import wraps
from math import ceil
from threading import Event

from tftpy import SOCK_TIMEOUT, TftpClient, TftpTimeout

from tinytoolslib.constants import LK_UDP_BOOTLOADER_MSG, LK_UDP_PORT
from tinytoolslib.requests import get, post
from tinytoolslib.exceptions import TinyToolsFlashError, TinyToolsRequestError
from tinytoolslib.models import (
    LK_HW_20,
    LK_HW_20_PS,
    LK_HW_25,
    LK_HW_25_PS,
    get_version,
)


class Flasher:
    """Class with all flash related functions.

    Generally use as:
    flasher = Flasher()
    flasher.run(...)
    """

    def __init__(self, callback=None):
        """Initialize Flasher.

        callback - None/function that will be called during flashing
        with progress information. 4 parameters: current, total,
        percent, unit ('packet', 'B').
        """
        self.callback = callback
        self.context = {}
        self.canceled = Event()

    # region TFTP flashing
    @staticmethod
    def get_optimal_number_of_attempts(version_info):
        """Return number of attempts, so for HW2.X it quits earlier.

        Each attempt takes SOCK_TIMEOUT*TIMEOUT_RETRIES
        """
        logging.debug("Getting optimal number of flash attempts (less for LK2.X)")
        lk_2X_models = [
            LK_HW_20_PS.info.model,
            LK_HW_20.info.model,
            LK_HW_25.info.model,
            LK_HW_25_PS.info.model,
        ]
        if version_info is not None and version_info["model"] in lk_2X_models:
            return 1
        return 4

    def start_bootloader(self, host, username, password, schema, port):
        """Start bootloader mode on device (LK2.X, LK3.X)."""
        success = False
        # First try http method.
        try:
            # First check if upgrade is enabled else enable it
            resp = get(host, "/xml/st.xml", schema, port, username, password)["parsed"]
            if resp.get("upgr") == "0":
                logging.info("Upgrade is disabled on device - trying to enable it.")
                cmd = "/stm.cgi?auth={}{}{}".format(resp["auth"], 1, resp["userpass"])
                get(host, cmd, schema, port, username, password)["parsed"]
            logging.info("Starting bootloader mode via HTTP...")
            get(host, "/stm.cgi?upgrade=lkstart3", schema, port, username, password)
            success = True
        except (KeyError, ValueError, TinyToolsRequestError) as exc:
            logging.error("Failed to enable bootloader via HTTP: %s", str(exc))
        if not success:
            # Try UDP method.
            logging.info("Starting bootloader mode via UDP...")
            with socket.socket(
                type=socket.SOCK_DGRAM, proto=socket.IPPROTO_UDP
            ) as sock:
                sock.connect((host, LK_UDP_PORT))
                sock.sendall(LK_UDP_BOOTLOADER_MSG)
            success = True
        return success

    def flash_hook(self, packet):
        """Display flashing progress."""
        if self.canceled.is_set() and packet.opcode == 2:
            # Cancel if stop flag set and still waiting for transfer.
            raise TinyToolsFlashError("Flash canceled by user")
        if packet.opcode == 3:
            logging.debug("Packet %d/%d", packet.blocknumber, self.context["packets"])
            if callable(self.callback):
                # Call with <packet no>, <total packets>, <progress %>
                self.callback(
                    packet.blocknumber,
                    self.context["packets"],
                    packet.blocknumber / self.context["packets"] * 100,
                    "packet",
                )

    def flash_firmware_via_tftp(self, host, firmware_path, attempts_limit):
        """Try to flash firmware and display progress."""
        firmware_name = os.path.basename(firmware_path)
        bytes_size = os.stat(firmware_path).st_size
        self.context.update(
            {
                "size": bytes_size,
                "packets": ceil(bytes_size / 512),
            }
        )
        logging.info(
            "Uploading firmware %s with size of %dB in %d packets",
            firmware_name,
            self.context["size"],
            self.context["packets"],
        )
        client = TftpClient(host)
        attempt = 0
        flashed = False
        canceled = False
        while attempt < attempts_limit and not flashed:
            try:
                if self.canceled.is_set():
                    # Stop before starting flash.
                    raise TinyToolsFlashError("Flash canceled by user")
                client.upload(firmware_name, firmware_path, self.flash_hook)
            except TftpTimeout:
                attempt += 1
            except (ConnectionError, socket.gaierror):
                attempt += 1
                time.sleep(SOCK_TIMEOUT)
            except TinyToolsFlashError:
                canceled = True
                break
            else:
                flashed = True
        if canceled:
            logging.info("Canceled flashing")
            return False
        elif not flashed:
            logging.warning("Unable to connect with device. Try again.")
            return False
        else:
            logging.info(
                "Uploaded firmware in %.1fs with avg speed of %.0f kbps.",
                client.context.metrics.duration,
                client.context.metrics.kbps,
            )
            return True

    # endregion

    def update_firmware_via_http(
        self, firmware_path, host, username, password, schema, port
    ):
        """Update firmware via HTTP for LK4/tcPDU."""
        try:
            with open(firmware_path, "rb") as fread:
                bytes_size = os.stat(firmware_path).st_size
                self.context.update(
                    {
                        "size": bytes_size,
                        "uploaded": 0,
                    }
                )
                # Modify stream object to update progress
                func = getattr(fread, "read")

                @wraps(func)
                def read(data, *args, **kwargs):
                    res = func(data, *args, **kwargs)
                    self.context["uploaded"] += data
                    if self.context["uploaded"] > self.context["size"]:
                        self.context["uploaded"] = self.context["size"]
                    logging.debug(
                        "Uploaded %.0f/%.0f kB (%.1f %%)",
                        self.context["uploaded"] / 1024,
                        self.context["size"] / 1024,
                        self.context["uploaded"] / self.context["size"] * 100,
                    )
                    if callable(self.callback):
                        # Call with <uploaded B>, <total B>, <progress %>
                        self.callback(
                            self.context["uploaded"],
                            self.context["size"],
                            self.context["uploaded"] / self.context["size"] * 100,
                            "B",
                        )
                    return res

                setattr(fread, "read", read)
                # Upload file
                if callable(self.callback):
                    # Call with <0 B>, <total B>, <0 %>
                    self.callback(0, self.context["size"], 0, "B")
                resp = post(
                    host,
                    "/api/v1/upload_firmware/new_firmware",
                    fread,
                    schema,
                    port,
                    username,
                    password,
                )
                # Restart device
                get(host, "/api/v1/save/?restart=1", schema, port, username, password)
        except Exception as exc:
            logging.warning("Error occurred: %s. Try again.", str(exc))
            return False
        else:
            logging.info(
                "Uploaded firmware in %.1fs with avg speed of %.0f kbps.",
                resp.elapsed.total_seconds(),
                self.context["size"] / 1024 * 8 / resp.elapsed.total_seconds(),
            )
            return True

    def run(
        self, firmware_path, host, username, password, port=80, progress_callback=None
    ):
        """Main entry to flashing.

        Depending on input and data found from device it will select
        tftp or http method.
        """
        if progress_callback is not None:
            self.callback = progress_callback
        self.context = {}
        if (
            isinstance(firmware_path, str)
            and firmware_path
            and os.path.isfile(firmware_path)
        ):
            # Try to check what device type are we working with. For now,
            # assume that lk4/tcpdu always respond via HTTP.
            version_info = get_version(host, port, username, password)
            if version_info and version_info["network_info"].get("schema") == "https":
                schema = "https"
                port = 443
            else:
                schema = "http"
            if version_info and version_info.get("http_update"):
                return self.update_firmware_via_http(
                    firmware_path, host, username, password, schema, port
                )
            else:
                attempts = self.get_optimal_number_of_attempts(version_info)
                logging.info("Preparing device for flashing...")
                self.start_bootloader(host, username, password, schema, port)
                return self.flash_firmware_via_tftp(host, firmware_path, attempts)
        else:
            logging.warning("Invalid file for flashing.")
            return False


# region getting new firmware file
def check_for_latest_firmware(version_info):
    """Check latest available version of firmware."""
    if version_info["fw_url"] is None:
        return (
            False,
            "Cannot get firmware files for this device directly. "
            "You can look for it at https://tinycontrol.pl.",
        )
    try:
        resp = get(version_info["fw_url"], None, timeout=5)
    except TinyToolsRequestError as exc:
        return False, str(exc)
    else:
        result = resp["parsed"]
        result.update({"hardware_version": version_info["hardware_version"]})
        return True, result


def get_latest_firmware(host, username, password, firmware_directory):
    """Get latest firmware for device."""
    version_info = get_version(host, username=username, password=password)
    if version_info:
        latest_version = check_for_latest_firmware(version_info)
        if latest_version[0]:
            # Check if downloaded else download
            firmware_name = latest_version[1]["url"].split("/")[-1]
            firmware_path = os.path.join(firmware_directory, firmware_name)
            if os.path.isfile(firmware_path) or download_firmware(
                latest_version[1]["url"], firmware_path
            ):
                version_info.update(
                    {
                        "path": firmware_path,
                        "new_sw": latest_version[1]["name"],
                    }
                )
                return True, version_info
            else:
                return False, "Failed to download file"
        else:
            return False, latest_version[1]
    return False, "Cannot get information about latest firmware"


def download_firmware(download_url, save_location):
    """Download firmware from given url."""
    try:
        resp = get(download_url, None, timeout=5)
    except TinyToolsRequestError:
        return False
    else:
        os.makedirs(os.path.dirname(save_location), exist_ok=True)
        with open(save_location, "wb") as f:
            f.write(resp["_response"].content)
        return True


# endregion
