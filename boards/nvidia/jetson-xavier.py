import boards
from linux import sysfs

class Board(boards.Board):
    __compatible__ = 'nvidia,p2972-0000'
    name = 'NVIDIA Jetson Xavier Development Kit'

    devices = [
        # platform bus
        sysfs.Device('platform', '2200000.gpio', 'tegra186-gpio'),
        sysfs.Device('platform', '2490000.ethernet', 'dwc-eth-dwmac'),
        sysfs.Device('platform', '3110000.serial', 'of_serial'),
        sysfs.Device('platform', '31c0000.i2c', 'tegra-i2c'),
        sysfs.Device('platform', '3400000.sdhci', 'sdhci-tegra'),
        sysfs.Device('platform', '3460000.sdhci', 'sdhci-tegra'),
        sysfs.Device('platform', '3c00000.hsp', 'tegra-hsp'),
        sysfs.Device('platform', 'c150000.hsp', 'tegra-hsp'),
        sysfs.Device('platform', 'c340000.pwm', 'tegra-pwm'),
        sysfs.Device('platform', 'c360000.pmc', 'tegra-pmc'),
        sysfs.Device('platform', '13e00000.host1x', 'tegra-host1x'),
        sysfs.Device('platform', 'bpmp', 'tegra-bpmp'),
        sysfs.Device('platform', 'bpmp:i2c', 'tegra-bpmp-i2c'),
        sysfs.Device('platform', 'bpmp:thermal', 'tegra-bpmp-thermal'),
        sysfs.Device('platform', 'fan', 'pwm-fan'),
        sysfs.Device('platform', 'gpio-keys', 'gpio-keys'),
        # I2C bus
        sysfs.Device('i2c', '0-003c', 'max77620'),
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
