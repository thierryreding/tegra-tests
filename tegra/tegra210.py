from linux import sysfs
import tegra

class SoC(tegra.SoC):
    compatible = 'nvidia,tegra210'
    name = 'NVIDIA Tegra210'
    ID = 0x21

    def __init__(self):
        self.num_cpus = 4
        self.devices = {}
