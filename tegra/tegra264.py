from linux import sysfs
import tegra

class SoC(tegra.SoC):
    compatible = 'nvidia,tegra264'
    name = 'NVIDIA Tegra264'
    ID = 0x264

    def __init__(self):
        self.num_cpus = 14
        self.devices = {}
        self.chiplets = {}

        # BPMP and subdevices
        bpmp = sysfs.Device(bus = 'platform', name = 'bpmp', driver = 'tegra-bpmp')
        i2c = sysfs.i2c.Controller(parent = bpmp.child('bpmp:i2c'), driver = 'tegra-bpmp-i2c')
        thermal = sysfs.Device(bus = 'platform', name = 'bpmp:thermal', driver = 'tegra-bpmp-thermal')

        self.devices['bpmp'] = bpmp
        self.devices['bpmp:i2c'] = i2c
        self.devices['bpmp:thermal'] = thermal

        self.chiplets['system'] = sysfs.Device(bus = 'platform', name = 'bus@0')
        self.chiplets['top'] = sysfs.Device(bus = 'platform', name = 'bus@8100000000')
        self.chiplets['vision'] = sysfs.Device(bus = 'platform', name = 'bus@8180000000')
        self.chiplets['disp-usb'] = sysfs.Device(bus = 'platform', name = 'bus@8800000000')
        self.chiplets['uphy0'] = sysfs.Device(bus = 'platform', name = 'bus@a800000000')

        top_mmio = sysfs.Device(bus = 'platform', name = 'bus@8100000000')

        # I2C controllers
        self.devices['i2c1'] = sysfs.i2c.Controller(parent = top_mmio, name = '810c640000.i2c', driver = 'tegra-i2c')
