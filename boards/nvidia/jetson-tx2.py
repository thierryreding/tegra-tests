import boards, tegra
from linux.system import Kernel
from linux import sysfs, system
from tegra import tegra186

class Board(boards.Board):
    __compatible__ = 'nvidia,p2771-0000'
    name = 'NVIDIA Jetson TX2 Development Kit'

    def _build_devices(self, kernel):
        yield from super()._build_devices(kernel)

        # platform bus
        yield sysfs.Device(bus = 'platform', name = '2200000.gpio', driver = 'tegra186-gpio')
        yield sysfs.Device(bus = 'platform', name = '2490000.ethernet', driver = 'dwc-eth-dwmac')
        yield sysfs.Device(bus = 'platform', name = '2c00000.memory-controller', driver = [ 'tegra186-mc', 'tegra-mc' ])
        yield sysfs.Device(bus = 'platform', name = '3100000.serial', driver = [ 'of_serial', 'tegra-uart' ])
        yield sysfs.Device(bus = 'platform', name = '3160000.i2c', driver = 'tegra-i2c')
        yield sysfs.Device(bus = 'platform', name = '3180000.i2c', driver = 'tegra-i2c')
        yield sysfs.Device(bus = 'platform', name = '3190000.i2c', driver = 'tegra-i2c')
        yield sysfs.Device(bus = 'platform', name = '31c0000.i2c', driver = 'tegra-i2c')
        yield sysfs.Device(bus = 'platform', name = '31e0000.i2c', driver = 'tegra-i2c')
        yield sysfs.Device(bus = 'platform', name = '3510000.hda', driver = 'tegra-hda')
        yield sysfs.Device(bus = 'platform', name = '3520000.padctl', driver = 'tegra-xusb-padctl')
        yield sysfs.Device(bus = 'platform', name = '3530000.usb', driver = 'tegra-xusb')
        yield sysfs.Device(bus = 'platform', name = '3820000.fuse', driver = 'tegra-fuse')
        yield sysfs.Device(bus = 'platform', name = '3c00000.hsp', driver = 'tegra-hsp')
        yield sysfs.Device(bus = 'platform', name = 'c240000.i2c', driver = 'tegra-i2c')
        yield sysfs.Device(bus = 'platform', name = 'c250000.i2c', driver = 'tegra-i2c')
        yield sysfs.Device(bus = 'platform', name = 'c2a0000.rtc', driver = 'tegra_rtc')
        yield sysfs.Device(bus = 'platform', name = 'c2f0000.gpio', driver = 'tegra186-gpio')
        yield sysfs.Device(bus = 'platform', name = 'c360000.pmc', driver = 'tegra-pmc')
        yield sysfs.Device(bus = 'platform', name = 'e000000.ccplex', driver = 'tegra186-cpufreq')
        yield sysfs.Device(bus = 'platform', name = '10003000.pcie', driver = 'tegra-pcie')
        yield sysfs.Device(bus = 'platform', name = '12000000.iommu', driver = 'arm-smmu')
        yield sysfs.Device(bus = 'platform', name = '13e00000.host1x', driver = 'tegra-host1x')
        yield sysfs.Device(bus = 'platform', name = '15040000.dpaux', driver = 'tegra-dpaux')
        yield sysfs.Device(bus = 'platform', name = '15200000.display', driver = 'tegra-dc')
        yield sysfs.Device(bus = 'platform', name = '15200000.display-hub', driver = 'tegra-display-hub')
        yield sysfs.Device(bus = 'platform', name = '15210000.display', driver = 'tegra-dc')
        yield sysfs.Device(bus = 'platform', name = '15220000.display', driver = 'tegra-dc')
        yield sysfs.Device(bus = 'platform', name = '15340000.vic', driver = 'tegra-vic')
        yield sysfs.Device(bus = 'platform', name = '15540000.sor', driver = 'tegra-sor')
        yield sysfs.Device(bus = 'platform', name = '15580000.sor', driver = 'tegra-sor')
        yield sysfs.Device(bus = 'platform', name = '155c0000.dpaux', driver = 'tegra-dpaux')
        yield sysfs.Device(bus = 'platform', name = '30000000.sram', driver = 'sram')
        yield sysfs.Device(bus = 'platform', name = 'bpmp', driver = 'tegra-bpmp')
        yield sysfs.Device(bus = 'platform', name = 'bpmp:i2c', driver = 'tegra-bpmp-i2c')
        yield sysfs.Device(bus = 'platform', name = 'bpmp:thermal', driver = 'tegra-bpmp-thermal')
        yield sysfs.Device(bus = 'platform', name = 'gpio-keys', driver = 'gpio-keys')
        yield sysfs.Device(bus = 'platform', name = 'max77620-gpio', driver = 'max77620-gpio')
        yield sysfs.Device(bus = 'platform', name = 'max77620-pinctrl', driver = 'max77620-pinctrl')
        yield sysfs.Device(bus = 'platform', name = 'max77620-pmic', driver = 'max77620-pmic')
        yield sysfs.Device(bus = 'platform', name = 'max77620-rtc', driver = 'max77686-rtc')

        # Device trees in Linux v5.9 changed sdhci@... to mmc@...
        if kernel.version < '5.9.0':
            yield sysfs.Device(bus = 'platform', name = '3400000.sdhci', driver = 'sdhci-tegra')
            yield sysfs.Device(bus = 'platform', name = '3440000.sdhci', driver = 'sdhci-tegra')
            yield sysfs.Device(bus = 'platform', name = '3460000.sdhci', driver = 'sdhci-tegra')
        else:
            yield sysfs.Device(bus = 'platform', name = '3400000.mmc', driver = 'sdhci-tegra')
            yield sysfs.Device(bus = 'platform', name = '3440000.mmc', driver = 'sdhci-tegra')
            yield sysfs.Device(bus = 'platform', name = '3460000.mmc', driver = 'sdhci-tegra')

        # Linux v5.12 enabled support for the Audio Processing Engine
        if kernel.version >= '5.12.0':
            yield sysfs.Device(bus = 'platform', name = 'aconnect@2900000', driver = 'tegra-aconnect')
            yield sysfs.Device(bus = 'platform', name = '2900800.ahub', driver = 'tegra210-ahub')
            yield sysfs.Device(bus = 'platform', name = '2901000.i2s', driver = 'tegra210-i2s')
            yield sysfs.Device(bus = 'platform', name = '2901100.i2s', driver = 'tegra210-i2s')
            yield sysfs.Device(bus = 'platform', name = '2901200.i2s', driver = 'tegra210-i2s')
            yield sysfs.Device(bus = 'platform', name = '2901300.i2s', driver = 'tegra210-i2s')
            yield sysfs.Device(bus = 'platform', name = '2901400.i2s', driver = 'tegra210-i2s')
            yield sysfs.Device(bus = 'platform', name = '2901500.i2s', driver = 'tegra210-i2s')
            yield sysfs.Device(bus = 'platform', name = '2904000.dmic', driver = 'tegra210-dmic')
            yield sysfs.Device(bus = 'platform', name = '2904000.dmic', driver = 'tegra210-dmic')
            yield sysfs.Device(bus = 'platform', name = '2904100.dmic', driver = 'tegra210-dmic')
            yield sysfs.Device(bus = 'platform', name = '2904200.dmic', driver = 'tegra210-dmic')
            yield sysfs.Device(bus = 'platform', name = '2905000.dspk', driver = 'tegra186-dspk')
            yield sysfs.Device(bus = 'platform', name = '2905100.dspk', driver = 'tegra186-dspk')
            yield sysfs.Device(bus = 'platform', name = '290f000.admaif', driver = 'tegra210-admaif')
            yield sysfs.Device(bus = 'platform', name = '2930000.dma-controller', driver = 'tegra-adma')
            yield sysfs.Device(bus = 'platform', name = '2a41000.interrupt-controller', driver = 'gic')
            yield sysfs.Device(bus = 'platform', name = 'sound', driver = 'tegra-audio-graph-card')

        # HDA bus
        yield sysfs.Device(bus = 'hdaudio', name = 'hdaudioC0D3', driver = [ 'snd_hda_codec_hdmi', 'snd_hda_codec_tegrahdmi' ])
        yield sysfs.Device(bus = 'hdaudio', name = 'hdaudioC0D4', driver = [ 'snd_hda_codec_hdmi', 'snd_hda_codec_tegrahdmi' ])

        # I2C bus
        yield sysfs.Device(bus = 'i2c', name = '0-003c', driver = 'max77620')
        yield sysfs.Device(bus = 'i2c', name = '1-0040', driver = 'ina3221')
        yield sysfs.Device(bus = 'i2c', name = '1-0041', driver = 'ina3221')
        yield sysfs.Device(bus = 'i2c', name = '1-0042', driver = 'ina3221')
        yield sysfs.Device(bus = 'i2c', name = '1-0043', driver = 'ina3221')
        yield sysfs.Device(bus = 'i2c', name = '1-0074', driver = 'pca953x')
        yield sysfs.Device(bus = 'i2c', name = '1-0077', driver = 'pca953x')
        yield sysfs.Device(bus = 'i2c', name = '6-0050', driver = 'at24')
        yield sysfs.Device(bus = 'i2c', name = '6-0057', driver = 'at24')

        # host1x bus
        yield sysfs.Device(bus = 'host1x', name = 'drm', driver = 'drm')

    def _build_drivers(self, kernel):
        yield from super()._build_drivers(kernel)

        yield sysfs.Driver('platform', 'tegra-host1x')

    def _build_allowlist(self, kernel):
        yield from super()._build_allowlist(kernel)

        yield r'CPU features: SANITY CHECK: .*',
        yield r'CPU features: Unsupported CPU feature variation detected',
        yield r'EINJ: ACPI disabled.',
        yield r'dwc-eth-dwmac 2490000.ethernet: Cannot get CSR clock',
        yield r'dwc-eth-dwmac 2490000.ethernet: PTP uses main clock',
        yield r'tegra-i2c 3190000.i2c: deferred probe timeout, ignoring dependency',
        yield r'urandom_read: [0-9]+ callbacks suppressed',

        if kernel.version < '5.13.0':
            yield r'.* sound: ASoC: no DMI vendor name!'

        if kernel.version >= '6.3.0' and kernel.version < '6.6.0':
            yield r'memfd_create\(\) without MFD_EXEC nor MFD_NOEXEC_SEAL, pid=[0-9]+ \'systemd\''

        if kernel.version >= '6.4.0':
            yield r'systemd\[[0-9]+\]: memfd_create\(\) called without MFD_EXEC or MFD_NOEXEC_SEAL set'

        if kernel.version >= '6.4.0':
            yield r'tegra-mc 2c00000.memory-controller: sync_state\(\) pending due to 15380000.nvjpg'
            yield r'tegra-mc 2c00000.memory-controller: sync_state\(\) pending due to 154c0000.nvenc'
            yield r'tegra-mc 2c00000.memory-controller: sync_state\(\) pending due to 3507000.sata'

        if kernel.version >= '6.5.0':
            yield r'tegra186-emc 2c60000.external-memory-controller: sync_state\(\) pending due to 15380000.nvjpg'
            yield r'tegra186-emc 2c60000.external-memory-controller: sync_state\(\) pending due to 154c0000.nvenc'
            yield r'tegra186-emc 2c60000.external-memory-controller: sync_state\(\) pending due to 3507000.sata'

        if kernel.version >= '6.17.0':
            yield r'tegra-bpmp bpmp: sync_state\(\) pending due to 3960000.cec'
            yield r'tegra-bpmp bpmp: sync_state\(\) pending due to 3507000.sata'
            yield r'tegra-bpmp bpmp: sync_state\(\) pending due to 15380000.nvjpg'
            yield r'tegra-bpmp bpmp: sync_state\(\) pending due to 154c0000.nvenc'

        if kernel.version >= '6.19.0' and kernel.version < '7.0.0':
            yield r'tegra210-ahub 2900800.ahub: using zero-initialized flat cache, this may cause unexpected behavior'

    def __init__(self, kernel = Kernel()):
        super().__init__(tegra186.SoC(), kernel)

        self.eeproms = {}

        i2c = self.soc.devices['i2c8']

        self.eeproms['module'] = i2c.client(0x50)
        self.eeproms['system'] = i2c.client(0x57)
