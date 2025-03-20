from linux import system
import tegra

class SoC(tegra.SoC):
    compatible = 'nvidia,tegra210'
    name = 'NVIDIA Tegra210'

    def __init__(self):
        self.num_cpus = 4
        self.devices = {}

        self.devices['i2c2'] = system.I2CController('platform', '7000c400.i2c')
        self.devices['i2c3'] = system.I2CController('platform', '7000c500.i2c')
        self.devices['i2c5'] = system.I2CController('platform', '7000d000.i2c')
