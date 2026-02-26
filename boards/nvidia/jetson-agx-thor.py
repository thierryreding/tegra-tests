import boards
from linux import sysfs
from tegra import tegra264

class Board(boards.Board):
    __compatible__ = 'nvidia,p4071-0000+p3834-0008'
    name = 'NVIDIA Jetson AGX Thor Developer Kit'

    def _build_devices(self, kernel):
        yield from super()._build_devices(kernel)

        # platform bus
        yield sysfs.Device(bus = 'platform', name = '8400000.dma-controller', driver = 'tegra-gpcdma')
        yield sysfs.Device(bus = 'platform', name = '8800000.hsp', driver = 'tegra-hsp')
        yield sysfs.Device(bus = 'platform', name = 'c4e0000.serial', driver = 'tegra-utc')
        yield sysfs.Device(bus = 'platform', name = 'c5a0000.serial', driver = 'tegra-utc')
        yield sysfs.Device(bus = 'platform', name = 'c6a0000.pwm', driver = 'tegra-pwm')
        yield sysfs.Device(bus = 'platform', name = 'c7a2000.pinmux', driver = 'tegra264-pinctrl')
        yield sysfs.Device(bus = 'platform', name = 'c800000.pmc', driver = 'tegra-pmc')
        yield sysfs.Device(bus = 'platform', name = 'cf00000.gpio', driver = 'tegra186-gpio')
        yield sysfs.Device(bus = 'platform', name = '8105000000.iommu', driver = 'arm-smmu-v3')
        yield sysfs.Device(bus = 'platform', name = '8106000000.iommu', driver = 'arm-smmu-v3')
        yield sysfs.Device(bus = 'platform', name = '8108020000.memory-controller:external-memory-controller@8800000', driver = 'tegra186-emc')
        yield sysfs.Device(bus = 'platform', name = '8108020000.memory-controller', driver = 'tegra-mc')
        yield sysfs.Device(bus = 'platform', name = '810c281000.pinmux', driver = 'tegra264-pinctrl')
        yield sysfs.Device(bus = 'platform', name = '810c300000.gpio', driver = 'tegra186-gpio')
        yield sysfs.Device(bus = 'platform', name = '8181200000.host1x', driver = 'tegra-host1x')
        yield sysfs.Device(bus = 'platform', name = '8188050000.vic', driver = 'tegra-vic')
        yield sysfs.Device(bus = 'platform', name = 'a8082e0000.pinmux', driver = 'tegra264-pinctrl')
        yield sysfs.Device(bus = 'platform', name = 'a808300000.gpio', driver = 'tegra186-gpio')
        yield sysfs.Device(bus = 'platform', name = 'a808420000.pci', driver = 'tegra264-pcie')
        yield sysfs.Device(bus = 'platform', name = 'a808480000.pci', driver = 'tegra264-pcie')
        yield sysfs.Device(bus = 'platform', name = 'bpmp:thermal', driver = 'tegra-bpmp-thermal')
        yield sysfs.Device(bus = 'platform', name = 'pmu', driver = 'armv8-pmu')
        yield sysfs.Device(bus = 'platform', name = 'psci', driver = 'psci-cpuidle-domain')
        yield sysfs.Device(bus = 'platform', name = 'pwm-fan', driver = 'pwm-fan')

        yield self.soc.devices['bpmp']

        # PCI bus
        yield sysfs.Device(bus = 'pci', name = '0002:00:00.0', driver = 'pcieport')
        yield sysfs.Device(bus = 'pci', name = '0002:01:00.0', driver = 'r8169')
        yield sysfs.Device(bus = 'pci', name = '0005:00:00.0', driver = 'pcieport')
        yield sysfs.Device(bus = 'pci', name = '0005:01:00.0', driver = 'nvme')

        # I2C controllers and clients
        if kernel.version >= '7.4.0':
            i2c_bpmp = self.soc.devices['bpmp:i2c']

            yield i2c_bpmp

    def _build_allowlist(self, kernel):
        yield r'.*: loading out-of-tree module taints kernel.'
        yield r'block nvme0n1: No UUID available providing old NGUID'

    def __init__(self):
        super().__init__(tegra264.SoC(), kernel)

        self.eeproms = {}
