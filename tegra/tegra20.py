import tegra

class SoC(tegra.SoC):
    compatible = 'nvidia,tegra20'
    name = 'NVIDIA Tegra20'

    def __init__(self):
        self.num_cpus = 2
