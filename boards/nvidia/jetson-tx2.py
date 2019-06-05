import boards
from linux import sysfs

class Board(boards.Board):
    __compatible__ = 'nvidia,p2771-0000'
    name = 'NVIDIA Jetson TX2 Development Kit'

    devices = [
        # platform bus
        sysfs.Device('platform', '10003000.pcie',  'tegra-pcie'),
        sysfs.Device('platform', '12000000.iommu', 'arm-smmu'),
        sysfs.Device('platform', '13e00000.host1x', 'tegra-host1x'),
        sysfs.Device('platform', '15040000.dpaux', 'tegra-dpaux'),
        sysfs.Device('platform', '15200000.display', 'tegra-dc'),
        sysfs.Device('platform', '15200000.display-hub', 'tegra-display-hub'),
        sysfs.Device('platform', '15210000.display', 'tegra-dc'),
        sysfs.Device('platform', '15220000.display', 'tegra-dc'),
        sysfs.Device('platform', '15340000.vic', 'tegra-vic'),
        sysfs.Device('platform', '15580000.sor', 'tegra-sor'),
        sysfs.Device('platform', '155c0000.dpaux', 'tegra-dpaux'),
        sysfs.Device('platform', '2200000.gpio', 'tegra186-gpio'),
        sysfs.Device('platform', '2490000.ethernet', 'dwc-eth-dwmac'),
        sysfs.Device('platform', '2c00000.memory-controller', 'tegra186-mc'),
        sysfs.Device('platform', '30000000.sysram', 'sram'),
        sysfs.Device('platform', '3100000.serial', 'of_serial'),
        sysfs.Device('platform', '3160000.i2c', 'tegra-i2c'),
        sysfs.Device('platform', '3180000.i2c', 'tegra-i2c'),
        sysfs.Device('platform', '3190000.i2c', 'tegra-i2c'),
        sysfs.Device('platform', '31c0000.i2c', 'tegra-i2c'),
        sysfs.Device('platform', '31e0000.i2c', 'tegra-i2c'),
        sysfs.Device('platform', '3400000.sdhci', 'sdhci-tegra'),
        sysfs.Device('platform', '3510000.hda', 'tegra-hda'),
        sysfs.Device('platform', '3820000.fuse', 'tegra-fuse'),
        sysfs.Device('platform', '3c00000.hsp', 'tegra-hsp'),
        sysfs.Device('platform', 'c240000.i2c', 'tegra-i2c'),
        sysfs.Device('platform', 'c250000.i2c', 'tegra-i2c'),
        sysfs.Device('platform', 'c2a0000.rtc', 'tegra_rtc'),
        sysfs.Device('platform', 'c2f0000.gpio', 'tegra186-gpio'),
        sysfs.Device('platform', 'c360000.pmc', 'tegra-pmc'),
        # I2C bus
        sysfs.Device('i2c', '0-003c', 'max77620'),
        sysfs.Device('i2c', '1-0074', 'pca953x'),
        sysfs.Device('i2c', '1-0077', 'pca953x'),
    ]

    whitelist = [
        r'CPU features: SANITY CHECK: .*',
        r'CPU features: Unsupported CPU feature variation detected',
        r'EINJ: ACPI disabled.',
        r'dwc-eth-dwmac 2490000.ethernet: Cannot get CSR clock',
        r'dwc-eth-dwmac 2490000.ethernet: PTP uses main clock',
        r'urandom_read: [0-9]+ callbacks suppressed',
    ]
