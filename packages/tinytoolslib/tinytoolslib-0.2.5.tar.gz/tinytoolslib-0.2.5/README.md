# tinyToolsLib

Set of tools for use with tinycontrol devices like LK2.X, LK3.X, LK4.X or tcPDU.

## Features

Easy to use functions for common actions with tinycontrol devices:

- Flashing firmware via TFTP (LK2.X, LK3.X).
- Flashing firmware via HTTP (LK4, tcPDU).
- Getting data from devices.
- Sending commands to devices (for common tasks like controlling OUTs, PWMs, etc.).
- Checking device version.

## Usage

Discovering devices in network:

```py
from tinytoolslib.discovery import run_discovery_all

devices = run_discovery_all()
for device in devices:
    print('{ip_address:20}{name:20}{mac_address:20}{family:10}{hardware_version:10}{software_version:15}'.format_map(device))
```

Flashing firmware:

```py
from tinytoolslib.flash import get_latest_firmware, Flasher

success, data = get_latest_firmware(IP_ADDRESS, USERNAME, PASSWORD, DIRECTORY_FOR_FIRMWARE_FILES)
if success:
    flasher = Flasher()
    success = flasher.run(data['path'], IP_ADDRESS, USERNAME, PASSWORD)
```

Working with tinycontrol devices:

```py
from tinytoolslib.models import get_version

version_info = get_version(IP_ADDRESS, with_device=True)
if version_info:
    device_model = version_info['device_model']
    # Get reading from device
    device_model.get_all()
    # Control outputs OUT
    device_model.set_out(1, 1)
```

## File structure

- constants.py - constants related to tinycontrol devices.
- discovery.py - functions for discovering devices in network via UDP broadcast. Works for LK2.X, LK3.5 SW 1.26+, LK4.0, tcPDU.
- exceptions.py - errors raised in this library.
- flash.py - functions for updating the firmware of devices. Includes both method: TFTP and HTTP.
- models.py - models for working with different device types.
- parsers.py - functions for working with data formats used on LKs.
- requests.py - base request functions.
