from linux.system import Kernel
from linux import sysfs
import tegra

class SoC(tegra.SoC):
    compatible = 'nvidia,tegra194'
    name = 'NVIDIA Tegra194'

    def __init__(self):
        self.num_cpus = 8
        self.devices = {}

        if Kernel().version >= Kernel.Version('5.10.0'):
            self.devices['i2c1'] = sysfs.i2c.Controller('platform', '3160000.i2c')
