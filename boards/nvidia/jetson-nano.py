import boards
from linux.system import Kernel
from linux import sysfs
from tegra import tegra210

class Board(boards.Board):
    __compatible__ = 'nvidia,p3450-0000'
    name = 'NVIDIA Jetson Nano Developer Kit'

    devices = [
        # platform bus
        sysfs.Device(bus = 'platform', name = '1003000.pcie', driver = 'tegra-pcie'),
        sysfs.Device(bus = 'platform', name = '50000000.host1x', driver = 'tegra-host1x'),
        sysfs.Device(bus = 'platform', name = '54040000.dpaux', driver = 'tegra-dpaux'),
        sysfs.Device(bus = 'platform', name = '54200000.dc', driver = 'tegra-dc'),
        sysfs.Device(bus = 'platform', name = '54240000.dc', driver = 'tegra-dc'),
        sysfs.Device(bus = 'platform', name = '54340000.vic', driver = 'tegra-vic'),
        sysfs.Device(bus = 'platform', name = '54540000.sor', driver = 'tegra-sor'),
        sysfs.Device(bus = 'platform', name = '54580000.sor', driver = 'tegra-sor'),
        sysfs.Device(bus = 'platform', name = '545c0000.dpaux', driver = 'tegra-dpaux'),
        sysfs.Device(bus = 'platform', name = '57000000.gpu', driver = 'nouveau'),
        sysfs.Device(bus = 'platform', name = '60005000.timer', driver = ''),
        sysfs.Device(bus = 'platform', name = '60007000.flow-controller', driver = 'tegra-flowctrl'),
        sysfs.Device(bus = 'platform', name = '6000d000.gpio', driver = 'tegra-gpio'),
        sysfs.Device(bus = 'platform', name = '60020000.dma', driver = 'tegra-apbdma'),
        sysfs.Device(bus = 'platform', name = '700008d4.pinmux', driver = 'tegra210-pinctrl'),
        sysfs.Device(bus = 'platform', name = '70006000.serial', driver = [ 'of_serial', 'tegra-uart' ]),
        sysfs.Device(bus = 'platform', name = '7000a000.pwm', driver = 'tegra-pwm'),
        sysfs.Device(bus = 'platform', name = '7000c500.i2c', driver = 'tegra-i2c'),
        sysfs.Device(bus = 'platform', name = '7000c700.i2c', driver = 'tegra-i2c'),
        sysfs.Device(bus = 'platform', name = '7000d000.i2c', driver = 'tegra-i2c'),
        sysfs.Device(bus = 'platform', name = '7000e000.rtc', driver = 'tegra_rtc'),
        sysfs.Device(bus = 'platform', name = '7000e400.pmc', driver = 'tegra-pmc'),
        sysfs.Device(bus = 'platform', name = '7000f800.fuse', driver = 'tegra-fuse'),
        sysfs.Device(bus = 'platform', name = '70019000.memory-controller', driver = 'tegra-mc'),
        sysfs.Device(bus = 'platform', name = '70030000.hda', driver = 'tegra-hda'),
        sysfs.Device(bus = 'platform', name = '70090000.usb', driver = 'tegra-xusb'),
        sysfs.Device(bus = 'platform', name = '7009f000.padctl', driver = 'tegra-xusb-padctl'),
        sysfs.Device(bus = 'platform', name = '700e2000.thermal-sensor', driver = 'tegra_soctherm'),
        sysfs.Device(bus = 'platform', name = '700e3000.mipi', driver = 'tegra-mipi'),
        sysfs.Device(bus = 'platform', name = 'pwm-fan' if Kernel().version >= Kernel.Version('5.19.0') else 'fan', driver = 'pwm-fan'),
        sysfs.Device(bus = 'platform', name = 'gpio-keys', driver = 'gpio-keys'),
        sysfs.Device(bus = 'platform', name = 'max77620-gpio', driver = 'max77620-gpio'),
        sysfs.Device(bus = 'platform', name = 'max77620-pinctrl', driver = 'max77620-pinctrl'),
        sysfs.Device(bus = 'platform', name = 'max77620-pmic', driver = 'max77620-pmic'),
        sysfs.Device(bus = 'platform', name = 'max77620-rtc', driver = 'max77686-rtc'),
        sysfs.Device(bus = 'platform', name = 'pmu', driver = 'armv8-pmu'),
    # Device trees in Linux v5.9 changed sdhci@... to mmc@...
    ] + [
        device for device in [
            sysfs.Device(bus = 'platform', name = '700b0000.sdhci', driver = 'sdhci-tegra'),
            sysfs.Device(bus = 'platform', name = '700b0400.sdhci', driver = 'sdhci-tegra'),
        ] if Kernel().version < Kernel.Version('5.9.0')
    ] + [
        device for device in [
            sysfs.Device(bus = 'platform', name = '700b0000.mmc', driver = 'sdhci-tegra'),
            sysfs.Device(bus = 'platform', name = '700b0400.mmc', driver = 'sdhci-tegra'),
        ] if Kernel().version >= Kernel.Version('5.9.0')
    # Linux v5.10 enabled support for ACONNECT, ADMA and AGIC
    ] + [
        device for device in [
            sysfs.Device(bus = 'platform', name = 'aconnect@702c0000', driver = 'tegra-aconnect'),
            sysfs.Device(bus = 'platform', name = '702e2000.dma-controller', driver = 'tegra-adma'),
            sysfs.Device(bus = 'platform', name = '702f9000.interrupt-controller', driver = 'gic'),
        ] if Kernel().version >= Kernel.Version('5.10.0')
    # Linux v5.12 enabled support for the Audio Processing Engine
    ] + [
        device for device in [
            sysfs.Device(bus = 'platform', name = '702d0800.ahub', driver = 'tegra210-ahub'),
            sysfs.Device(bus = 'platform', name = '702d0000.admaif', driver = 'tegra210-admaif'),
            sysfs.Device(bus = 'platform', name = '702d1200.i2s', driver = 'tegra210-i2s'),
            sysfs.Device(bus = 'platform', name = '702d1300.i2s', driver = 'tegra210-i2s'),
            sysfs.Device(bus = 'platform', name = '702d4000.dmic', driver = 'tegra210-dmic'),
            sysfs.Device(bus = 'platform', name = '702d4000.dmic', driver = 'tegra210-dmic'),
            sysfs.Device(bus = 'platform', name = '702d4100.dmic', driver = 'tegra210-dmic'),
            sysfs.Device(bus = 'platform', name = 'sound', driver = 'tegra-audio-graph-card'),
        ] if Kernel().version >= Kernel.Version('5.12.0')
    # HDA bus
    ] + [
        sysfs.Device(bus = 'hdaudio', name = 'hdaudioC0D3', driver = 'snd_hda_codec_hdmi'),
    # I2C bus
    ] + [
        sysfs.Device(bus = 'i2c', name = '0-0050', driver = 'at24'),
        sysfs.Device(bus = 'i2c', name = '0-0057', driver = 'at24'),
        sysfs.Device(bus = 'i2c', name = '1-003c', driver = 'max77620'),
        sysfs.Device(bus = 'i2c', name = '1-0068', driver = 'dummy'),
    # PCI bus
    ] + [
        sysfs.Device(bus = 'pci', name = '0000:00:02.0', driver = 'pcieport'),
        sysfs.Device(bus = 'pci', name = '0000:01:00.0', driver = 'r8169'),
    # host1x bus
    ] + [
        sysfs.Device(bus = 'host1x', name = 'drm', driver = 'drm'),
    # Linux v5.9 enabled support for the Tegra VI/CSI V4L2 driver on Jetson Nano
    ] + [
        device for device in [
            sysfs.Device(bus = 'host1x', name = 'tegra-video', driver = 'tegra-video'),
        ] if Kernel().version >= Kernel.Version('5.9.0')
    ]

    drivers = [
        sysfs.Driver('platform', 'tegra-host1x'),
    ]

    allowlist = [
        r'EINJ: ACPI disabled.',
        r'pci_bus [0-9a-fA-F]{4}:[0-9a-fA-F]{2}: \d+-byte config .* to [0-9a-fA-F]{4}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}\.\d offset 0x[0-9a-fA-F]+ may corrupt adjacent RW1C bits',
        r'pci [0-9a-fA-F]{4}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}\.[0-9a-fA-F]: nv_msi_ht_cap_quirk didn\'t locate host bridge',
        r'tegra-i2c 7000c700.i2c: deferred probe timeout, ignoring dependency',
        r'urandom_read: [0-9]+ callbacks suppressed',
    ] + [
        warning for warning in [
            r'.* sound: ASoC: no DMI vendor name!',
        ] if Kernel().version < Kernel.Version('5.13.0')
    ] + [
        warning for warning in [
            r'memfd_create\(\) without MFD_EXEC nor MFD_NOEXEC_SEAL, pid=[0-9]+ \'systemd\'',
        ] if Kernel().version >= Kernel.Version('6.3.0') and Kernel().version < Kernel.Version('6.6.0')
    ] + [
        warning for warning in [
            r'systemd\[[0-9]+\]: memfd_create\(\) called without MFD_EXEC or MFD_NOEXEC_SEAL set',
        ] if Kernel().version >= Kernel.Version('6.4.0')
    ]

    def __init__(self):
        self.soc = tegra210.SoC()
        self.eeproms = {}

        i2c = self.soc.devices['i2c3']

        self.eeproms['module'] = i2c.client(0x50)
        self.eeproms['system'] = i2c.client(0x57)
