import boards
from linux.system import Kernel
from linux import sysfs, system
from tegra import tegra210

class Board(boards.Board):
    __compatible__ = 'nvidia,p2371-2180'
    name = 'NVIDIA Jetson TX1 Developer Kit'

    def _build_devices(self, kernel):
        yield from super()._build_devices(kernel)

        # platform bus
        yield sysfs.Device(bus = 'platform', name = '1003000.pcie', driver = 'tegra-pcie')
        yield sysfs.Device(bus = 'platform', name = '50000000.host1x', driver = 'tegra-host1x')
        yield sysfs.Device(bus = 'platform', name = '54040000.dpaux', driver = 'tegra-dpaux')
        yield sysfs.Device(bus = 'platform', name = '54200000.dc', driver = 'tegra-dc')
        yield sysfs.Device(bus = 'platform', name = '54240000.dc', driver = 'tegra-dc')
        yield sysfs.Device(bus = 'platform', name = '54300000.dsi', driver = 'tegra-dsi')
        yield sysfs.Device(bus = 'platform', name = '54340000.vic', driver = 'tegra-vic')
        yield sysfs.Device(bus = 'platform', name = '54580000.sor', driver = 'tegra-sor')
        yield sysfs.Device(bus = 'platform', name = '60005000.timer', driver = '')
        yield sysfs.Device(bus = 'platform', name = '60007000.flow-controller', driver = 'tegra-flowctrl')
        yield sysfs.Device(bus = 'platform', name = '6000d000.gpio', driver = 'tegra-gpio')
        yield sysfs.Device(bus = 'platform', name = '700008d4.pinmux', driver = 'tegra210-pinctrl')
        yield sysfs.Device(bus = 'platform', name = '70006000.serial', driver = [ 'of_serial', 'tegra-uart' ])
        yield sysfs.Device(bus = 'platform', name = '7000a000.pwm', driver = 'tegra-pwm')
        yield sysfs.Device(bus = 'platform', name = '7000c400.i2c', driver = 'tegra-i2c')
        yield sysfs.Device(bus = 'platform', name = '7000c500.i2c', driver = 'tegra-i2c')
        yield sysfs.Device(bus = 'platform', name = '7000c700.i2c', driver = 'tegra-i2c')
        yield sysfs.Device(bus = 'platform', name = '7000d000.i2c', driver = 'tegra-i2c')
        yield sysfs.Device(bus = 'platform', name = '7000e000.rtc', driver = 'tegra_rtc')
        yield sysfs.Device(bus = 'platform', name = '7000e400.pmc', driver = 'tegra-pmc')
        yield sysfs.Device(bus = 'platform', name = '7000f800.fuse', driver = 'tegra-fuse')
        yield sysfs.Device(bus = 'platform', name = '70019000.memory-controller', driver = 'tegra-mc')
        yield sysfs.Device(bus = 'platform', name = '70030000.hda', driver = 'tegra-hda')
        yield sysfs.Device(bus = 'platform', name = '70090000.usb', driver = 'tegra-xusb')
        yield sysfs.Device(bus = 'platform', name = '7009f000.padctl', driver = 'tegra-xusb-padctl')
        yield sysfs.Device(bus = 'platform', name = '700e2000.thermal-sensor', driver = 'tegra_soctherm')
        yield sysfs.Device(bus = 'platform', name = '700e3000.mipi', driver = 'tegra-mipi')
        yield sysfs.Device(bus = 'platform', name = '70110000.clock', driver = 'tegra124-dfll')
        yield sysfs.Device(bus = 'platform', name = 'cpufreq-dt.0', driver = 'cpufreq-dt')
        yield sysfs.Device(bus = 'platform', name = 'cpufreq-tegra124', driver = 'cpufreq-tegra124')
        yield sysfs.Device(bus = 'platform', name = 'gpio-keys', driver = 'gpio-keys')
        yield sysfs.Device(bus = 'platform', name = 'max77620-gpio', driver = 'max77620-gpio')
        yield sysfs.Device(bus = 'platform', name = 'max77620-pinctrl', driver = 'max77620-pinctrl')
        yield sysfs.Device(bus = 'platform', name = 'max77620-pmic', driver = 'max77620-pmic')
        yield sysfs.Device(bus = 'platform', name = 'max77620-rtc', driver = 'max77686-rtc')
        yield sysfs.Device(bus = 'platform', name = 'pmu', driver = 'armv8-pmu')

        if kernel.version >= '6.19.0':
            yield sysfs.Device(bus = 'platform', name = '60020000.dma-controller' driver = 'tegra-apbdma')
        else:
            yield sysfs.Device(bus = 'platform', name = '60020000.dma', driver = 'tegra-apbdma')

        # Device trees in Linux v5.9 changed sdhci@... to mmc@...
        if kernel.version < '5.9.0':
            yield sysfs.Device(bus = 'platform', name = '700b0000.sdhci', driver = 'sdhci-tegra')
            yield sysfs.Device(bus = 'platform', name = '700b0600.sdhci', driver = 'sdhci-tegra')
        else:
            yield sysfs.Device(bus = 'platform', name = '700b0000.mmc', driver = 'sdhci-tegra')
            yield sysfs.Device(bus = 'platform', name = '700b0600.mmc', driver = 'sdhci-tegra')

        # Linux v5.10 enabled support for ACONNECT, ADMA and AGIC
        if kernel.version >= '5.10.0':
            yield sysfs.Device(bus = 'platform', name = 'aconnect@702c0000', driver = 'tegra-aconnect')
            yield sysfs.Device(bus = 'platform', name = '702e2000.dma-controller', driver = 'tegra-adma')
            yield sysfs.Device(bus = 'platform', name = '702f9000.interrupt-controller', driver = 'gic')

        # Linux v5.12 enabled support for the Audio Processing Engine
        if kernel.version >= '5.12.0':
            yield sysfs.Device(bus = 'platform', name = '702d0800.ahub', driver = 'tegra210-ahub')
            yield sysfs.Device(bus = 'platform', name = '702d0000.admaif', driver = 'tegra210-admaif')
            yield sysfs.Device(bus = 'platform', name = '702d1000.i2s', driver = 'tegra210-i2s')
            yield sysfs.Device(bus = 'platform', name = '702d1100.i2s', driver = 'tegra210-i2s')
            yield sysfs.Device(bus = 'platform', name = '702d1200.i2s', driver = 'tegra210-i2s')
            yield sysfs.Device(bus = 'platform', name = '702d1300.i2s', driver = 'tegra210-i2s')
            yield sysfs.Device(bus = 'platform', name = '702d1400.i2s', driver = 'tegra210-i2s')
            yield sysfs.Device(bus = 'platform', name = '702d4000.dmic', driver = 'tegra210-dmic')
            yield sysfs.Device(bus = 'platform', name = '702d4000.dmic', driver = 'tegra210-dmic')
            yield sysfs.Device(bus = 'platform', name = '702d4100.dmic', driver = 'tegra210-dmic')
            yield sysfs.Device(bus = 'platform', name = '702d4200.dmic', driver = 'tegra210-dmic')
            yield sysfs.Device(bus = 'platform', name = 'sound', driver = 'tegra-audio-graph-card')

        # Linux v6.15 enabled support for 7000c000.i2c
        if kernel.version >= '6.15.0':
            yield sysfs.Device(bus = 'platform', name = '7000c000.i2c', driver = 'tegra-i2c')

        # HDA bus
        yield sysfs.Device(bus = 'hdaudio', name = 'hdaudioC0D3', driver = [ 'snd_hda_codec_hdmi', 'snd_hda_codec_tegrahdmi' ])

        # USB bus
        yield sysfs.Device(bus = 'usb', name = '2-1:1.0', driver = 'r8152')

        # host1x bus
        yield sysfs.Device(bus = 'host1x', name = 'drm', driver = 'drm')

        # Linux v5.8 enabled support for the Tegra VI/CSI V4L2 driver on Jetson TX1
        if kernel.version >= '5.8.0':
            yield sysfs.Device(bus = 'host1x', name = 'tegra-video', driver = 'tegra-video')

        # I2C bus
        i2c1 = self.soc.devices['i2c1']
        i2c2 = self.soc.devices['i2c2']
        i2c3 = self.soc.devices['i2c3']
        i2c5 = self.soc.devices['i2c5']

        yield i2c1
        yield i2c2
        yield i2c2.client(0x74, driver = 'pca953x')
        yield i2c2.client(0x77, driver = 'pca953x')
        yield i2c3
        yield i2c3.client(0x50, driver = 'at24')
        yield i2c3.client(0x57, driver = 'at24')
        yield i2c5
        yield i2c5.client(0x3c, driver = 'max77620')

        if kernel.version >= '6.15.0':
            yield i2c1.client(0x4c, driver = 'lm90')

    def _build_drivers(self, kernel):
        yield from super()._build_drivers(kernel)

        yield sysfs.Driver('platform', 'tegra-host1x')

    def _build_allowlist(self, kernel):
        yield from super()._build_allowlist(kernel)

        yield r'EINJ: ACPI disabled.'
        yield r'lp855x 0-002c: failed to read 0x00'
        yield r'lp855x 0-002c: pre init device err: -121'
        yield r'lp855x 0-002c: device config err: -121'
        yield r'lp855x: probe of 0-002c failed with error -121'
        yield r'tegra-i2c 7000c700.i2c: deferred probe timeout, ignoring dependency'
        yield r'urandom_read: [0-9]+ callbacks suppressed'

        if kernel.version < '5.13.0':
            yield r'.* sound: ASoC: no DMI vendor name!'

        if kernel.version >= '6.3.0' and kernel.version < '6.6.0':
            yield r'memfd_create\(\) without MFD_EXEC nor MFD_NOEXEC_SEAL, pid=[0-9]+ \'systemd\''

        if kernel.version >= '6.4.0':
            yield r'systemd\[[0-9]+\]: memfd_create\(\) called without MFD_EXEC or MFD_NOEXEC_SEAL set'

        if kernel.version >= '6.19.0' and kernel.version < '7.0.0':
            yield r'tegra210-ahub 702d0800.ahub: using zero-initialized flat cache, this may cause unexpected behavior'

    def __init__(self, kernel = Kernel()):
        super().__init__(tegra210.SoC(), kernel)

        self.eeproms = {}

        i2c3 = self.soc.devices['i2c3']

        # I2C bus
        self.eeproms['module'] = i2c3.client(0x50, driver = 'at24')
        self.eeproms['system'] = i2c3.client(0x57, driver = 'at24')

