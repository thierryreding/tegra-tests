import tegra

class SoC(tegra.SoC):
    compatible = 'nvidia,tegra124'
    name = 'NVIDIA Tegra124'

    def __init__(self):
        self.num_cpus = 4
