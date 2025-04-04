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
        sysfs.Device(bus = 'platform', name = 'pwm-fan' if Kernel().version >= Kernel.Version('5.19.0') else 'fan', driver = 'pwm-fan'),
        sysfs.Device(bus = 'platform', name = 'gpio-keys', driver = 'gpio-keys'),
        sysfs.Device(bus = 'platform', name = 'max20024-pinctrl', driver = 'max77620-pinctrl'),
        sysfs.Device(bus = 'platform', name = 'max20024-pmic', driver = 'max77620-pmic'),
        sysfs.Device(bus = 'platform', name = 'max77620-gpio', driver = 'max77620-gpio'),
        sysfs.Device(bus = 'platform', name = 'max77620-rtc', driver = 'max77686-rtc'),
        sysfs.Device(bus = 'platform', name = 'serial' if Kernel().version >= Kernel.Version('5.17.0') else 'tcu', driver = 'tegra-tcu'),
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
            sysfs.Device(bus = 'platform', name = '2c00000.memory-controller', driver = [ 'tegra186-mc', 'tegra-mc' ]),
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
    # and support for ACONNECT, ADMA and AGIC
    ] + [
        device for device in [
            sysfs.Device(bus = 'platform', name = 'bus@0:aconnect@2900000', driver = 'tegra-aconnect'),
            sysfs.Device(bus = 'platform', name = '2930000.dma-controller', driver = 'tegra-adma'),
            sysfs.Device(bus = 'platform', name = '2a41000.interrupt-controller', driver = 'gic'),
            sysfs.Device(bus = 'platform', name = '3160000.i2c', driver = 'tegra-i2c'),
        ] if Kernel().version >= Kernel.Version('5.10.0')
    # Linux v5.12 enabled support for the Audio Processing Engine
    ] + [
        device for device in [
            sysfs.Device(bus = 'platform', name = '2900800.ahub', driver = 'tegra210-ahub'),
            sysfs.Device(bus = 'platform', name = '2901000.i2s', driver = 'tegra210-i2s'),
            sysfs.Device(bus = 'platform', name = '2901100.i2s', driver = 'tegra210-i2s'),
            sysfs.Device(bus = 'platform', name = '2901300.i2s', driver = 'tegra210-i2s'),
            sysfs.Device(bus = 'platform', name = '2901500.i2s', driver = 'tegra210-i2s'),
            sysfs.Device(bus = 'platform', name = '2904200.dmic', driver = 'tegra210-dmic'),
            sysfs.Device(bus = 'platform', name = '290f000.admaif', driver = 'tegra210-admaif'),
            sysfs.Device(bus = 'platform', name = 'sound', driver = 'tegra-audio-graph-card'),
        ] if Kernel().version >= Kernel.Version('5.12.0')
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
        r'.*: loading out-of-tree module taints kernel.',
        r'OF: (fdt|reserved mem): Reserved memory: unsupported node format, ignoring',
        r'EINJ: ACPI disabled.',
        r'cacheinfo: Unable to detect cache hierarchy for CPU 0',
        r'dwc-eth-dwmac 2490000.ethernet: Cannot get CSR clock',
        r'mmc0: Unknown controller version \(5\). You may experience problems.',
        r'mmc1: Unknown controller version \(5\). You may experience problems.',
        r'tegra-dpaux 155e0000.dpaux: 155e0000.dpaux supply vdd not found, using dummy regulator',
        r'tegra-hda 3510000.hda: azx_get_response timeout, switching to polling mode:',
        r'tegra-host1x 13e00000.host1x: Context device 0 has no IOMMU!',
        r'tegra-i2c 31c0000.i2c: deferred probe timeout, ignoring dependency',
        r'\[drm\] parse error at position 6 in video mode \'tegrafb\'',
        r'urandom_read: [0-9]+ callbacks suppressed',
    ] + [
        warning for warning in [
            r'.* sound: ASoC: no DMI vendor name!',
        ] if Kernel().version < Kernel.Version('5.13.0')
    ] + [
        warning for warning in [
            r'kvm: pmu event creation failed -2',
        ] if Kernel().version < Kernel.Version('5.14.0')
    ] + [
        warning for warning in [
            r'mmc0: running CQE recovery',
        ] if Kernel().version >= Kernel.Version('5.17.0')
    ] + [
        warning for warning in [
            r'tegra194-pcie [0-f]+.pcie: Phy link never came up',
        ] if Kernel().version < Kernel.Version('6.2.0')
    ] + [
        warning for warning in [
            r'memfd_create\(\) without MFD_EXEC nor MFD_NOEXEC_SEAL, pid=[0-9]+ \'systemd\'',
        ] if Kernel().version >= Kernel.Version('6.3.0') and Kernel().version < Kernel.Version('6.6.0')
    ] + [
        warning for warning in [
            r'systemd\[[0-9]+\]: memfd_create\(\) called without MFD_EXEC or MFD_NOEXEC_SEAL set',
        ] if Kernel().version >= Kernel.Version('6.4.0')
    ] + [
        warning for warning in [
            r'tegra-mc 2c00000.memory-controller: sync_state\(\) pending due to 15380000.nvjpg',
            r'tegra-mc 2c00000.memory-controller: sync_state\(\) pending due to 154c0000.nvenc',
            r'tegra-mc 2c00000.memory-controller: sync_state\(\) pending due to 15a80000.nvenc',
            r'tegra-mc 2c00000.memory-controller: sync_state\(\) pending due to 17000000.gpu',
        ] if Kernel().version >= Kernel.Version('6.4.0')
    ] + [
        warning for warning in [
            r'tegra186-emc 2c60000.external-memory-controller: sync_state\(\) pending due to 15380000.nvjpg',
            r'tegra186-emc 2c60000.external-memory-controller: sync_state\(\) pending due to 154c0000.nvenc',
            r'tegra186-emc 2c60000.external-memory-controller: sync_state\(\) pending due to 15a80000.nvenc',
            r'tegra186-emc 2c60000.external-memory-controller: sync_state\(\) pending due to 17000000.gpu',
        ] if Kernel().version >= Kernel.Version('6.5.0')
    # List of IRQs that do not support setting the IRQ affinity
    ] + [
        r"IRQ%s: set affinity failed\(-22\)." % irq for irq in [
            sysfs.interrupt_get('ahci[0001:01:00.0]'),
        ]
    ]

    def __init__(self):
        self.soc = tegra194.SoC()
        self.eeproms = {}

        if 'i2c1' in self.soc.devices:
            i2c = self.soc.devices['i2c1']
            self.eeproms['module'] = i2c.client(0x50)
            self.eeproms['system'] = i2c.client(0x56)
