import boards
from linux.system import Kernel
from linux import sysfs

class Board(boards.Board):
    __compatible__ = 'nvidia,p2371-2180'
    name = 'NVIDIA Jetson TX1 Developer Kit'

    devices = [
        # platform bus
        sysfs.Device(bus = 'platform', name = '1003000.pcie', driver = 'tegra-pcie'),
        sysfs.Device(bus = 'platform', name = '50000000.host1x', driver = 'tegra-host1x'),
        sysfs.Device(bus = 'platform', name = '54040000.dpaux', driver = 'tegra-dpaux'),
        sysfs.Device(bus = 'platform', name = '54200000.dc', driver = 'tegra-dc'),
        sysfs.Device(bus = 'platform', name = '54240000.dc', driver = 'tegra-dc'),
        sysfs.Device(bus = 'platform', name = '54340000.vic', driver = 'tegra-vic'),
        sysfs.Device(bus = 'platform', name = '54580000.sor', driver = 'tegra-sor'),
        sysfs.Device(bus = 'platform', name = '60007000.flow-controller', driver = 'tegra-flowctrl'),
        sysfs.Device(bus = 'platform', name = '6000d000.gpio', driver = 'tegra-gpio'),
        sysfs.Device(bus = 'platform', name = '60020000.dma', driver = 'tegra-apbdma'),
        sysfs.Device(bus = 'platform', name = '700008d4.pinmux', driver = 'tegra210-pinctrl'),
        sysfs.Device(bus = 'platform', name = '70006000.serial', driver = [ 'of_serial', 'tegra-uart' ]),
        sysfs.Device(bus = 'platform', name = '7000c400.i2c', driver = 'tegra-i2c'),
        sysfs.Device(bus = 'platform', name = '7000c700.i2c', driver = 'tegra-i2c'),
        sysfs.Device(bus = 'platform', name = '7000d000.i2c', driver = 'tegra-i2c'),
        sysfs.Device(bus = 'platform', name = '7000a000.pwm', driver = 'tegra-pwm'),
        sysfs.Device(bus = 'platform', name = '7000e000.rtc', driver = 'tegra_rtc'),
        sysfs.Device(bus = 'platform', name = '7000e400.pmc', driver = 'tegra-pmc'),
        sysfs.Device(bus = 'platform', name = '7000f800.fuse', driver = 'tegra-fuse'),
        sysfs.Device(bus = 'platform', name = '70019000.memory-controller', driver = 'tegra-mc'),
        sysfs.Device(bus = 'platform', name = '70090000.usb', driver = 'tegra-xusb'),
        sysfs.Device(bus = 'platform', name = '7009f000.padctl', driver = 'tegra-xusb-padctl'),
        sysfs.Device(bus = 'platform', name = '700e3000.mipi', driver = 'tegra-mipi'),
        sysfs.Device(bus = 'platform', name = 'gpio-keys', driver = 'gpio-keys'),
    # Device trees in Linux v5.9 changed sdhci@... to mmc@...
    ] + [
        device for device in [
            sysfs.Device(bus = 'platform', name = '700b0000.sdhci', driver = 'sdhci-tegra'),
            sysfs.Device(bus = 'platform', name = '700b0600.sdhci', driver = 'sdhci-tegra'),
        ] if Kernel().version < Kernel.Version('5.9.0')
    ] + [
        device for device in [
            sysfs.Device(bus = 'platform', name = '700b0000.mmc', driver = 'sdhci-tegra'),
            sysfs.Device(bus = 'platform', name = '700b0600.mmc', driver = 'sdhci-tegra'),
        ] if Kernel().version >= Kernel.Version('5.9.0')
    # I2C bus
    ] + [
        sysfs.Device(bus = 'i2c', name = '0-002c', driver = 'lp855x'),
        sysfs.Device(bus = 'i2c', name = '0-0074', driver = 'pca953x'),
        sysfs.Device(bus = 'i2c', name = '1-003c', driver = 'max77620'),
    # USB bus
    ] + [
        sysfs.Device(bus = 'usb', name = '2-1:1.0', driver = 'r8152'),
    # host1x bus
    # Linux v5.8 enabled support for the Tegra VI/CSI V4L2 driver on Jetson TX1
    ] + [
        device for device in [
            sysfs.Device(bus = 'host1x', name = 'tegra-video', driver = 'tegra-video'),
        ] if Kernel().version >= Kernel.Version('5.8.0')
    ]

    drivers = [
        sysfs.Driver('platform', 'tegra-host1x'),
    ]

    whitelist = [
        r'urandom_read: [0-9]+ callbacks suppressed',
    ]
