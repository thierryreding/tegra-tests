import boards, tegra
from linux.system import Kernel
from linux import sysfs
from tegra import tegra20

class Board(boards.Board):
    __compatible__ = 'nvidia,ventana'
    name = 'NVIDIA Ventana'

    def _build_devices(self, kernel):
        yield from super()._build_devices(kernel)

        # platform bus
        yield sysfs.Device(bus = 'platform', name = '50000000.host1x', driver = 'tegra-host1x')
        yield sysfs.Device(bus = 'platform', name = '54140000.gr2d', driver = 'tegra-gr2d')
        yield sysfs.Device(bus = 'platform', name = '54180000.gr3d', driver = 'tegra-gr3d')
        yield sysfs.Device(bus = 'platform', name = '54200000.dc', driver = 'tegra-dc')
        yield sysfs.Device(bus = 'platform', name = '54240000.dc', driver = 'tegra-dc')
        yield sysfs.Device(bus = 'platform', name = '54280000.hdmi', driver = 'tegra-hdmi')
        yield sysfs.Device(bus = 'platform', name = '60007000.flow-controller', driver = 'tegra-flowctrl')
        yield sysfs.Device(bus = 'platform', name = '6000c000.ahb', driver = 'tegra-ahb')
        yield sysfs.Device(bus = 'platform', name = '6000d000.gpio', driver = 'tegra-gpio')
        yield sysfs.Device(bus = 'platform', name = '70000014.pinmux', driver = 'tegra20-pinctrl')
        yield sysfs.Device(bus = 'platform', name = '70000c00.das', driver = 'tegra20-das')
        yield sysfs.Device(bus = 'platform', name = '70002800.i2s', driver = 'tegra20-i2s')
        yield sysfs.Device(bus = 'platform', name = '70006300.serial', driver = [ 'of_serial', 'tegra-uart' ])
        yield sysfs.Device(bus = 'platform', name = '7000a000.pwm', driver = 'tegra-pwm')
        yield sysfs.Device(bus = 'platform', name = '7000c000.i2c', driver = 'tegra-i2c')
        yield sysfs.Device(bus = 'platform', name = '7000c400.i2c', driver = 'tegra-i2c')
        yield sysfs.Device(bus = 'platform', name = '7000c500.i2c', driver = 'tegra-i2c')
        yield sysfs.Device(bus = 'platform', name = '7000d000.i2c', driver = 'tegra-i2c')
        yield sysfs.Device(bus = 'platform', name = '7000e000.rtc', driver = 'tegra_rtc')
        yield sysfs.Device(bus = 'platform', name = '7000e400.pmc', driver = 'tegra-pmc')
        yield sysfs.Device(bus = 'platform', name = '7000f000.memory-controller', driver = 'tegra-mc')
        yield sysfs.Device(bus = 'platform', name = '7000f400.memory-controller', driver = 'tegra20-emc')
        yield sysfs.Device(bus = 'platform', name = '7000f800.fuse', driver = 'tegra-fuse')
        yield sysfs.Device(bus = 'platform', name = 'c5000000.usb', driver = 'tegra-usb')
        yield sysfs.Device(bus = 'platform', name = 'c5000000.usb-phy', driver = 'tegra-phy')
        yield sysfs.Device(bus = 'platform', name = 'c5004000.usb', driver = 'tegra-usb')
        yield sysfs.Device(bus = 'platform', name = 'c5004000.usb-phy', driver = 'tegra-phy')
        yield sysfs.Device(bus = 'platform', name = 'c5008000.usb', driver = 'tegra-usb')
        yield sysfs.Device(bus = 'platform', name = 'c5008000.usb-phy', driver = 'tegra-phy')
        yield sysfs.Device(bus = 'platform', name = 'gpio-keys', driver = 'gpio-keys')
        yield sysfs.Device(bus = 'platform', name = 'pmu', driver = 'armv7-pmu')
        yield sysfs.Device(bus = 'platform', name = 'tegra20-cpufreq', driver = 'tegra20-cpufreq')
        yield sysfs.Device(bus = 'platform', name = 'tps6586x-gpio', driver = 'tps6586x-gpio')
        yield sysfs.Device(bus = 'platform', name = 'tps6586x-regulator', driver = 'tps6586x-regulator')
        yield sysfs.Device(bus = 'platform', name = 'tps6586x-rtc', driver = 'tps6586x-rtc')

        if kernel.version > '6.16.0':
            yield sysfs.Device(bus = 'platform', name = '6000a000.dma-controller', driver = 'tegra-apbdma')
        else:
            yield sysfs.Device(bus = 'platform', name = '6000a000.dma', driver = 'tegra-apbdma')

        # Device trees in Linux v5.9 changed sdhci@... to mmc@... and iram@... to sram@...
        if kernel.version < '5.9.0':
            yield sysfs.Device(bus = 'platform', name = '40000000.iram', driver = 'sram')
            yield sysfs.Device(bus = 'platform', name = 'c8000000.sdhci', driver = 'sdhci-tegra')
            yield sysfs.Device(bus = 'platform', name = 'c8000400.sdhci', driver = 'sdhci-tegra')
            yield sysfs.Device(bus = 'platform', name = 'c8000600.sdhci', driver = 'sdhci-tegra')
        else:
            yield sysfs.Device(bus = 'platform', name = '40000000.sram', driver = 'sram')
            yield sysfs.Device(bus = 'platform', name = 'c8000000.mmc', driver = 'sdhci-tegra')
            yield sysfs.Device(bus = 'platform', name = 'c8000400.mmc', driver = 'sdhci-tegra')
            yield sysfs.Device(bus = 'platform', name = 'c8000600.mmc', driver = 'sdhci-tegra')

        # Linux v5.14 changed the sound card driver name from 'tegra-snd-wm8903' to 'tegra-wm8903'
        if kernel.version < '5.14.0':
            yield sysfs.Device(bus = 'platform', name = 'sound', driver = 'tegra-snd-wm8903')

        if kernel.version >= '5.14.0':
            yield sysfs.Device(bus = 'platform', name = 'sound', driver = 'tegra-wm8903')

        # host1x bus
        yield sysfs.Device(bus = 'host1x', name = 'drm', driver = 'drm')

        # I2C bus
        yield sysfs.Device(bus = 'i2c', name = '0-001a', driver = 'wm8903')
        yield sysfs.Device(bus = 'i2c', name = '0-0044', driver = 'isl29018')
        yield sysfs.Device(bus = 'i2c', name = '3-0034', driver = 'tps6586x')
        yield sysfs.Device(bus = 'i2c', name = '3-004c', driver = 'lm90')

    def _build_allowlist(self, kernel):
        yield from super()._build_allowlist(kernel)

        if kernel.version < '5.13.0':
            yield r'.* sound: ASoC: no DMI vendor name!'

        if kernel.version >= '6.3.0' and kernel.version < '6.6.0':
            yield r'memfd_create\(\) without MFD_EXEC nor MFD_NOEXEC_SEAL, pid=[0-9]+ \'systemd\''

        if kernel.version >= '6.4.0':
            yield r'systemd\[[0-9]+\]: memfd_create\(\) called without MFD_EXEC or MFD_NOEXEC_SEAL set'

    def __init__(self, kernel = Kernel()):
        super().__init__(tegra20.SoC(), kernel)
