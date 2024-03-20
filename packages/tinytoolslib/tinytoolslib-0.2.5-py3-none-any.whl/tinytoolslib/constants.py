"""Constants related to tinycontrol devices."""

# Discovery related stuff
LK_UDP_PORT = 30403
LK_UDP_BOOTLOADER_MSG = b"\x12\xf4\x81"
LK_UDP_DISCOVERY_MSG = b"Discovery: Who is out there?"

# Device families. PS and DCDC are pretty much the same as LK (UI differs)
FAMILY_LK = "LK"
FAMILY_PS = "PS"  # Power socket
FAMILY_DCDC = "DCDC"  # Converter DC/DC
FAMILY_TCPDU = "tcPDU"

FW_URL_TEMPLATE = "https://tinycontrol.pl/firmware/{}/latest/"
