from linux.system import Kernel
from linux import sysfs
import tegra

class SoC(tegra.SoC):
    compatible = 'nvidia,tegra194'
    name = 'NVIDIA Tegra194'
    ID = 0x19

    def __init__(self):
        self.num_cpus = 8
        self.devices = {}

        # BPMP and subdevices
        bpmp = sysfs.Device(bus = 'platform', name = 'bpmp', driver = 'tegra-bpmp')
        i2c = sysfs.i2c.Controller(parent = bpmp.child('bpmp:i2c'), driver = 'tegra-bpmp-i2c')
        thermal = sysfs.Device(bus = 'platform', name = 'bpmp:thermal', driver = 'tegra-bpmp-thermal')

        self.devices['bpmp'] = bpmp
        self.devices['bpmp:i2c'] = i2c
        self.devices['bpmp:thermal'] = thermal
