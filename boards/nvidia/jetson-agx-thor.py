import boards
from linux import sysfs
from tegra import tegra264

class Board(boards.Board):
    __compatible__ = 'nvidia,p4071-0000+p3834-0008'
    name = 'NVIDIA Jetson AGX Thor Developer Kit'

    devices = [
        # platform bus
        sysfs.Device(bus = 'platform', name = '8400000.dma-controller', driver = 'tegra-gpcdma'),
        sysfs.Device(bus = 'platform', name = '8800000.hsp', driver = 'tegra-hsp'),
        sysfs.Device(bus = 'platform', name = 'c4e0000.serial', driver = 'tegra-utc'),
        sysfs.Device(bus = 'platform', name = 'c5a0000.serial', driver = 'tegra-utc'),
        sysfs.Device(bus = 'platform', name = 'c6a0000.pwm', driver = 'tegra-pwm'),
        sysfs.Device(bus = 'platform', name = 'c7a2000.pinmux', driver = 'tegra264-pinctrl'),
        sysfs.Device(bus = 'platform', name = 'c800000.pmc', driver = 'tegra-pmc'),
        sysfs.Device(bus = 'platform', name = 'cf00000.gpio', driver = 'tegra186-gpio'),
        sysfs.Device(bus = 'platform', name = '8105000000.iommu', driver = 'arm-smmu-v3'),
        sysfs.Device(bus = 'platform', name = '8106000000.iommu', driver = 'arm-smmu-v3'),
        sysfs.Device(bus = 'platform', name = '8108020000.memory-controller:external-memory-controller@8800000', driver = 'tegra186-emc'),
        sysfs.Device(bus = 'platform', name = '8108020000.memory-controller', driver = 'tegra-mc'),
        sysfs.Device(bus = 'platform', name = '810c281000.pinmux', driver = 'tegra264-pinctrl'),
        sysfs.Device(bus = 'platform', name = '810c300000.gpio', driver = 'tegra186-gpio'),
        sysfs.Device(bus = 'platform', name = '8181200000.host1x', driver = 'tegra-host1x'),
        sysfs.Device(bus = 'platform', name = '8188050000.vic', driver = 'tegra-vic'),
        sysfs.Device(bus = 'platform', name = 'a8082e0000.pinmux', driver = 'tegra264-pinctrl'),
        sysfs.Device(bus = 'platform', name = 'a808300000.gpio', driver = 'tegra186-gpio'),
        sysfs.Device(bus = 'platform', name = 'a808420000.pci', driver = 'tegra264-pcie'),
        sysfs.Device(bus = 'platform', name = 'a808480000.pci', driver = 'tegra264-pcie'),
        sysfs.Device(bus = 'platform', name = 'bpmp:thermal', driver = 'tegra-bpmp-thermal'),
        sysfs.Device(bus = 'platform', name = 'pmu', driver = 'armv8-pmu'),
        sysfs.Device(bus = 'platform', name = 'psci', driver = 'psci-cpuidle-domain'),
        sysfs.Device(bus = 'platform', name = 'pwm-fan', driver = 'pwm-fan'),
    ] + [
        # PCI bus
        sysfs.Device(bus = 'pci', name = '0002:00:00.0', driver = 'pcieport'),
        sysfs.Device(bus = 'pci', name = '0002:01:00.0', driver = 'r8169'),
        sysfs.Device(bus = 'pci', name = '0005:00:00.0', driver = 'pcieport'),
        sysfs.Device(bus = 'pci', name = '0005:01:00.0', driver = 'nvme'),
    ]

    allowlist = [
        r'.*: loading out-of-tree module taints kernel.',
        r'block nvme0n1: No UUID available providing old NGUID',
    ]

    def __init__(self):
        self.soc = tegra264.SoC()
        self.eeproms = {}

        self.devices = list(self.devices)
        self.devices.extend([
            self.soc.devices['bpmp'],
            self.soc.devices['bpmp:i2c'],
        ])
