from linux import sysfs
import tegra

class SoC(tegra.SoC):
    compatible = 'nvidia,tegra186'
    name = 'NVIDIA Tegra186'
    ID = 0x18

    def __init__(self):
        self.num_cpus = 6
        self.devices = {}

        # BPMP and subdevices
        bpmp = sysfs.Device(bus = 'platform', name = 'bpmp', driver = 'tegra-bpmp')
        i2c = sysfs.i2c.Controller(parent = bpmp.child('bpmp:i2c'), driver = 'tegra-bpmp-i2c')
        thermal = sysfs.Device(bus = 'platform', name = 'bpmp:thermal', driver = 'tegra-bpmp-thermal')

        self.devices['bpmp'] = bpmp
        self.devices['bpmp:i2c'] = i2c
        self.devices['bpmp:thermal'] = thermal
