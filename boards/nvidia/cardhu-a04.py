import boards, tegra
from linux.system import Kernel
from linux import sysfs
from tegra import tegra30

class Board(boards.Board):
    __compatible__ = 'nvidia,cardhu-a04'
    name = 'NVIDIA Cardhu A04'

    def _build_devices(self, kernel):
        yield from super()._build_devices(kernel)

        # platform bus
        yield sysfs.Device(bus = 'platform', name = '3000.pcie', driver = 'tegra-pcie')
        yield sysfs.Device(bus = 'platform', name = '50000000.host1x', driver = 'tegra-host1x')
        yield sysfs.Device(bus = 'platform', name = '54140000.gr2d', driver = 'tegra-gr2d')
        yield sysfs.Device(bus = 'platform', name = '60005000.timer', driver = 'tegra-wdt')
        yield sysfs.Device(bus = 'platform', name = '60007000.flow-controller', driver = 'tegra-flowctrl')
        yield sysfs.Device(bus = 'platform', name = '6000c000.ahb', driver = 'tegra-ahb')
        yield sysfs.Device(bus = 'platform', name = '6000d000.gpio', driver = 'tegra-gpio')
        yield sysfs.Device(bus = 'platform', name = '70000868.pinmux', driver = 'tegra30-pinctrl')
        yield sysfs.Device(bus = 'platform', name = '70006000.serial', driver = [ 'of_serial', 'tegra-uart' ])
        yield sysfs.Device(bus = 'platform', name = '70006200.serial', driver = 'serial-tegra')
        yield sysfs.Device(bus = 'platform', name = '7000a000.pwm', driver = 'tegra-pwm')
        yield sysfs.Device(bus = 'platform', name = '7000c000.i2c', driver = 'tegra-i2c')
        yield sysfs.Device(bus = 'platform', name = '7000c400.i2c', driver = 'tegra-i2c')
        yield sysfs.Device(bus = 'platform', name = '7000c500.i2c', driver = 'tegra-i2c')
        yield sysfs.Device(bus = 'platform', name = '7000c700.i2c', driver = 'tegra-i2c')
        yield sysfs.Device(bus = 'platform', name = '7000d000.i2c', driver = 'tegra-i2c')
        yield sysfs.Device(bus = 'platform', name = '7000da00.spi', driver = 'spi-tegra-slink')
        yield sysfs.Device(bus = 'platform', name = '7000e000.rtc', driver = 'tegra_rtc')
        yield sysfs.Device(bus = 'platform', name = '7000e400.pmc', driver = 'tegra-pmc')
        yield sysfs.Device(bus = 'platform', name = '7000f000.memory-controller', driver = 'tegra-mc')
        yield sysfs.Device(bus = 'platform', name = '7000f400.memory-controller', driver = 'tegra30-emc')
        yield sysfs.Device(bus = 'platform', name = '7000f800.fuse', driver = 'tegra-fuse')
        yield sysfs.Device(bus = 'platform', name = '70080000.ahub', driver = 'tegra30-ahub')
        yield sysfs.Device(bus = 'platform', name = '70080400.i2s', driver = 'tegra30-i2s')
        yield sysfs.Device(bus = 'platform', name = '7d008000.usb', driver = 'tegra-usb')
        yield sysfs.Device(bus = 'platform', name = '7d008000.usb-phy', driver = 'tegra-phy')
        yield sysfs.Device(bus = 'platform', name = 'gpio-keys', driver = 'gpio-keys')
        yield sysfs.Device(bus = 'platform', name = 'pmu', driver = 'armv7-pmu')
        yield sysfs.Device(bus = 'platform', name = 'tps65910-gpio', driver = 'tps65910-gpio')
        yield sysfs.Device(bus = 'platform', name = 'tps65910-pmic', driver = 'tps65910-pmic')
        yield sysfs.Device(bus = 'platform', name = 'tps65910-rtc', driver = 'tps65910-rtc')

        if kernel.version >= '6.16.0':
            yield sysfs.Device(bus = 'platform', name = '6000a000.dma-controller', driver = 'tegra-apbdma')
        else:
            yield sysfs.Device(bus = 'platform', name = '6000a000.dma', driver = 'tegra-apbdma')

        # Device trees in Linux v5.9 changed sdhci@... to mmc@... and iram@... to sram@...
        if kernel.version < '5.9.0':
            yield sysfs.Device(bus = 'platform', name = '40000000.iram', driver = 'sram')
            yield sysfs.Device(bus = 'platform', name = '78000000.sdhci', driver = 'sdhci-tegra')
            yield sysfs.Device(bus = 'platform', name = '78000400.sdhci', driver = 'sdhci-tegra')
            yield sysfs.Device(bus = 'platform', name = '78000600.sdhci', driver = 'sdhci-tegra')
        else:
            yield sysfs.Device(bus = 'platform', name = '40000000.sram', driver = 'sram')
            yield sysfs.Device(bus = 'platform', name = '78000000.mmc', driver = 'sdhci-tegra')
            yield sysfs.Device(bus = 'platform', name = '78000400.mmc', driver = 'sdhci-tegra')
            yield sysfs.Device(bus = 'platform', name = '78000600.mmc', driver = 'sdhci-tegra')

        # Linux v5.14 changed the sound card driver name from 'tegra-snd-wm8903' to 'tegra-wm8903'
        if kernel.version < '5.14.0':
            yield sysfs.Device(bus = 'platform', name = 'sound', driver = 'tegra-snd-wm8903')
        else:
            yield sysfs.Device(bus = 'platform', name = 'sound', driver = 'tegra-wm8903')

        if kernel.version < '5.19.0':
            yield sysfs.Device(bus = 'platform', name = '54180000.gr3d', driver = 'tegra-gr3d')
            yield sysfs.Device(bus = 'platform', name = '54200000.dc', driver = 'tegra-dc')
            yield sysfs.Device(bus = 'platform', name = '54240000.dc', driver = 'tegra-dc')

        # HDA bus

        # host1x bus
        if kernel.version < '5.19.0':
            yield sysfs.Device(bus = 'host1x', name = 'drm', driver = 'drm')

        # I2C bus
        yield sysfs.Device(bus = 'i2c', name = '2-0044', driver = 'isl29028')
        yield sysfs.Device(bus = 'i2c', name = '2-0070', driver = 'pca954x')
        yield sysfs.Device(bus = 'i2c', name = '4-001a', driver = 'wm8903')
        yield sysfs.Device(bus = 'i2c', name = '4-002d', driver = 'tps65910')
        yield sysfs.Device(bus = 'i2c', name = '4-004c', driver = 'lm90')
        yield sysfs.Device(bus = 'i2c', name = '4-0060', driver = 'tps62360')

        # SPI bus
        yield sysfs.Device(bus = 'spi', name = 'spi0.1', driver = 'spi-nor')

    def _build_allowlist(self, kernel):
        yield from super()._build_allowlist(kernel)

        if kernel.version < '5.13.0':
            yield r'.* sound: ASoC: no DMI vendor name!'

        if kernel.version >= '6.3.0' and kernel.version < '6.6.0':
            yield r'memfd_create\(\) without MFD_EXEC nor MFD_NOEXEC_SEAL, pid=[0-9]+ \'systemd\''

        if kernel.version >= '6.4.0':
            yield r'systemd\[[0-9]+\]: memfd_create\(\) called without MFD_EXEC or MFD_NOEXEC_SEAL set'

    def __init__(self, kernel = Kernel()):
        super().__init__(tegra30.SoC(), kernel)
