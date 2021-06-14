import boards, tegra
from linux.system import Kernel
from linux import sysfs, system
from tegra import tegra186

class Board(boards.Board):
    __compatible__ = 'nvidia,p2771-0000'
    name = 'NVIDIA Jetson TX2 Development Kit'

    devices = [
        # platform bus
        sysfs.Device(bus = 'platform', name = '2200000.gpio', driver = 'tegra186-gpio'),
        sysfs.Device(bus = 'platform', name = '2490000.ethernet', driver = 'dwc-eth-dwmac'),
        sysfs.Device(bus = 'platform', name = '2c00000.memory-controller', driver = [ 'tegra186-mc', 'tegra-mc' ]),
        sysfs.Device(bus = 'platform', name = '3100000.serial', driver = [ 'of_serial', 'tegra-uart' ]),
        sysfs.Device(bus = 'platform', name = '3160000.i2c', driver = 'tegra-i2c'),
        sysfs.Device(bus = 'platform', name = '3180000.i2c', driver = 'tegra-i2c'),
        sysfs.Device(bus = 'platform', name = '3190000.i2c', driver = 'tegra-i2c'),
        sysfs.Device(bus = 'platform', name = '31c0000.i2c', driver = 'tegra-i2c'),
        sysfs.Device(bus = 'platform', name = '31e0000.i2c', driver = 'tegra-i2c'),
        sysfs.Device(bus = 'platform', name = '3510000.hda', driver = 'tegra-hda'),
        sysfs.Device(bus = 'platform', name = '3520000.padctl', driver = 'tegra-xusb-padctl'),
        sysfs.Device(bus = 'platform', name = '3530000.usb', driver = 'tegra-xusb'),
        sysfs.Device(bus = 'platform', name = '3820000.fuse', driver = 'tegra-fuse'),
        sysfs.Device(bus = 'platform', name = '3c00000.hsp', driver = 'tegra-hsp'),
        sysfs.Device(bus = 'platform', name = 'c240000.i2c', driver = 'tegra-i2c'),
        sysfs.Device(bus = 'platform', name = 'c250000.i2c', driver = 'tegra-i2c'),
        sysfs.Device(bus = 'platform', name = 'c2a0000.rtc', driver = 'tegra_rtc'),
        sysfs.Device(bus = 'platform', name = 'c2f0000.gpio', driver = 'tegra186-gpio'),
        sysfs.Device(bus = 'platform', name = 'c360000.pmc', driver = 'tegra-pmc'),
        sysfs.Device(bus = 'platform', name = 'e000000.ccplex', driver = 'tegra186-cpufreq'),
        sysfs.Device(bus = 'platform', name = '10003000.pcie', driver = 'tegra-pcie'),
        sysfs.Device(bus = 'platform', name = '12000000.iommu', driver = 'arm-smmu'),
        sysfs.Device(bus = 'platform', name = '13e00000.host1x', driver = 'tegra-host1x'),
        sysfs.Device(bus = 'platform', name = '15040000.dpaux', driver = 'tegra-dpaux'),
        sysfs.Device(bus = 'platform', name = '15200000.display', driver = 'tegra-dc'),
        sysfs.Device(bus = 'platform', name = '15200000.display-hub', driver = 'tegra-display-hub'),
        sysfs.Device(bus = 'platform', name = '15210000.display', driver = 'tegra-dc'),
        sysfs.Device(bus = 'platform', name = '15220000.display', driver = 'tegra-dc'),
        sysfs.Device(bus = 'platform', name = '15340000.vic', driver = 'tegra-vic'),
        sysfs.Device(bus = 'platform', name = '15540000.sor', driver = 'tegra-sor'),
        sysfs.Device(bus = 'platform', name = '15580000.sor', driver = 'tegra-sor'),
        sysfs.Device(bus = 'platform', name = '155c0000.dpaux', driver = 'tegra-dpaux'),
        sysfs.Device(bus = 'platform', name = '30000000.sram', driver = 'sram'),
        sysfs.Device(bus = 'platform', name = 'bpmp', driver = 'tegra-bpmp'),
        sysfs.Device(bus = 'platform', name = 'bpmp:i2c', driver = 'tegra-bpmp-i2c'),
        sysfs.Device(bus = 'platform', name = 'bpmp:thermal', driver = 'tegra-bpmp-thermal'),
        sysfs.Device(bus = 'platform', name = 'gpio-keys', driver = 'gpio-keys'),
        sysfs.Device(bus = 'platform', name = 'max77620-gpio', driver = 'max77620-gpio'),
        sysfs.Device(bus = 'platform', name = 'max77620-pinctrl', driver = 'max77620-pinctrl'),
        sysfs.Device(bus = 'platform', name = 'max77620-pmic', driver = 'max77620-pmic'),
        sysfs.Device(bus = 'platform', name = 'max77620-rtc', driver = 'max77686-rtc'),
    # Device trees in Linux v5.9 changed sdhci@... to mmc@...
    ] + [
        device for device in [
            sysfs.Device(bus = 'platform', name = '3400000.sdhci', driver = 'sdhci-tegra'),
            sysfs.Device(bus = 'platform', name = '3440000.sdhci', driver = 'sdhci-tegra'),
            sysfs.Device(bus = 'platform', name = '3460000.sdhci', driver = 'sdhci-tegra'),
        ] if Kernel().version < Kernel.Version('5.9.0')
    ] + [
        device for device in [
            sysfs.Device(bus = 'platform', name = '3400000.mmc', driver = 'sdhci-tegra'),
            sysfs.Device(bus = 'platform', name = '3440000.mmc', driver = 'sdhci-tegra'),
            sysfs.Device(bus = 'platform', name = '3460000.mmc', driver = 'sdhci-tegra'),
        ] if Kernel().version >= Kernel.Version('5.9.0')
    # Linux v5.12 enabled support for the Audio Processing Engine
    ] + [
        device for device in [
            sysfs.Device(bus = 'platform', name = 'aconnect@2900000', driver = 'tegra-aconnect'),
            sysfs.Device(bus = 'platform', name = '2900800.ahub', driver = 'tegra210-ahub'),
            sysfs.Device(bus = 'platform', name = '2901000.i2s', driver = 'tegra210-i2s'),
            sysfs.Device(bus = 'platform', name = '2901100.i2s', driver = 'tegra210-i2s'),
            sysfs.Device(bus = 'platform', name = '2901200.i2s', driver = 'tegra210-i2s'),
            sysfs.Device(bus = 'platform', name = '2901300.i2s', driver = 'tegra210-i2s'),
            sysfs.Device(bus = 'platform', name = '2901400.i2s', driver = 'tegra210-i2s'),
            sysfs.Device(bus = 'platform', name = '2901500.i2s', driver = 'tegra210-i2s'),
            sysfs.Device(bus = 'platform', name = '2904000.dmic', driver = 'tegra210-dmic'),
            sysfs.Device(bus = 'platform', name = '2904000.dmic', driver = 'tegra210-dmic'),
            sysfs.Device(bus = 'platform', name = '2904100.dmic', driver = 'tegra210-dmic'),
            sysfs.Device(bus = 'platform', name = '2904200.dmic', driver = 'tegra210-dmic'),
            sysfs.Device(bus = 'platform', name = '2905000.dspk', driver = 'tegra186-dspk'),
            sysfs.Device(bus = 'platform', name = '2905100.dspk', driver = 'tegra186-dspk'),
            sysfs.Device(bus = 'platform', name = '290f000.admaif', driver = 'tegra210-admaif'),
            sysfs.Device(bus = 'platform', name = '2930000.dma-controller', driver = 'tegra-adma'),
            sysfs.Device(bus = 'platform', name = '2a41000.interrupt-controller', driver = 'gic'),
            sysfs.Device(bus = 'platform', name = 'sound', driver = 'tegra-audio-graph-card'),
        ] if Kernel().version >= Kernel.Version('5.12.0')
    # HDA bus
    ] + [
        sysfs.Device(bus = 'hdaudio', name = 'hdaudioC0D3', driver = 'snd_hda_codec_hdmi'),
        sysfs.Device(bus = 'hdaudio', name = 'hdaudioC0D4', driver = 'snd_hda_codec_hdmi'),
    # I2C bus
    ] + [
        sysfs.Device(bus = 'i2c', name = '0-003c', driver = 'max77620'),
        sysfs.Device(bus = 'i2c', name = '1-0040', driver = 'ina3221'),
        sysfs.Device(bus = 'i2c', name = '1-0041', driver = 'ina3221'),
        sysfs.Device(bus = 'i2c', name = '1-0042', driver = 'ina3221'),
        sysfs.Device(bus = 'i2c', name = '1-0043', driver = 'ina3221'),
        sysfs.Device(bus = 'i2c', name = '1-0074', driver = 'pca953x'),
        sysfs.Device(bus = 'i2c', name = '1-0077', driver = 'pca953x'),
        sysfs.Device(bus = 'i2c', name = '6-0050', driver = 'at24'),
        sysfs.Device(bus = 'i2c', name = '6-0057', driver = 'at24'),
    # host1x bus
    ] + [
        sysfs.Device(bus = 'host1x', name = 'drm', driver = 'drm'),
    ]

    drivers = [
        sysfs.Driver('platform', 'tegra-host1x'),
    ]

    allowlist = [
        r'CPU features: SANITY CHECK: .*',
        r'CPU features: Unsupported CPU feature variation detected',
        r'EINJ: ACPI disabled.',
        r'dwc-eth-dwmac 2490000.ethernet: Cannot get CSR clock',
        r'dwc-eth-dwmac 2490000.ethernet: PTP uses main clock',
        r'tegra-i2c 3190000.i2c: deferred probe timeout, ignoring dependency',
        r'urandom_read: [0-9]+ callbacks suppressed',
    ] + [
        warning for warning in [
            r'.* sound: ASoC: no DMI vendor name!',
        ] if Kernel().version < Kernel.Version('5.13.0')
    ]

    def __init__(self):
        self.soc = tegra186.SoC()
        self.eeproms = {}

        i2c = self.soc.devices['i2c8']

        self.eeproms['module'] = i2c.device(0x50)
        self.eeproms['system'] = i2c.device(0x57)
