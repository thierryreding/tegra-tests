from linux import sysfs
import tegra

class SoC(tegra.SoC):
    compatible = 'nvidia,tegra210'
    name = 'NVIDIA Tegra210'

    def __init__(self):
        self.num_cpus = 4
        self.devices = {}

        self.devices['i2c1'] = sysfs.i2c.Controller(bus = 'platform', name = '7000c000.i2c')
        self.devices['i2c2'] = sysfs.i2c.Controller(bus = 'platform', name = '7000c400.i2c')
        self.devices['i2c3'] = sysfs.i2c.Controller(bus = 'platform', name = '7000c500.i2c')
        self.devices['i2c4'] = sysfs.i2c.Controller(bus = 'platform', name = '7000c700.i2c')
        self.devices['i2c5'] = sysfs.i2c.Controller(bus = 'platform', name = '7000d000.i2c')
        self.devices['i2c6'] = sysfs.i2c.Controller(bus = 'platform', name = '7000d100.i2c')
