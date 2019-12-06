import boards
from linux import sysfs

class Board(boards.Board):
    __compatible__ = 'nvidia,p2972-0000'
    name = 'NVIDIA Jetson Xavier Development Kit'

    devices = [
        # platform bus
        sysfs.Device(bus = 'platform', name = '2200000.gpio', driver = 'tegra186-gpio'),
        sysfs.Device(bus = 'platform', name = '2490000.ethernet', driver = 'dwc-eth-dwmac'),
        sysfs.Device(bus = 'platform', name = '3110000.serial', driver = 'of_serial'),
        sysfs.Device(bus = 'platform', name = '31c0000.i2c', driver = 'tegra-i2c'),
        sysfs.Device(bus = 'platform', name = '3400000.sdhci', driver = 'sdhci-tegra'),
        sysfs.Device(bus = 'platform', name = '3460000.sdhci', driver = 'sdhci-tegra'),
        sysfs.Device(bus = 'platform', name = '3c00000.hsp', driver = 'tegra-hsp'),
        sysfs.Device(bus = 'platform', name = 'c150000.hsp', driver = 'tegra-hsp'),
        sysfs.Device(bus = 'platform', name = 'c340000.pwm', driver = 'tegra-pwm'),
        sysfs.Device(bus = 'platform', name = 'c360000.pmc', driver = 'tegra-pmc'),
        sysfs.Device(bus = 'platform', name = '13e00000.host1x', driver = 'tegra-host1x'),
        sysfs.Device(bus = 'platform', name = 'bpmp', driver = 'tegra-bpmp'),
        sysfs.Device(bus = 'platform', name = 'bpmp:i2c', driver = 'tegra-bpmp-i2c'),
        sysfs.Device(bus = 'platform', name = 'bpmp:thermal', driver = 'tegra-bpmp-thermal'),
        sysfs.Device(bus = 'platform', name = 'fan', driver = 'pwm-fan'),
        sysfs.Device(bus = 'platform', name = 'gpio-keys', driver = 'gpio-keys'),
        # I2C bus
        sysfs.Device(bus = 'i2c', name = '0-003c', driver = 'max77620'),
    ]

    drivers = [
        sysfs.Driver('platform', 'tegra-host1x'),
    ]

    whitelist = [
        r'OF: fdt: Reserved memory: unsupported node format, ignoring',
        r'EINJ: ACPI disabled.',
        r'cacheinfo: Unable to detect cache hierarchy for CPU 0',
        r'dwc-eth-dwmac 2490000.ethernet: Cannot get CSR clock',
        r'mmc0: Unknown controller version \(5\). You may experience problems.',
        r'mmc1: Unknown controller version \(5\). You may experience problems.',
        r'tegra-dpaux 155e0000.dpaux: 155e0000.dpaux supply vdd not found, using dummy regulator',
        r'\[drm\] parse error at position 6 in video mode \'tegrafb\'',
        r'urandom_read: [0-9]+ callbacks suppressed',
    ]
