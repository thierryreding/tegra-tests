import tegra

class SoC(tegra.SoC):
    compatible = 'nvidia,tegra132'
    name = 'NVIDIA Tegra132'

    def __init__(self):
        self.num_cpus = 2
