import boards, tegra
from linux.system import Kernel
from linux import sysfs
from tegra import tegra194

class Board(boards.Board):
    __compatible__ = 'nvidia,p3509-0000+p3668-0000'
    name = 'NVIDIA Jetson Xavier NX Developer Kit'

    def _build_devices(self, kernel):
        yield from super()._build_devices(kernel)

        # platform bus
        yield sysfs.Device(bus = 'platform', name = '13e00000.host1x', driver = 'tegra-host1x')
        yield sysfs.Device(bus = 'platform', name = '14160000.pcie', driver = 'tegra194-pcie')
        yield sysfs.Device(bus = 'platform', name = '141a0000.pcie', driver = 'tegra194-pcie')
        yield sysfs.Device(bus = 'platform', name = '15200000.display', driver = 'tegra-dc')
        yield sysfs.Device(bus = 'platform', name = '15200000.display-hub', driver = 'tegra-display-hub')
        yield sysfs.Device(bus = 'platform', name = '15210000.display', driver = 'tegra-dc')
        yield sysfs.Device(bus = 'platform', name = '15220000.display', driver = 'tegra-dc')
        yield sysfs.Device(bus = 'platform', name = '15230000.display', driver = 'tegra-dc')
        yield sysfs.Device(bus = 'platform', name = '15340000.vic', driver = 'tegra-vic')
        yield sysfs.Device(bus = 'platform', name = '155c0000.dpaux', driver = 'tegra-dpaux')
        yield sysfs.Device(bus = 'platform', name = '155d0000.dpaux', driver = 'tegra-dpaux')
        yield sysfs.Device(bus = 'platform', name = '15b00000.sor', driver = 'tegra-sor')
        yield sysfs.Device(bus = 'platform', name = '15b40000.sor', driver = 'tegra-sor')
        yield sysfs.Device(bus = 'platform', name = '2200000.gpio', driver = 'tegra186-gpio')
        yield sysfs.Device(bus = 'platform', name = '2430000.pinmux', driver = 'tegra194-pinctrl')
        yield sysfs.Device(bus = 'platform', name = '2490000.ethernet', driver = 'dwc-eth-dwmac')
        yield sysfs.Device(bus = 'platform', name = '2c00000.memory-controller', driver = [ 'tegra186-mc', 'tegra-mc' ])
        yield sysfs.Device(bus = 'platform', name = '3100000.serial', driver = [ 'of_serial', 'tegra-uart' ])
        yield sysfs.Device(bus = 'platform', name = '3190000.i2c', driver = 'tegra-i2c')
        yield sysfs.Device(bus = 'platform', name = '32d0000.pwm', driver = 'tegra-pwm')
        yield sysfs.Device(bus = 'platform', name = '3400000.mmc', driver = 'sdhci-tegra')
        yield sysfs.Device(bus = 'platform', name = '3510000.hda', driver = 'tegra-hda')
        yield sysfs.Device(bus = 'platform', name = '3520000.padctl', driver = 'tegra-xusb-padctl')
        yield sysfs.Device(bus = 'platform', name = '3610000.usb', driver = 'tegra-xusb')
        yield sysfs.Device(bus = 'platform', name = '3820000.fuse', driver = 'tegra-fuse')
        yield sysfs.Device(bus = 'platform', name = '3c00000.hsp', driver = 'tegra-hsp')
        yield sysfs.Device(bus = 'platform', name = '3e10000.phy', driver = 'tegra194-p2u')
        yield sysfs.Device(bus = 'platform', name = '3e20000.phy', driver = 'tegra194-p2u')
        yield sysfs.Device(bus = 'platform', name = '3e30000.phy', driver = 'tegra194-p2u')
        yield sysfs.Device(bus = 'platform', name = '3e40000.phy', driver = 'tegra194-p2u')
        yield sysfs.Device(bus = 'platform', name = '3e50000.phy', driver = 'tegra194-p2u')
        yield sysfs.Device(bus = 'platform', name = '3e60000.phy', driver = 'tegra194-p2u')
        yield sysfs.Device(bus = 'platform', name = '3e70000.phy', driver = 'tegra194-p2u')
        yield sysfs.Device(bus = 'platform', name = '3e80000.phy', driver = 'tegra194-p2u')
        yield sysfs.Device(bus = 'platform', name = '3e90000.phy', driver = 'tegra194-p2u')
        yield sysfs.Device(bus = 'platform', name = '3ea0000.phy', driver = 'tegra194-p2u')
        yield sysfs.Device(bus = 'platform', name = '3eb0000.phy', driver = 'tegra194-p2u')
        yield sysfs.Device(bus = 'platform', name = '3ec0000.phy', driver = 'tegra194-p2u')
        yield sysfs.Device(bus = 'platform', name = '3ed0000.phy', driver = 'tegra194-p2u')
        yield sysfs.Device(bus = 'platform', name = '3ee0000.phy', driver = 'tegra194-p2u')
        yield sysfs.Device(bus = 'platform', name = '3ef0000.phy', driver = 'tegra194-p2u')
        yield sysfs.Device(bus = 'platform', name = '3f00000.phy', driver = 'tegra194-p2u')
        yield sysfs.Device(bus = 'platform', name = '3f10000.phy', driver = 'tegra194-p2u')
        yield sysfs.Device(bus = 'platform', name = '3f20000.phy', driver = 'tegra194-p2u')
        yield sysfs.Device(bus = 'platform', name = '3f30000.phy', driver = 'tegra194-p2u')
        yield sysfs.Device(bus = 'platform', name = '3f40000.phy', driver = 'tegra194-p2u')
        yield sysfs.Device(bus = 'platform', name = 'c150000.hsp', driver = 'tegra-hsp')
        yield sysfs.Device(bus = 'platform', name = 'c2a0000.rtc', driver = 'tegra_rtc')
        yield sysfs.Device(bus = 'platform', name = 'c2f0000.gpio', driver = 'tegra186-gpio')
        yield sysfs.Device(bus = 'platform', name = 'c360000.pmc', driver = 'tegra-pmc')
        yield sysfs.Device(bus = 'platform', name = '40000000.sram', driver = 'sram')
        yield sysfs.Device(bus = 'platform', name = 'bpmp', driver = 'tegra-bpmp')
        yield sysfs.Device(bus = 'platform', name = 'bpmp:i2c', driver = 'tegra-bpmp-i2c')
        yield sysfs.Device(bus = 'platform', name = 'bpmp:thermal', driver = 'tegra-bpmp-thermal')
        yield sysfs.Device(bus = 'platform', name = 'gpio-keys', driver = 'gpio-keys')
        yield sysfs.Device(bus = 'platform', name = 'max20024-pinctrl', driver = 'max77620-pinctrl')
        yield sysfs.Device(bus = 'platform', name = 'max20024-pmic', driver = 'max77620-pmic')
        yield sysfs.Device(bus = 'platform', name = 'max77620-gpio', driver = 'max77620-gpio')
        yield sysfs.Device(bus = 'platform', name = 'max77620-rtc', driver = 'max77686-rtc')

        if kernel.version >= '5.19.0':
            yield sysfs.Device(bus = 'platform', name = 'pwm-fan', driver = 'pwm-fan')
        else:
            yield sysfs.Device(bus = 'platform', name = 'fan', driver = 'pwm-fan')

        if kernel.version >= '5.17.0':
            yield sysfs.Device(bus = 'platform', name = 'serial', driver = 'tegra-tcu')
        else:
            yield sysfs.Device(bus = 'platform', name = 'tcu', driver = 'tegra-tcu')

        # ACONNECT, ADMA and AGIC are available as of Linux v5.10
        if kernel.version >= '5.10.0':
            yield sysfs.Device(bus = 'platform', name = 'bus@0:aconnect@2900000', driver = 'tegra-aconnect')
            yield sysfs.Device(bus = 'platform', name = '2930000.dma-controller', driver = 'tegra-adma')
            yield sysfs.Device(bus = 'platform', name = '2a41000.interrupt-controller', driver = 'gic')

        # Linux v5.14 enabled support for the Audio Processing Engine
        if kernel.version >= '5.14.0':
            yield sysfs.Device(bus = 'platform', name = '2900800.ahub', driver = 'tegra210-ahub')
            yield sysfs.Device(bus = 'platform', name = '2901200.i2s', driver = 'tegra210-i2s')
            yield sysfs.Device(bus = 'platform', name = '2901400.i2s', driver = 'tegra210-i2s')
            yield sysfs.Device(bus = 'platform', name = '2904000.dmic', driver = 'tegra210-dmic')
            yield sysfs.Device(bus = 'platform', name = '2904100.dmic', driver = 'tegra210-dmic')
            yield sysfs.Device(bus = 'platform', name = '2904300.dmic', driver = 'tegra210-dmic')
            yield sysfs.Device(bus = 'platform', name = '2905000.dspk', driver = 'tegra186-dspk')
            yield sysfs.Device(bus = 'platform', name = '2905100.dspk', driver = 'tegra186-dspk')
            yield sysfs.Device(bus = 'platform', name = '290f000.admaif', driver = 'tegra210-admaif')
            yield sysfs.Device(bus = 'platform', name = 'sound', driver = 'tegra-audio-graph-card')

        # HDA bus
        yield sysfs.Device(bus = 'hdaudio', name = 'hdaudioC0D3', driver = [ 'snd_hda_codec_hdmi', 'snd_hda_codec_tegrahdmi' ])
        yield sysfs.Device(bus = 'hdaudio', name = 'hdaudioC0D4', driver = [ 'snd_hda_codec_hdmi', 'snd_hda_codec_tegrahdmi' ])
        yield sysfs.Device(bus = 'hdaudio', name = 'hdaudioC0D5', driver = [ 'snd_hda_codec_hdmi', 'snd_hda_codec_tegrahdmi' ])
        yield sysfs.Device(bus = 'hdaudio', name = 'hdaudioC0D6', driver = [ 'snd_hda_codec_hdmi', 'snd_hda_codec_tegrahdmi' ])

        # I2C bus
        yield sysfs.Device(bus = 'i2c', name = '0-003c', driver = 'max77620')

        # ID EEPROMs are available as of Linux v5.10
        if kernel.version >= '5.10.0':
            yield sysfs.Device(bus = 'i2c', name = '1-0050', driver = 'at24')
            yield sysfs.Device(bus = 'i2c', name = '1-0057', driver = 'at24')

        # host1x bus
        yield sysfs.Device(bus = 'host1x', name = 'drm', driver = 'drm')

    def _build_drivers(self, kernel):
        yield from super()._build_drivers(kernel)

        yield sysfs.Driver('platform', 'tegra-host1x')

    def _build_allowlist(self, kernel):
        yield from super()._build_allowlist(kernel)

        yield r'.*: loading out-of-tree module taints kernel.'
        yield r'OF: (fdt|reserved mem): Reserved memory: unsupported node format, ignoring'
        yield r'EINJ: ACPI disabled.'
        yield r'cacheinfo: Unable to detect cache hierarchy for CPU 0'
        yield r'dwc-eth-dwmac 2490000.ethernet: Cannot get CSR clock'
        yield r'mmc0: Unknown controller version \(5\). You may experience problems.'
        yield r'mmc1: Unknown controller version \(5\). You may experience problems.'
        yield r'tegra-dpaux 155e0000.dpaux: 155e0000.dpaux supply vdd not found, using dummy regulator'
        yield r'\[drm\] parse error at position 6 in video mode \'tegrafb\''
        yield r'urandom_read: [0-9]+ callbacks suppressed'

        if kernel.version < '5.13.0':
            yield r'.* sound: ASoC: no DMI vendor name!'

        if kernel.version == '5.13.0':
            yield r'kvm: pmu event creation failed -2'

        if kernel.version < '6.2.0':
            yield r'tegra194-pcie [0-f]+.pcie: Phy link never came up'

        if kernel.version >= '6.3.0' and kernel.version < '6.6.0':
            yield r'memfd_create\(\) without MFD_EXEC nor MFD_NOEXEC_SEAL, pid=[0-9]+ \'systemd\''

        if kernel.version >= '6.4.0':
            yield r'systemd\[[0-9]+\]: memfd_create\(\) called without MFD_EXEC or MFD_NOEXEC_SEAL set'

        if kernel.version >= '6.4.0':
            yield r'tegra-mc 2c00000.memory-controller: sync_state\(\) pending due to 15380000.nvjpg'
            yield r'tegra-mc 2c00000.memory-controller: sync_state\(\) pending due to 154c0000.nvenc'
            yield r'tegra-mc 2c00000.memory-controller: sync_state\(\) pending due to 15a80000.nvenc'
            yield r'tegra-mc 2c00000.memory-controller: sync_state\(\) pending due to 17000000.gpu'

        if kernel.version >= '6.5.0':
            yield r'tegra186-emc 2c60000.external-memory-controller: sync_state\(\) pending due to 15380000.nvjpg'
            yield r'tegra186-emc 2c60000.external-memory-controller: sync_state\(\) pending due to 154c0000.nvenc'
            yield r'tegra186-emc 2c60000.external-memory-controller: sync_state\(\) pending due to 15a80000.nvenc'
            yield r'tegra186-emc 2c60000.external-memory-controller: sync_state\(\) pending due to 17000000.gpu'

        if kernel.version >= '6.17.0':
            yield r'tegra-bpmp bpmp: sync_state\(\) pending due to 3960000.cec'
            yield r'tegra-bpmp bpmp: sync_state\(\) pending due to 17000000.gpu'
            yield r'tegra-bpmp bpmp: sync_state\(\) pending due to 15380000.nvjpg'
            yield r'tegra-bpmp bpmp: sync_state\(\) pending due to 154c0000.nvenc'
            yield r'tegra-bpmp bpmp: sync_state\(\) pending due to 15a80000.nvenc'

        if kernel.version >= '6.19.0' and kernel.version < '7.0.0':
            yield r'tegra210-ahub 2900800.ahub: using zero-initialized flat cache, this may cause unexpected behavior'

    def __init__(self, kernel = Kernel()):
        super().__init__(tegra194.SoC(), kernel)

        self.eeproms = {}

        if 'i2c1' in self.soc.devices:
            i2c = self.soc.devices['i2c1']
            self.eeproms['module'] = i2c.client(0x50)
            self.eeproms['system'] = i2c.client(0x57)
