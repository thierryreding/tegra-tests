import boards
from linux import sysfs

class Board(boards.Board):
    __compatible__ = 'nvidia,p2371-2180'
    name = 'NVIDIA Jetson TX1 Developer Kit'

    devices = [
        # platform bus
        sysfs.Device('platform', '1003000.pcie', 'tegra-pcie'),
        sysfs.Device('platform', '50000000.host1x', 'tegra-host1x'),
        sysfs.Device('platform', '54040000.dpaux', 'tegra-dpaux'),
        sysfs.Device('platform', '54200000.dc', 'tegra-dc'),
        sysfs.Device('platform', '54240000.dc', 'tegra-dc'),
        sysfs.Device('platform', '54340000.vic', 'tegra-vic'),
        sysfs.Device('platform', '54580000.sor', 'tegra-sor'),
        sysfs.Device('platform', '7000c400.i2c', 'tegra-i2c'),
        sysfs.Device('platform', '7000c700.i2c', 'tegra-i2c'),
        sysfs.Device('platform', '7000d000.i2c', 'tegra-i2c'),
        sysfs.Device('platform', '60007000.flow-controller', 'tegra-flowctrl'),
        sysfs.Device('platform', '6000d000.gpio', 'tegra-gpio'),
        sysfs.Device('platform', '60020000.dma', 'tegra-apbdma'),
        sysfs.Device('platform', '700008d4.pinmux', 'tegra210-pinctrl'),
        sysfs.Device('platform', '70006000.serial', 'of_serial'),
        sysfs.Device('platform', '7000a000.pwm', 'tegra-pwm'),
        sysfs.Device('platform', '7000e000.rtc', 'tegra_rtc'),
        sysfs.Device('platform', '7000e400.pmc', 'tegra-pmc'),
        sysfs.Device('platform', '7000f800.fuse', 'tegra-fuse'),
        sysfs.Device('platform', '70019000.memory-controller', 'tegra-mc'),
        sysfs.Device('platform', '70090000.usb', 'tegra-xusb'),
        sysfs.Device('platform', '7009f000.padctl', 'tegra-xusb-padctl'),
        sysfs.Device('platform', '700b0000.sdhci', 'sdhci-tegra'),
        sysfs.Device('platform', '700b0600.sdhci', 'sdhci-tegra'),
        sysfs.Device('platform', '700e3000.mipi', 'tegra-mipi'),
        sysfs.Device('platform', 'gpio-keys', 'gpio-keys'),
        # I2C bus
        sysfs.Device('i2c', '0-002c', 'lp855x'),
        sysfs.Device('i2c', '0-0074', 'pca953x'),
        sysfs.Device('i2c', '1-003c', 'max77620'),
        # USB bus
        sysfs.Device('usb', '2-1:1.0', 'r8152'),
    ]
