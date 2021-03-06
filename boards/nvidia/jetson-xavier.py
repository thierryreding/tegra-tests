import boards, tegra
from linux.system import Kernel
from linux import sysfs
from tegra import tegra194

class Board(boards.Board):
    __compatible__ = 'nvidia,p2972-0000'
    name = 'NVIDIA Jetson Xavier Development Kit'

    devices = [
        # platform bus
        sysfs.Device(bus = 'platform', name = '2200000.gpio', driver = 'tegra186-gpio'),
        sysfs.Device(bus = 'platform', name = '2490000.ethernet', driver = 'dwc-eth-dwmac'),
        sysfs.Device(bus = 'platform', name = '3110000.serial', driver = [ 'of_serial', 'tegra-uart' ]),
        sysfs.Device(bus = 'platform', name = '31c0000.i2c', driver = 'tegra-i2c'),
        sysfs.Device(bus = 'platform', name = '3c00000.hsp', driver = 'tegra-hsp'),
        sysfs.Device(bus = 'platform', name = 'c150000.hsp', driver = 'tegra-hsp'),
        sysfs.Device(bus = 'platform', name = 'c340000.pwm', driver = 'tegra-pwm'),
        sysfs.Device(bus = 'platform', name = 'c360000.pmc', driver = 'tegra-pmc'),
        sysfs.Device(bus = 'platform', name = '13e00000.host1x', driver = 'tegra-host1x'),
        sysfs.Device(bus = 'platform', name = 'bpmp', driver = 'tegra-bpmp'),
        sysfs.Device(bus = 'platform', name = 'bpmp:i2c', driver = 'tegra-bpmp-i2c'),
        sysfs.Device(bus = 'platform', name = 'bpmp:thermal', driver = 'tegra-bpmp-thermal'),
        sysfs.Device(bus = 'platform', name = 'fan', driver = 'pwm-fan'),
        sysfs.Device(bus = 'platform', name = 'gpio-keys', driver = 'gpio-keys'),
    # Linux v5.5 added support for the PCIe host controllers on Jetson AGX Xavier
    ] + [
        device for device in [
            sysfs.Device(bus = 'platform', name = '14100000.pcie', driver = 'tegra194-pcie'),
            sysfs.Device(bus = 'platform', name = '14140000.pcie', driver = 'tegra194-pcie'),
            sysfs.Device(bus = 'platform', name = '14180000.pcie', driver = 'tegra194-pcie'),
            sysfs.Device(bus = 'platform', name = '141a0000.pcie', driver = 'tegra194-pcie'),
        ] if Kernel().version >= Kernel.Version('5.5.0')
    # Device trees in Linux v5.9 changed sdhci@... to mmc@...
    ] + [
        device for device in [
            sysfs.Device(bus = 'platform', name = '3400000.sdhci', driver = 'sdhci-tegra'),
            sysfs.Device(bus = 'platform', name = '3460000.sdhci', driver = 'sdhci-tegra'),
        ] if Kernel().version < Kernel.Version('5.9.0')
    ] + [
        device for device in [
            sysfs.Device(bus = 'platform', name = '3400000.mmc', driver = 'sdhci-tegra'),
            sysfs.Device(bus = 'platform', name = '3460000.mmc', driver = 'sdhci-tegra'),
        ] if Kernel().version >= Kernel.Version('5.9.0')
    # Linux v5.10 enabled the GEN_I2C1 controller that drives the bus containing ID EEPROMs
    ] + [
        device for device in [
            sysfs.Device(bus = 'platform', name = '3160000.i2c', driver = 'tegra-i2c'),
        ] if Kernel().version >= Kernel.Version('5.10.0')
    # I2C bus
    ] + [
        sysfs.Device(bus = 'i2c', name = '0-003c', driver = 'max77620'),
    # ID EEPROMs are available as of Linux v5.10
    ] + [
        device for device in [
            sysfs.Device(bus = 'i2c', name = '1-0050', driver = 'at24'),
            sysfs.Device(bus = 'i2c', name = '1-0056', driver = 'at24'),
        ] if Kernel().version >= Kernel.Version('5.10.0')
    ]

    drivers = [
        sysfs.Driver('platform', 'tegra-host1x'),
    ]

    allowlist = [
        r'OF: fdt: Reserved memory: unsupported node format, ignoring',
        r'EINJ: ACPI disabled.',
        r'cacheinfo: Unable to detect cache hierarchy for CPU 0',
        r'dwc-eth-dwmac 2490000.ethernet: Cannot get CSR clock',
        r'mmc0: Unknown controller version \(5\). You may experience problems.',
        r'mmc1: Unknown controller version \(5\). You may experience problems.',
        r'tegra-dpaux 155e0000.dpaux: 155e0000.dpaux supply vdd not found, using dummy regulator',
        r'tegra-hda 3510000.hda: azx_get_response timeout, switching to polling mode:',
        r'tegra-i2c 31c0000.i2c: deferred probe timeout, ignoring dependency',
        r'\[drm\] parse error at position 6 in video mode \'tegrafb\'',
        r'urandom_read: [0-9]+ callbacks suppressed',
    ]

    def __init__(self):
        self.soc = tegra194.SoC()
        self.eeproms = {}

        if 'i2c1' in self.soc.devices:
            i2c = self.soc.devices['i2c1']
            self.eeproms['module'] = i2c.device(0x50)
            self.eeproms['system'] = i2c.device(0x56)
