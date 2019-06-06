import boards, tegra
from linux.system import Kernel
from linux import sysfs, system
from tegra import tegra186

class Board(boards.Board):
    __compatible__ = 'nvidia,p2771-0000'
    name = 'NVIDIA Jetson TX2 Development Kit'

    devices = [
        # platform bus
        sysfs.Device(bus = 'platform', name = '10003000.pcie', driver = 'tegra-pcie'),
        sysfs.Device(bus = 'platform', name = '12000000.iommu', driver = 'arm-smmu'),
        sysfs.Device(bus = 'platform', name = '13e00000.host1x', driver = 'tegra-host1x'),
        sysfs.Device(bus = 'platform', name = '15040000.dpaux', driver = 'tegra-dpaux'),
        sysfs.Device(bus = 'platform', name = '15200000.display', driver = 'tegra-dc'),
        sysfs.Device(bus = 'platform', name = '15200000.display-hub', driver = 'tegra-display-hub'),
        sysfs.Device(bus = 'platform', name = '15210000.display', driver = 'tegra-dc'),
        sysfs.Device(bus = 'platform', name = '15220000.display', driver = 'tegra-dc'),
        sysfs.Device(bus = 'platform', name = '15340000.vic', driver = 'tegra-vic'),
        sysfs.Device(bus = 'platform', name = '15580000.sor', driver = 'tegra-sor'),
        sysfs.Device(bus = 'platform', name = '155c0000.dpaux', driver = 'tegra-dpaux'),
        sysfs.Device(bus = 'platform', name = '2200000.gpio', driver = 'tegra186-gpio'),
        sysfs.Device(bus = 'platform', name = '2490000.ethernet', driver = 'dwc-eth-dwmac'),
        sysfs.Device(bus = 'platform', name = '2c00000.memory-controller', driver = 'tegra186-mc'),
        sysfs.Device(bus = 'platform', name = '3100000.serial', driver = [ 'of_serial', 'tegra-uart' ]),
        sysfs.Device(bus = 'platform', name = '3160000.i2c', driver = 'tegra-i2c'),
        sysfs.Device(bus = 'platform', name = '3180000.i2c', driver = 'tegra-i2c'),
        sysfs.Device(bus = 'platform', name = '3190000.i2c', driver = 'tegra-i2c'),
        sysfs.Device(bus = 'platform', name = '31c0000.i2c', driver = 'tegra-i2c'),
        sysfs.Device(bus = 'platform', name = '31e0000.i2c', driver = 'tegra-i2c'),
        sysfs.Device(bus = 'platform', name = '3510000.hda', driver = 'tegra-hda'),
        sysfs.Device(bus = 'platform', name = '3820000.fuse', driver = 'tegra-fuse'),
        sysfs.Device(bus = 'platform', name = '3c00000.hsp', driver = 'tegra-hsp'),
        sysfs.Device(bus = 'platform', name = 'c240000.i2c', driver = 'tegra-i2c'),
        sysfs.Device(bus = 'platform', name = 'c250000.i2c', driver = 'tegra-i2c'),
        sysfs.Device(bus = 'platform', name = 'c2a0000.rtc', driver = 'tegra_rtc'),
        sysfs.Device(bus = 'platform', name = 'c2f0000.gpio', driver = 'tegra186-gpio'),
        sysfs.Device(bus = 'platform', name = 'c360000.pmc', driver = 'tegra-pmc'),
        sysfs.Device(bus = 'platform', name = '30000000.sram', driver = 'sram'),
    # Device trees in Linux v5.9 changed sdhci@... to mmc@...
    ] + [
        device for device in [
            sysfs.Device(bus = 'platform', name = '3400000.sdhci', driver = 'sdhci-tegra'),
        ] if Kernel().version < Kernel.Version('5.9.0')
    ] + [
        device for device in [
            sysfs.Device(bus = 'platform', name = '3400000.mmc', driver = 'sdhci-tegra'),
        ] if Kernel().version >= Kernel.Version('5.9.0')
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
        r'urandom_read: [0-9]+ callbacks suppressed',
    ]

    def __init__(self):
        self.soc = tegra186.SoC()
        self.eeproms = {}

        i2c = self.soc.devices['i2c8']

        self.eeproms['module'] = i2c.device(0x50)
        self.eeproms['system'] = i2c.device(0x57)
