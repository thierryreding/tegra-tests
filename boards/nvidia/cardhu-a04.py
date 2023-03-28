import boards
from linux.system import Kernel
from linux import sysfs

class Board(boards.Board):
    __compatible__ = 'nvidia,cardhu-a04'
    name = 'NVIDIA Cardhu A04'

    devices = [
        # platform bus
        sysfs.Device(bus = 'platform', name = '3000.pcie', driver = 'tegra-pcie'),
        sysfs.Device(bus = 'platform', name = '50000000.host1x', driver = 'tegra-host1x'),
        sysfs.Device(bus = 'platform', name = '54140000.gr2d', driver = 'tegra-gr2d'),
        sysfs.Device(bus = 'platform', name = '60005000.timer', driver = 'tegra-wdt'),
        sysfs.Device(bus = 'platform', name = '60007000.flow-controller', driver = 'tegra-flowctrl'),
        sysfs.Device(bus = 'platform', name = '6000a000.dma', driver = 'tegra-apbdma'),
        sysfs.Device(bus = 'platform', name = '6000c000.ahb', driver = 'tegra-ahb'),
        sysfs.Device(bus = 'platform', name = '6000d000.gpio', driver = 'tegra-gpio'),
        sysfs.Device(bus = 'platform', name = '70000868.pinmux', driver = 'tegra30-pinctrl'),
        sysfs.Device(bus = 'platform', name = '70006000.serial', driver = [ 'of_serial', 'tegra-uart' ]),
        sysfs.Device(bus = 'platform', name = '70006200.serial', driver = 'serial-tegra'),
        sysfs.Device(bus = 'platform', name = '7000a000.pwm', driver = 'tegra-pwm'),
        sysfs.Device(bus = 'platform', name = '7000c000.i2c', driver = 'tegra-i2c'),
        sysfs.Device(bus = 'platform', name = '7000c400.i2c', driver = 'tegra-i2c'),
        sysfs.Device(bus = 'platform', name = '7000c500.i2c', driver = 'tegra-i2c'),
        sysfs.Device(bus = 'platform', name = '7000c700.i2c', driver = 'tegra-i2c'),
        sysfs.Device(bus = 'platform', name = '7000d000.i2c', driver = 'tegra-i2c'),
        sysfs.Device(bus = 'platform', name = '7000da00.spi', driver = 'spi-tegra-slink'),
        sysfs.Device(bus = 'platform', name = '7000e000.rtc', driver = 'tegra_rtc'),
        sysfs.Device(bus = 'platform', name = '7000e400.pmc', driver = 'tegra-pmc'),
        sysfs.Device(bus = 'platform', name = '7000f000.memory-controller', driver = 'tegra-mc'),
        sysfs.Device(bus = 'platform', name = '7000f400.memory-controller', driver = 'tegra30-emc'),
        sysfs.Device(bus = 'platform', name = '7000f800.fuse', driver = 'tegra-fuse'),
        sysfs.Device(bus = 'platform', name = '70080000.ahub', driver = 'tegra30-ahub'),
        sysfs.Device(bus = 'platform', name = '70080400.i2s', driver = 'tegra30-i2s'),
        sysfs.Device(bus = 'platform', name = '7d008000.usb', driver = 'tegra-usb'),
        sysfs.Device(bus = 'platform', name = '7d008000.usb-phy', driver = 'tegra-phy'),
        sysfs.Device(bus = 'platform', name = 'gpio-keys', driver = 'gpio-keys'),
        sysfs.Device(bus = 'platform', name = 'pmu', driver = 'armv7-pmu'),
        sysfs.Device(bus = 'platform', name = 'tps65910-gpio', driver = 'tps65910-gpio'),
        sysfs.Device(bus = 'platform', name = 'tps65910-pmic', driver = 'tps65910-pmic'),
        sysfs.Device(bus = 'platform', name = 'tps65910-rtc', driver = 'tps65910-rtc'),
    # Device trees in Linux v5.9 changed sdhci@... to mmc@... and iram@... to sram@...
    ] + [
        device for device in [
            sysfs.Device(bus = 'platform', name = '40000000.iram', driver = 'sram'),
            sysfs.Device(bus = 'platform', name = '78000000.sdhci', driver = 'sdhci-tegra'),
            sysfs.Device(bus = 'platform', name = '78000400.sdhci', driver = 'sdhci-tegra'),
            sysfs.Device(bus = 'platform', name = '78000600.sdhci', driver = 'sdhci-tegra'),
        ] if Kernel().version < Kernel.Version('5.9.0')
    ] + [
        device for device in [
            sysfs.Device(bus = 'platform', name = '40000000.sram', driver = 'sram'),
            sysfs.Device(bus = 'platform', name = '78000000.mmc', driver = 'sdhci-tegra'),
            sysfs.Device(bus = 'platform', name = '78000400.mmc', driver = 'sdhci-tegra'),
            sysfs.Device(bus = 'platform', name = '78000600.mmc', driver = 'sdhci-tegra'),
        ] if Kernel().version >= Kernel.Version('5.9.0')
    # Linux v5.14 changed the sound card driver name from 'tegra-snd-wm8903' to 'tegra-wm8903'
    ] + [
        device for device in [
            sysfs.Device(bus = 'platform', name = 'sound', driver = 'tegra-snd-wm8903'),
        ] if Kernel().version < Kernel.Version('5.14.0')
    ] + [
        device for device in [
            sysfs.Device(bus = 'platform', name = 'sound', driver = 'tegra-wm8903'),
        ] if Kernel().version >= Kernel.Version('5.14.0')
    ] + [
        device for device in [
            sysfs.Device(bus = 'platform', name = '54180000.gr3d', driver = 'tegra-gr3d'),
            sysfs.Device(bus = 'platform', name = '54200000.dc', driver = 'tegra-dc'),
            sysfs.Device(bus = 'platform', name = '54240000.dc', driver = 'tegra-dc'),
        ] if Kernel().version < Kernel.Version('5.19.0')
    # HDA bus
    ] + [
    # host1x bus
    ] + [
        device for device in [
            sysfs.Device(bus = 'host1x', name = 'drm', driver = 'drm'),
        ] if Kernel().version < Kernel.Version('5.19.0')
    # I2C bus
    ] + [
        sysfs.Device(bus = 'i2c', name = '2-0044', driver = 'isl29028'),
        sysfs.Device(bus = 'i2c', name = '2-0070', driver = 'pca954x'),
        sysfs.Device(bus = 'i2c', name = '4-001a', driver = 'wm8903'),
        sysfs.Device(bus = 'i2c', name = '4-002d', driver = 'tps65910'),
        sysfs.Device(bus = 'i2c', name = '4-004c', driver = 'lm90'),
        sysfs.Device(bus = 'i2c', name = '4-0060', driver = 'tps62360'),
    # SPI bus
    ] + [
        sysfs.Device(bus = 'spi', name = 'spi0.1', driver = 'spi-nor'),
    ]

    allowlist = [
    ] + [
        warning for warning in [
            r'.* sound: ASoC: no DMI vendor name!',
        ] if Kernel().version < Kernel.Version('5.13.0')
    ] + [
        warning for warning in [
            r'memfd_create() without MFD_EXEC nor MFD_NOEXEC_SEAL, pid=[0-9]+ \'systemd\'',
        ] if Kernel().version < Kernel.Version('6.3.0')
    ]
