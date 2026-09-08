from linux import sysfs
import tegra

class SoC(tegra.SoC):
    compatible = 'nvidia,tegra264'
    name = 'NVIDIA Tegra264'
    ID = 0x264

    def __init__(self):
        self.num_cpus = 14
        self.devices = {}

        # BPMP and subdevices
        bpmp = sysfs.Device(bus = 'platform', name = 'bpmp', driver = 'tegra-bpmp')
        i2c = sysfs.i2c.Controller(parent = bpmp.child('bpmp:i2c'), driver = 'tegra-bpmp-i2c')

        self.devices['bpmp'] = bpmp
        self.devices['bpmp:i2c'] = i2c
