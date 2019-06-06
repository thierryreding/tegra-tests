from linux import system
import tegra

class SoC(tegra.SoC):
    compatible = 'nvidia,tegra186'
    name = 'NVIDIA Tegra186'

    def __init__(self):
        self.num_cpus = 6
        self.devices = {}

        self.devices['i2c8'] = system.I2CController('platform', 'c250000.i2c')
