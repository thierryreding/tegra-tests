import tegra

class SoC(tegra.SoC):
    compatible = 'nvidia,tegra186'
    name = 'NVIDIA Tegra186'

    def __init__(self):
        self.num_cpus = 6
