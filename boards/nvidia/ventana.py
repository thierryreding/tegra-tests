import boards
from linux.system import Kernel
from linux import sysfs

class Board(boards.Board):
    __compatible__ = 'nvidia,ventana'
    name = 'NVIDIA Ventana'

    devices = [
        # platform bus
        sysfs.Device(bus = 'platform', name = '50000000.host1x', driver ='tegra-host1x'),
        sysfs.Device(bus = 'platform', name = '54140000.gr2d', driver ='tegra-gr2d'),
        sysfs.Device(bus = 'platform', name = '54180000.gr3d', driver ='tegra-gr3d'),
        sysfs.Device(bus = 'platform', name = '54200000.dc', driver ='tegra-dc'),
        sysfs.Device(bus = 'platform', name = '54240000.dc', driver ='tegra-dc'),
        sysfs.Device(bus = 'platform', name = '54280000.hdmi', driver ='tegra-hdmi'),
        sysfs.Device(bus = 'platform', name = '60007000.flow-controller', driver ='tegra-flowctrl'),
        sysfs.Device(bus = 'platform', name = '6000a000.dma', driver ='tegra-apbdma'),
        sysfs.Device(bus = 'platform', name = '6000c000.ahb', driver ='tegra-ahb'),
        sysfs.Device(bus = 'platform', name = '6000d000.gpio', driver ='tegra-gpio'),
        sysfs.Device(bus = 'platform', name = '70000014.pinmux', driver ='tegra20-pinctrl'),
        sysfs.Device(bus = 'platform', name = '70000c00.das', driver ='tegra20-das'),
        sysfs.Device(bus = 'platform', name = '70002800.i2s', driver ='tegra20-i2s'),
        sysfs.Device(bus = 'platform', name = '70006300.serial', driver = [ 'of_serial', 'tegra-uart' ]),
        sysfs.Device(bus = 'platform', name = '7000a000.pwm', driver ='tegra-pwm'),
        sysfs.Device(bus = 'platform', name = '7000c000.i2c', driver ='tegra-i2c'),
        sysfs.Device(bus = 'platform', name = '7000c400.i2c', driver ='tegra-i2c'),
        sysfs.Device(bus = 'platform', name = '7000c500.i2c', driver ='tegra-i2c'),
        sysfs.Device(bus = 'platform', name = '7000d000.i2c', driver ='tegra-i2c'),
        sysfs.Device(bus = 'platform', name = '7000e000.rtc', driver ='tegra_rtc'),
        sysfs.Device(bus = 'platform', name = '7000e400.pmc', driver ='tegra-pmc'),
        sysfs.Device(bus = 'platform', name = '7000f000.memory-controller', driver ='tegra-mc'),
        sysfs.Device(bus = 'platform', name = '7000f400.memory-controller', driver ='tegra20-emc'),
        sysfs.Device(bus = 'platform', name = '7000f800.fuse', driver ='tegra-fuse'),
        sysfs.Device(bus = 'platform', name = 'c5000000.usb', driver ='tegra-usb'),
        sysfs.Device(bus = 'platform', name = 'c5000000.usb-phy', driver ='tegra-phy'),
        sysfs.Device(bus = 'platform', name = 'c5004000.usb', driver ='tegra-usb'),
        sysfs.Device(bus = 'platform', name = 'c5004000.usb-phy', driver ='tegra-phy'),
        sysfs.Device(bus = 'platform', name = 'c5008000.usb', driver ='tegra-usb'),
        sysfs.Device(bus = 'platform', name = 'c5008000.usb-phy', driver ='tegra-phy'),
        sysfs.Device(bus = 'platform', name = 'gpio-keys', driver ='gpio-keys'),
        sysfs.Device(bus = 'platform', name = 'pmu', driver ='armv7-pmu'),
        sysfs.Device(bus = 'platform', name = 'tegra20-cpufreq', driver ='tegra20-cpufreq'),
        sysfs.Device(bus = 'platform', name = 'tps6586x-gpio', driver ='tps6586x-gpio'),
        sysfs.Device(bus = 'platform', name = 'tps6586x-regulator', driver ='tps6586x-regulator'),
        sysfs.Device(bus = 'platform', name = 'tps6586x-rtc', driver ='tps6586x-rtc'),
    # Device trees in Linux v5.9 changed sdhci@... to mmc@... and iram@... to sram@...
    ] + [
        device for device in [
            sysfs.Device(bus = 'platform', name = '40000000.iram', driver ='sram'),
            sysfs.Device(bus = 'platform', name = 'c8000000.sdhci', driver ='sdhci-tegra'),
            sysfs.Device(bus = 'platform', name = 'c8000400.sdhci', driver ='sdhci-tegra'),
            sysfs.Device(bus = 'platform', name = 'c8000600.sdhci', driver ='sdhci-tegra'),
        ] if Kernel().version < Kernel.Version('5.9.0')
    ] + [
        device for device in [
            sysfs.Device(bus = 'platform', name = '40000000.sram', driver ='sram'),
            sysfs.Device(bus = 'platform', name = 'c8000000.mmc', driver ='sdhci-tegra'),
            sysfs.Device(bus = 'platform', name = 'c8000400.mmc', driver ='sdhci-tegra'),
            sysfs.Device(bus = 'platform', name = 'c8000600.mmc', driver ='sdhci-tegra'),
        ] if Kernel().version >= Kernel.Version('5.9.0')
    # Linux v5.14 changed the sound card driver name from 'tegra-snd-wm8903' to 'tegra-wm8903'
    ] + [
        device for device in [
            sysfs.Device(bus = 'platform', name = 'sound', driver ='tegra-snd-wm8903'),
        ] if Kernel().version < Kernel.Version('5.14.0')
    ] + [
        device for device in [
            sysfs.Device(bus = 'platform', name = 'sound', driver ='tegra-wm8903'),
        ] if Kernel().version >= Kernel.Version('5.14.0')
    # host1x bus
    ] + [
        sysfs.Device(bus = 'host1x', name = 'drm', driver ='drm'),
    # I2C bus
    ] + [
        sysfs.Device(bus = 'i2c', name = '0-001a', driver ='wm8903'),
        sysfs.Device(bus = 'i2c', name = '0-0044', driver ='isl29018'),
        sysfs.Device(bus = 'i2c', name = '3-0034', driver ='tps6586x'),
        sysfs.Device(bus = 'i2c', name = '3-004c', driver ='lm90'),
    ]

    allowlist = [
    ] + [
        warning for warning in [
            r'.* sound: ASoC: no DMI vendor name!',
        ] if Kernel().version < Kernel.Version('5.13.0')
    ]
