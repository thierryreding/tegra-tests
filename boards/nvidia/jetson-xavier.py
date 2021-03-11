import boards, tegra
from linux.system import Kernel
from linux import sysfs
from tegra import tegra194

class Board(boards.Board):
    __compatible__ = 'nvidia,p2972-0000'
    name = 'NVIDIA Jetson Xavier Development Kit'

    devices = [
        # platform bus
        sysfs.Device(bus = 'platform', name = '2200000.gpio', driver = 'tegra186-gpio'),
        sysfs.Device(bus = 'platform', name = '2430000.pinmux', driver = 'tegra194-pinctrl'),
        sysfs.Device(bus = 'platform', name = '2490000.ethernet', driver = 'dwc-eth-dwmac'),
        sysfs.Device(bus = 'platform', name = '3110000.serial', driver = [ 'of_serial', 'tegra-uart' ]),
        sysfs.Device(bus = 'platform', name = '31c0000.i2c', driver = 'tegra-i2c'),
        sysfs.Device(bus = 'platform', name = '31c0000.i2c', driver = 'tegra-i2c'),
        sysfs.Device(bus = 'platform', name = '3510000.hda', driver = 'tegra-hda'),
        sysfs.Device(bus = 'platform', name = '3c00000.hsp', driver = 'tegra-hsp'),
        sysfs.Device(bus = 'platform', name = '3e10000.phy', driver = 'tegra194-p2u'),
        sysfs.Device(bus = 'platform', name = '3e20000.phy', driver = 'tegra194-p2u'),
        sysfs.Device(bus = 'platform', name = '3e30000.phy', driver = 'tegra194-p2u'),
        sysfs.Device(bus = 'platform', name = '3e40000.phy', driver = 'tegra194-p2u'),
        sysfs.Device(bus = 'platform', name = '3e50000.phy', driver = 'tegra194-p2u'),
        sysfs.Device(bus = 'platform', name = '3e60000.phy', driver = 'tegra194-p2u'),
        sysfs.Device(bus = 'platform', name = '3e70000.phy', driver = 'tegra194-p2u'),
        sysfs.Device(bus = 'platform', name = '3e80000.phy', driver = 'tegra194-p2u'),
        sysfs.Device(bus = 'platform', name = '3e90000.phy', driver = 'tegra194-p2u'),
        sysfs.Device(bus = 'platform', name = '3ea0000.phy', driver = 'tegra194-p2u'),
        sysfs.Device(bus = 'platform', name = '3eb0000.phy', driver = 'tegra194-p2u'),
        sysfs.Device(bus = 'platform', name = '3ec0000.phy', driver = 'tegra194-p2u'),
        sysfs.Device(bus = 'platform', name = '3ed0000.phy', driver = 'tegra194-p2u'),
        sysfs.Device(bus = 'platform', name = '3ee0000.phy', driver = 'tegra194-p2u'),
        sysfs.Device(bus = 'platform', name = '3ef0000.phy', driver = 'tegra194-p2u'),
        sysfs.Device(bus = 'platform', name = '3f00000.phy', driver = 'tegra194-p2u'),
        sysfs.Device(bus = 'platform', name = '3f10000.phy', driver = 'tegra194-p2u'),
        sysfs.Device(bus = 'platform', name = '3f20000.phy', driver = 'tegra194-p2u'),
        sysfs.Device(bus = 'platform', name = '3f30000.phy', driver = 'tegra194-p2u'),
        sysfs.Device(bus = 'platform', name = '3f40000.phy', driver = 'tegra194-p2u'),
        sysfs.Device(bus = 'platform', name = 'c150000.hsp', driver = 'tegra-hsp'),
        sysfs.Device(bus = 'platform', name = 'c2a0000.rtc', driver = 'tegra_rtc'),
        sysfs.Device(bus = 'platform', name = 'c2f0000.gpio', driver = 'tegra186-gpio'),
        sysfs.Device(bus = 'platform', name = 'c340000.pwm', driver = 'tegra-pwm'),
        sysfs.Device(bus = 'platform', name = 'c360000.pmc', driver = 'tegra-pmc'),
        sysfs.Device(bus = 'platform', name = '13e00000.host1x', driver = 'tegra-host1x'),
        sysfs.Device(bus = 'platform', name = '14100000.pcie', driver = 'tegra194-pcie'),
        sysfs.Device(bus = 'platform', name = '14140000.pcie', driver = 'tegra194-pcie'),
        sysfs.Device(bus = 'platform', name = '14180000.pcie', driver = 'tegra194-pcie'),
        sysfs.Device(bus = 'platform', name = '141a0000.pcie', driver = 'tegra194-pcie'),
        sysfs.Device(bus = 'platform', name = '15200000.display', driver = 'tegra-dc'),
        sysfs.Device(bus = 'platform', name = '15200000.display-hub', driver = 'tegra-display-hub'),
        sysfs.Device(bus = 'platform', name = '15210000.display', driver = 'tegra-dc'),
        sysfs.Device(bus = 'platform', name = '15220000.display', driver = 'tegra-dc'),
        sysfs.Device(bus = 'platform', name = '15230000.display', driver = 'tegra-dc'),
        sysfs.Device(bus = 'platform', name = '15340000.vic', driver = 'tegra-vic'),
        sysfs.Device(bus = 'platform', name = '155e0000.dpaux', driver = 'tegra-dpaux'),
        sysfs.Device(bus = 'platform', name = '15b80000.sor', driver = 'tegra-sor'),
        sysfs.Device(bus = 'platform', name = 'bpmp', driver = 'tegra-bpmp'),
        sysfs.Device(bus = 'platform', name = 'bpmp:i2c', driver = 'tegra-bpmp-i2c'),
        sysfs.Device(bus = 'platform', name = 'bpmp:thermal', driver = 'tegra-bpmp-thermal'),
        sysfs.Device(bus = 'platform', name = 'fan', driver = 'pwm-fan'),
        sysfs.Device(bus = 'platform', name = 'gpio-keys', driver = 'gpio-keys'),
        sysfs.Device(bus = 'platform', name = 'max20024-pinctrl', driver = 'max77620-pinctrl'),
        sysfs.Device(bus = 'platform', name = 'max20024-pmic', driver = 'max77620-pmic'),
        sysfs.Device(bus = 'platform', name = 'max77620-gpio', driver = 'max77620-gpio'),
        sysfs.Device(bus = 'platform', name = 'max77620-rtc', driver = 'max77686-rtc'),
        sysfs.Device(bus = 'platform', name = 'tcu', driver = 'tegra-tcu'),
    # Linux v5.5 added support for the PCIe host controllers and Display Port on Jetson AGX Xavier
    ] + [
        device for device in [
            sysfs.Device(bus = 'platform', name = '14100000.pcie', driver = 'tegra194-pcie'),
            sysfs.Device(bus = 'platform', name = '14140000.pcie', driver = 'tegra194-pcie'),
            sysfs.Device(bus = 'platform', name = '14180000.pcie', driver = 'tegra194-pcie'),
            sysfs.Device(bus = 'platform', name = '141a0000.pcie', driver = 'tegra194-pcie'),
            sysfs.Device(bus = 'platform', name = '155c0000.dpaux', driver = 'tegra-dpaux'),
            sysfs.Device(bus = 'platform', name = '155d0000.dpaux', driver = 'tegra-dpaux'),
            sysfs.Device(bus = 'platform', name = '15b00000.sor', driver = 'tegra-sor'),
            sysfs.Device(bus = 'platform', name = '15b40000.sor', driver = 'tegra-sor'),
        ] if Kernel().version >= Kernel.Version('5.5.0')
    # Linux v5.6 added support for the fuse and memory controller on Jetson AGX Xavier
    ] + [
        device for device in [
            sysfs.Device(bus = 'platform', name = '2c00000.memory-controller', driver = 'tegra186-mc'),
            sysfs.Device(bus = 'platform', name = '3820000.fuse', driver = 'tegra-fuse'),
        ] if Kernel().version >= Kernel.Version('5.6.0')
    # Linux v5.7 added support for USB on Jetson AGX Xavier
    ] + [
        device for device in [
            sysfs.Device(bus = 'platform', name = '3520000.padctl', driver = 'tegra-xusb-padctl'),
            sysfs.Device(bus = 'platform', name = '3610000.usb', driver = 'tegra-xusb'),
        ] if Kernel().version >= Kernel.Version('5.7.0')
    # Device trees in Linux v5.9 changed sdhci@... to mmc@... and sysram@... to sram@...
    ] + [
        device for device in [
            sysfs.Device(bus = 'platform', name = '3400000.sdhci', driver = 'sdhci-tegra'),
            sysfs.Device(bus = 'platform', name = '3460000.sdhci', driver = 'sdhci-tegra'),
            sysfs.Device(bus = 'platform', name = '40000000.sysram', driver = 'sram'),
        ] if Kernel().version < Kernel.Version('5.9.0')
    ] + [
        device for device in [
            sysfs.Device(bus = 'platform', name = '3400000.mmc', driver = 'sdhci-tegra'),
            sysfs.Device(bus = 'platform', name = '3460000.mmc', driver = 'sdhci-tegra'),
            sysfs.Device(bus = 'platform', name = '40000000.sram', driver = 'sram'),
        ] if Kernel().version >= Kernel.Version('5.9.0')
    # Linux v5.10 enabled the GEN_I2C1 controller that drives the bus containing ID EEPROMs
    ] + [
        device for device in [
            sysfs.Device(bus = 'platform', name = '3160000.i2c', driver = 'tegra-i2c'),
        ] if Kernel().version >= Kernel.Version('5.10.0')
    # HDA bus
    ] + [
        sysfs.Device(bus = 'hdaudio', name = 'hdaudioC0D3', driver = 'snd_hda_codec_hdmi'),
        sysfs.Device(bus = 'hdaudio', name = 'hdaudioC0D4', driver = 'snd_hda_codec_hdmi'),
        sysfs.Device(bus = 'hdaudio', name = 'hdaudioC0D5', driver = 'snd_hda_codec_hdmi'),
        sysfs.Device(bus = 'hdaudio', name = 'hdaudioC0D6', driver = 'snd_hda_codec_hdmi'),
    # I2C bus
    ] + [
        sysfs.Device(bus = 'i2c', name = '0-003c', driver = 'max77620'),
        sysfs.Device(bus = 'i2c', name = '0-004c', driver = 'lm90'),
    # ID EEPROMs are available as of Linux v5.10
    ] + [
        device for device in [
            sysfs.Device(bus = 'i2c', name = '1-0050', driver = 'at24'),
            sysfs.Device(bus = 'i2c', name = '1-0056', driver = 'at24'),
        ] if Kernel().version >= Kernel.Version('5.10.0')
    # host1x bus
    ] + [
        sysfs.Device(bus = 'host1x', name = 'drm', driver = 'drm'),
    # PCI bus
    ] + [
        sysfs.Device(bus = 'pci', name = '0001:00:00.0', driver = 'pcieport'),
        sysfs.Device(bus = 'pci', name = '0001:01:00.0', driver = 'ahci'),
    ]

    drivers = [
        sysfs.Driver('platform', 'tegra-host1x'),
    ]

    allowlist = [
        r'OF: fdt: Reserved memory: unsupported node format, ignoring',
        r'EINJ: ACPI disabled.',
        r'cacheinfo: Unable to detect cache hierarchy for CPU 0',
        r'dwc-eth-dwmac 2490000.ethernet: Cannot get CSR clock',
        r'mmc0: Unknown controller version \(5\). You may experience problems.',
        r'mmc1: Unknown controller version \(5\). You may experience problems.',
        r'tegra-dpaux 155e0000.dpaux: 155e0000.dpaux supply vdd not found, using dummy regulator',
        r'tegra-hda 3510000.hda: azx_get_response timeout, switching to polling mode:',
        r'tegra-i2c 31c0000.i2c: deferred probe timeout, ignoring dependency',
        r'\[drm\] parse error at position 6 in video mode \'tegrafb\'',
        r'urandom_read: [0-9]+ callbacks suppressed',
    ] + [
        warning for warning in [
            r'.* sound: ASoC: no DMI vendor name!',
        ] if Kernel().version < Kernel.Version('5.13.0')
    ]

    def __init__(self):
        self.soc = tegra194.SoC()
        self.eeproms = {}

        if 'i2c1' in self.soc.devices:
            i2c = self.soc.devices['i2c1']
            self.eeproms['module'] = i2c.device(0x50)
            self.eeproms['system'] = i2c.device(0x56)
