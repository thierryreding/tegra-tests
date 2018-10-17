import tegra

class SoC(tegra.SoC):
    compatible = 'nvidia,tegra194'
    name = 'NVIDIA Tegra194'

    def __init__(self):
        self.num_cpus = 8
