from linux.system import Kernel
from linux import system
import tegra

class SoC(tegra.SoC):
    compatible = 'nvidia,tegra234'
    name = 'NVIDIA Tegra234'

    def __init__(self):
        self.num_cpus = 12
        self.devices = {}
