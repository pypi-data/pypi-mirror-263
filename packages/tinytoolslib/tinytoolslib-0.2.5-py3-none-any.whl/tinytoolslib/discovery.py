import concurrent.futures
import logging
import socket
import socketserver
import threading
import time

import netifaces

from tinytoolslib.constants import LK_UDP_DISCOVERY_MSG, LK_UDP_PORT
from tinytoolslib.models import detect_version, get_device_info


def get_ips():
    """Return list of IPs to check."""
    try:
        gateways = netifaces.gateways()
        interfaces = []
        for key, value in gateways.items():
            if key != "default":
                for item in value:
                    interfaces.append(item[1])
        addresses = set()
        for interface in interfaces:
            addresses_tmp = netifaces.ifaddresses(interface).get(2)
            if addresses_tmp:
                for addr in addresses_tmp:
                    addresses.add(addr["addr"])
    except ValueError:
        addresses = socket.gethostbyname_ex(socket.gethostname())[2]
    return addresses


def run_discovery_single(address, timelimit=3):
    """Run discovery for given address (tuple) in timelimit."""
    devices = []
    with DiscoveryServer(address, DiscoveryHandler) as server:
        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.start()
        time.sleep(timelimit)
        server.shutdown()
        devices = server.devices.copy()
        del server_thread
    return devices


def serve_forever(server):
    """Wrapper for serve_forever method of server."""
    server.serve_forever()


def run_discovery_all(timelimit=3, port=LK_UDP_PORT, version=2, addresses=None):
    """Run discovery on all available addresses.

    `version` - 1 and 2 are parallel, where time execution of 2
    is closer to timelimit; 3 is sequential run;
    """
    if addresses is None:
        addresses = [ip for ip in get_ips() if not ip.startswith("169.254")]
    devices = []
    if version == 1:
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            servers = [
                DiscoveryServer((address, port), DiscoveryHandler)
                for address in addresses
            ]
            executor.map(serve_forever, servers)
            time.sleep(timelimit)
            for server in servers:
                server.shutdown()
                devices.extend(server.devices)
    elif version == 2:
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            servers = [
                DiscoveryServerAuto(
                    (address, port), DiscoveryHandler, timelimit=timelimit
                )
                for address in addresses
            ]
            futures = {
                executor.submit(server.serve_forever): server for server in servers
            }
            for future in concurrent.futures.as_completed(futures):
                try:
                    data = future.result()
                except Exception as exc:
                    logging.warning("discovery error: %s", str(exc))
                else:
                    devices.extend(data)
    else:
        for address in addresses:
            temp = run_discovery_single((address, port))
            devices.extend(temp)
    return devices


class DiscoveryHandler(socketserver.BaseRequestHandler):
    """Handler for LK discovery server."""

    def handle(self):
        data = self.request[0].strip()
        if self.server.server_address[0] != self.client_address[0]:
            try:
                device_response = data.decode(errors="ignore").splitlines()
                device_data = {
                    "ip_address": self.client_address[0],
                    "name": device_response[0],
                    "mac_address": device_response[1].replace("-", ":"),
                    "software_version": None,
                    "hardware_version": None,
                }
                if len(device_response) == 4:
                    device_data["software_version"] = device_response[2]
                    device_data["hardware_version"] = device_response[3]
                else:
                    # LK2.0/2.5 response do not include hardware_version, so detect it.
                    device_data["software_version"] = device_response[2][:-1]
                    device_data["hardware_version"] = detect_version(
                        device_data["software_version"]
                    )
                device_data.update(
                    get_device_info(
                        device_data["hardware_version"],
                        device_data["software_version"],
                        asdict_=True,
                    )
                )
                self.server.devices.append(device_data)
            except (UnicodeDecodeError, IndexError):
                pass


class DiscoveryServer(socketserver.UDPServer):
    """Server for finding LKs in networks."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.devices = []

    def server_activate(self):
        """Send discovery message after activation."""
        super().server_activate()
        dst_ip = ".".join(self.server_address[0].split(".")[:3]) + ".255"
        dst_port = self.server_address[1]
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.socket.sendto(LK_UDP_DISCOVERY_MSG, (dst_ip, dst_port))


class DiscoveryServerAuto(DiscoveryServer):
    """DiscoveryServer that autmatically shuts down."""

    def __init__(self, *args, **kwargs):
        self.started_at = time.time()
        self.timelimit = kwargs.pop("timelimit", 3)
        super().__init__(*args, **kwargs)

    def service_actions(self):
        super().service_actions()
        now = time.time()
        if now - self.started_at >= self.timelimit:
            if not self._BaseServer__shutdown_request:
                self._BaseServer__shutdown_request = True

    def serve_forever(self, *args, **kwargs):
        """Return devices list after auto shutdown."""
        super().serve_forever(*args, **kwargs)
        return self.devices
