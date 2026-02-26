import boards
from linux.system import Kernel
from linux import sysfs
from tegra import tegra210

class Board(boards.Board):
    __compatible__ = 'nvidia,p3450-0000'
    name = 'NVIDIA Jetson Nano Developer Kit'

    def _build_devices(self, kernel):
        yield from super()._build_devices(kernel)

        # platform bus
        yield sysfs.Device(bus = 'platform', name = '1003000.pcie', driver = 'tegra-pcie')
        yield sysfs.Device(bus = 'platform', name = '50000000.host1x', driver = 'tegra-host1x')
        yield sysfs.Device(bus = 'platform', name = '54040000.dpaux', driver = 'tegra-dpaux')
        yield sysfs.Device(bus = 'platform', name = '54200000.dc', driver = 'tegra-dc')
        yield sysfs.Device(bus = 'platform', name = '54240000.dc', driver = 'tegra-dc')
        yield sysfs.Device(bus = 'platform', name = '54340000.vic', driver = 'tegra-vic')
        yield sysfs.Device(bus = 'platform', name = '54540000.sor', driver = 'tegra-sor')
        yield sysfs.Device(bus = 'platform', name = '54580000.sor', driver = 'tegra-sor')
        yield sysfs.Device(bus = 'platform', name = '545c0000.dpaux', driver = 'tegra-dpaux')
        yield sysfs.Device(bus = 'platform', name = '57000000.gpu', driver = 'nouveau')
        yield sysfs.Device(bus = 'platform', name = '60005000.timer', driver = '')
        yield sysfs.Device(bus = 'platform', name = '60007000.flow-controller', driver = 'tegra-flowctrl')
        yield sysfs.Device(bus = 'platform', name = '6000d000.gpio', driver = 'tegra-gpio')
        yield sysfs.Device(bus = 'platform', name = '700008d4.pinmux', driver = 'tegra210-pinctrl')
        yield sysfs.Device(bus = 'platform', name = '70006000.serial', driver = [ 'of_serial', 'tegra-uart' ])
        yield sysfs.Device(bus = 'platform', name = '7000a000.pwm', driver = 'tegra-pwm')
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

        if kernel.version >= '5.19.0':
            yield sysfs.Device(bus = 'platform', name = 'pwm-fan', driver = 'pwm-fan')
        else:
            yield sysfs.Device(bus = 'platform', name = 'fan', driver = 'pwm-fan')

        # Device trees in Linux v5.9 changed sdhci@... to mmc@...
        if kernel.version > '5.9.0':
            yield sysfs.Device(bus = 'platform', name = '700b0000.sdhci', driver = 'sdhci-tegra')
            yield sysfs.Device(bus = 'platform', name = '700b0400.sdhci', driver = 'sdhci-tegra')
        else:
            yield sysfs.Device(bus = 'platform', name = '700b0000.mmc', driver = 'sdhci-tegra')
            yield sysfs.Device(bus = 'platform', name = '700b0400.mmc', driver = 'sdhci-tegra')

        # Linux v5.10 enabled support for ACONNECT, ADMA and AGIC
        if kernel.version >= '5.10.0':
            yield sysfs.Device(bus = 'platform', name = 'aconnect@702c0000', driver = 'tegra-aconnect')
            yield sysfs.Device(bus = 'platform', name = '702e2000.dma-controller', driver = 'tegra-adma')
            yield sysfs.Device(bus = 'platform', name = '702f9000.interrupt-controller', driver = 'gic')

        # Linux v5.12 enabled support for the Audio Processing Engine
        if kernel.version >= '5.12.0':
            sysfs.Device(bus = 'platform', name = '702d0800.ahub', driver = 'tegra210-ahub')
            sysfs.Device(bus = 'platform', name = '702d0000.admaif', driver = 'tegra210-admaif')
            sysfs.Device(bus = 'platform', name = '702d1200.i2s', driver = 'tegra210-i2s')
            sysfs.Device(bus = 'platform', name = '702d1300.i2s', driver = 'tegra210-i2s')
            sysfs.Device(bus = 'platform', name = '702d4000.dmic', driver = 'tegra210-dmic')
            sysfs.Device(bus = 'platform', name = '702d4000.dmic', driver = 'tegra210-dmic')
            sysfs.Device(bus = 'platform', name = '702d4100.dmic', driver = 'tegra210-dmic')
            sysfs.Device(bus = 'platform', name = 'sound', driver = 'tegra-audio-graph-card')

        # HDA bus
        yield sysfs.Device(bus = 'hdaudio', name = 'hdaudioC0D3', driver = [ 'snd_hda_codec_hdmi', 'snd_hda_codec_tegrahdmi' ])

        # I2C bus
        yield sysfs.Device(bus = 'i2c', name = '0-0050', driver = 'at24')
        yield sysfs.Device(bus = 'i2c', name = '0-0057', driver = 'at24')
        yield sysfs.Device(bus = 'i2c', name = '1-003c', driver = 'max77620')
        yield sysfs.Device(bus = 'i2c', name = '1-0068', driver = 'dummy')

        # PCI bus
        yield sysfs.Device(bus = 'pci', name = '0000:00:02.0', driver = 'pcieport')
        yield sysfs.Device(bus = 'pci', name = '0000:01:00.0', driver = 'r8169')

        # host1x bus
        yield sysfs.Device(bus = 'host1x', name = 'drm', driver = 'drm')

        # Linux v5.9 enabled support for the Tegra VI/CSI V4L2 driver on Jetson Nano
        if kernel.version >= '5.9.0':
            yield sysfs.Device(bus = 'host1x', name = 'tegra-video', driver = 'tegra-video')

    def _build_drivers(self, kernel):
        yield from super()._build_drivers(kernel)

        yield sysfs.Driver('platform', 'tegra-host1x')

    def _build_allowlist(self, kernel):
        yield r'EINJ: ACPI disabled.'
        yield r'pci_bus [0-9a-fA-F]{4}:[0-9a-fA-F]{2}: \d+-byte config .* to [0-9a-fA-F]{4}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}\.\d offset 0x[0-9a-fA-F]+ may corrupt adjacent RW1C bits'
        yield r'pci [0-9a-fA-F]{4}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}\.[0-9a-fA-F]: nv_msi_ht_cap_quirk didn\'t locate host bridge'
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

        i2c = self.soc.devices['i2c3']

        self.eeproms['module'] = i2c.client(0x50)
        self.eeproms['system'] = i2c.client(0x57)
