from linux.system import Kernel
from linux import sysfs
import tegra

class SoC(tegra.SoC):
    compatible = 'nvidia,tegra234'
    name = 'NVIDIA Tegra234'
    ID = 0x234

    def __init__(self):
        self.num_cpus = 12
        self.devices = {}

        # BPMP and subdevices
        bpmp = sysfs.Device(bus = 'platform', name = 'bpmp', driver = 'tegra-bpmp')
        i2c = sysfs.i2c.Controller(parent = bpmp.child('bpmp:i2c'), driver = 'tegra-bpmp-i2c')

        self.devices['bpmp'] = bpmp
        self.devices['bpmp:i2c'] = i2c

        # I2C controllers
        self.devices['i2c1'] = sysfs.i2c.Controller(bus = 'platform', name = '3160000.i2c', driver = 'tegra-i2c')
        self.devices['i2c2'] = sysfs.i2c.Controller(bus = 'platform', name = 'c240000.i2c', driver = 'tegra-i2c')
        self.devices['i2c3'] = sysfs.i2c.Controller(bus = 'platform', name = '3180000.i2c', driver = 'tegra-i2c')
        self.devices['i2c4'] = sysfs.i2c.Controller(bus = 'platform', name = '3190000.i2c', driver = 'tegra-i2c')
        self.devices['i2c5'] = sysfs.i2c.Controller(bus = 'platform', name = '31a0000.i2c', driver = 'tegra-i2c')
        self.devices['i2c6'] = sysfs.i2c.Controller(bus = 'platform', name = '31b0000.i2c', driver = 'tegra-i2c')
        self.devices['i2c7'] = sysfs.i2c.Controller(bus = 'platform', name = '31c0000.i2c', driver = 'tegra-i2c')
        self.devices['i2c8'] = sysfs.i2c.Controller(bus = 'platform', name = 'c250000.i2c', driver = 'tegra-i2c')
        self.devices['i2c9'] = sysfs.i2c.Controller(bus = 'platform', name = '31e0000.i2c', driver = 'tegra-i2c')
