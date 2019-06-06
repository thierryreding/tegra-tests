from linux import system
import tegra

class SoC(tegra.SoC):
    compatible = 'nvidia,tegra210'
    name = 'NVIDIA Tegra210'

    def __init__(self):
        self.num_cpus = 4
        self.devices = {}

        self.devices['i2c3'] = system.I2CController('platform', '7000c500.i2c')
