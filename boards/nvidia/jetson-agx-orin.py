import boards, tegra
from linux.system import Kernel
from linux import sysfs
from tegra import tegra234

class Board(boards.Board):
    __compatible__ = 'nvidia,p3737-0000+p3701-0000'
    name = 'NVIDIA Jetson AGX Orin Developer Kit'

    devices = [
        # platform bus
        sysfs.Device(bus = 'platform', name = '2200000.gpio', driver = 'tegra186-gpio'),
        sysfs.Device(bus = 'platform', name = '2600000.dma-controller', driver = 'tegra-gpcdma'),
        sysfs.Device(bus = 'platform', name = '2900800.ahub', driver = 'tegra210-ahub'),
        sysfs.Device(bus = 'platform', name = '2901000.i2s', driver = 'tegra210-i2s'),
        sysfs.Device(bus = 'platform', name = '2901100.i2s', driver = 'tegra210-i2s'),
        sysfs.Device(bus = 'platform', name = '2901300.i2s', driver = 'tegra210-i2s'),
        sysfs.Device(bus = 'platform', name = '2901500.i2s', driver = 'tegra210-i2s'),
        sysfs.Device(bus = 'platform', name = '2902000.sfc', driver = 'tegra210-sfc'),
        sysfs.Device(bus = 'platform', name = '2902200.sfc', driver = 'tegra210-sfc'),
        sysfs.Device(bus = 'platform', name = '2902400.sfc', driver = 'tegra210-sfc'),
        sysfs.Device(bus = 'platform', name = '2902600.sfc', driver = 'tegra210-sfc'),
        sysfs.Device(bus = 'platform', name = '2903000.amx', driver = 'tegra210-amx'),
        sysfs.Device(bus = 'platform', name = '2903100.amx', driver = 'tegra210-amx'),
        sysfs.Device(bus = 'platform', name = '2903200.amx', driver = 'tegra210-amx'),
        sysfs.Device(bus = 'platform', name = '2903300.amx', driver = 'tegra210-amx'),
        sysfs.Device(bus = 'platform', name = '2903800.adx', driver = 'tegra210-adx'),
        sysfs.Device(bus = 'platform', name = '2903900.adx', driver = 'tegra210-adx'),
        sysfs.Device(bus = 'platform', name = '2903a00.adx', driver = 'tegra210-adx'),
        sysfs.Device(bus = 'platform', name = '2903b00.adx', driver = 'tegra210-adx'),
        sysfs.Device(bus = 'platform', name = '2904200.dmic', driver = 'tegra210-dmic'),
        sysfs.Device(bus = 'platform', name = '2908000.processing-engine', driver = 'tegra210-ope'),
        sysfs.Device(bus = 'platform', name = '290a000.mvc', driver = 'tegra210-mvc'),
        sysfs.Device(bus = 'platform', name = '290a200.mvc', driver = 'tegra210-mvc'),
        sysfs.Device(bus = 'platform', name = '290bb00.amixer', driver = 'tegra210_mixer'),
        sysfs.Device(bus = 'platform', name = '290f000.admaif', driver = 'tegra210-admaif'),
        sysfs.Device(bus = 'platform', name = '2910000.asrc', driver = 'tegra186-asrc'),
        sysfs.Device(bus = 'platform', name = '2930000.dma-controller', driver = 'tegra-adma'),
        sysfs.Device(bus = 'platform', name = '2a41000.interrupt-controller', driver = 'gic'),
        sysfs.Device(bus = 'platform', name = '2c00000.memory-controller/2c60000.external-memory-controller', driver = 'tegra186-emc'),
        sysfs.Device(bus = 'platform', name = '2c00000.memory-controller', driver = 'tegra-mc'),
        sysfs.Device(bus = 'platform', name = '3100000.serial', driver = 'serial-tegra'),
        sysfs.Device(bus = 'platform', name = '3460000.mmc', driver = 'sdhci-tegra'),
        sysfs.Device(bus = 'platform', name = '3510000.hda', driver = 'tegra-hda'),
        sysfs.Device(bus = 'platform', name = '3810000.fuse', driver = 'tegra-fuse'),
        sysfs.Device(bus = 'platform', name = '3c00000.hsp', driver = 'tegra-hsp'),
        sysfs.Device(bus = 'platform', name = '3e00000.phy', driver = 'tegra194-p2u'),
        sysfs.Device(bus = 'platform', name = '3e10000.phy', driver = 'tegra194-p2u'),
        sysfs.Device(bus = 'platform', name = '3e20000.phy', driver = 'tegra194-p2u'),
        sysfs.Device(bus = 'platform', name = '3e30000.phy', driver = 'tegra194-p2u'),
        sysfs.Device(bus = 'platform', name = '3e40000.phy', driver = 'tegra194-p2u'),
        sysfs.Device(bus = 'platform', name = '3e50000.phy', driver = 'tegra194-p2u'),
        sysfs.Device(bus = 'platform', name = '3e60000.phy', driver = 'tegra194-p2u'),
        sysfs.Device(bus = 'platform', name = '3e70000.phy', driver = 'tegra194-p2u'),
        sysfs.Device(bus = 'platform', name = '3e90000.phy', driver = 'tegra194-p2u'),
        sysfs.Device(bus = 'platform', name = '3ea0000.phy', driver = 'tegra194-p2u'),
        sysfs.Device(bus = 'platform', name = '3eb0000.phy', driver = 'tegra194-p2u'),
        sysfs.Device(bus = 'platform', name = '3ec0000.phy', driver = 'tegra194-p2u'),
        sysfs.Device(bus = 'platform', name = '3ed0000.phy', driver = 'tegra194-p2u'),
        sysfs.Device(bus = 'platform', name = '3ee0000.phy', driver = 'tegra194-p2u'),
        sysfs.Device(bus = 'platform', name = '3ef0000.phy', driver = 'tegra194-p2u'),
        sysfs.Device(bus = 'platform', name = '3f00000.phy', driver = 'tegra194-p2u'),
        sysfs.Device(bus = 'platform', name = '3f20000.phy', driver = 'tegra194-p2u'),
        sysfs.Device(bus = 'platform', name = '3f30000.phy', driver = 'tegra194-p2u'),
        sysfs.Device(bus = 'platform', name = '3f40000.phy', driver = 'tegra194-p2u'),
        sysfs.Device(bus = 'platform', name = '3f50000.phy', driver = 'tegra194-p2u'),
        sysfs.Device(bus = 'platform', name = '3f60000.phy', driver = 'tegra194-p2u'),
        sysfs.Device(bus = 'platform', name = '3f70000.phy', driver = 'tegra194-p2u'),
        sysfs.Device(bus = 'platform', name = '3f80000.phy', driver = 'tegra194-p2u'),
        sysfs.Device(bus = 'platform', name = '3f90000.phy', driver = 'tegra194-p2u'),
        sysfs.Device(bus = 'platform', name = '8000000.iommu', driver = 'arm-smmu'),
        sysfs.Device(bus = 'platform', name = 'b600000.sce-fabric', driver = 'tegra234-cbb'),
        sysfs.Device(bus = 'platform', name = 'be00000.rce-fabric', driver = 'tegra234-cbb'),
        sysfs.Device(bus = 'platform', name = 'c150000.hsp', driver = 'tegra-hsp'),
        sysfs.Device(bus = 'platform', name = 'c2a0000.rtc', driver = 'tegra_rtc'),
        sysfs.Device(bus = 'platform', name = 'c2f0000.gpio', driver = 'tegra186-gpio'),
        sysfs.Device(bus = 'platform', name = 'c360000.pmc', driver = 'tegra-pmc'),
        sysfs.Device(bus = 'platform', name = 'c600000.aon-fabric', driver = 'tegra234-cbb'),
        sysfs.Device(bus = 'platform', name = 'd600000.bpmp-fabric', driver = 'tegra234-cbb'),
        sysfs.Device(bus = 'platform', name = 'de00000.dce-fabric', driver = 'tegra234-cbb'),
        sysfs.Device(bus = 'platform', name = 'e000000.ccplex', driver = 'tegra194-cpufreq'),
        sysfs.Device(bus = 'platform', name = '10000000.iommu', driver = 'arm-smmu'),
        sysfs.Device(bus = 'platform', name = '12000000.iommu', driver = 'arm-smmu'),
        sysfs.Device(bus = 'platform', name = '13a00000.cbb-fabric', driver = 'tegra234-cbb'),
        sysfs.Device(bus = 'platform', name = '13e00000.host1x', driver = 'tegra-host1x'),
        sysfs.Device(bus = 'platform', name = '14100000.pcie', driver = 'tegra194-pcie'),
        sysfs.Device(bus = 'platform', name = '14160000.pcie', driver = 'tegra194-pcie'),
        sysfs.Device(bus = 'platform', name = '15340000.vic', driver = 'tegra-vic'),
        sysfs.Device(bus = 'platform', name = '40000000.sram', driver = 'sram'),
        sysfs.Device(bus = 'platform', name = 'alarmtimer.0.auto', driver = 'alarmtimer'),
        sysfs.Device(bus = 'platform', name = 'bpmp', driver = 'tegra-bpmp'),
        sysfs.Device(bus = 'platform', name = 'bpmp:i2c', driver = 'tegra-bpmp-i2c'),
        sysfs.Device(bus = 'platform', name = 'bus@0:aconnect@2900000', driver = 'tegra-aconnect'),
        sysfs.Device(bus = 'platform', name = 'gpio-keys', driver = 'gpio-keys'),
        sysfs.Device(bus = 'platform', name = 'pmu', driver = 'armv8-pmu'),
        sysfs.Device(bus = 'platform', name = 'psci', driver = 'psci-cpuidle-domain'),
        sysfs.Device(bus = 'platform', name = 'reg-dummy', driver = 'reg-dummy'),
        sysfs.Device(bus = 'platform', name = 'regulator-vdd-12v-pcie', driver = 'reg-fixed-voltage'),
        sysfs.Device(bus = 'platform', name = 'regulator-vdd-1v8-ao', driver = 'reg-fixed-voltage'),
        sysfs.Device(bus = 'platform', name = 'regulator-vdd-1v8-ls', driver = 'reg-fixed-voltage'),
        sysfs.Device(bus = 'platform', name = 'regulator-vdd-3v3-pcie', driver = 'reg-fixed-voltage'),
        sysfs.Device(bus = 'platform', name = 'serial', driver = 'tegra-tcu'),
        sysfs.Device(bus = 'platform', name = 'serial8250', driver = 'serial8250'),
        sysfs.Device(bus = 'platform', name = 'snd-soc-dummy', driver = 'snd-soc-dummy'),
        sysfs.Device(bus = 'platform', name = 'sound', driver = 'tegra-audio-graph-card'),
    # Linux v6.2 added support for the ethernet controller on Jetson AGX Xavier
    ] + [
        device for device in [
            sysfs.Device(bus = 'platform', name = '6800000.ethernet', driver = 'tegra-mgbe'),
            sysfs.Device(bus = 'mdio_bus', name = 'stmmac-0:00', driver = 'Aquantia AQR113C'),
        ] if Kernel().version >= Kernel.Version('6.2.0')
    # HDA bus
    ] + [
        sysfs.Device(bus = 'hdaudio', name = 'hdaudioC0D0', driver = 'snd_hda_codec_hdmi'),
    # host1x bus
    ] + [
        sysfs.Device(bus = 'host1x', name = 'drm', driver = 'drm'),
    # PCI bus
    ] + [
        sysfs.Device(bus = 'pci', name = '0001:00:00.0', driver = 'pcieport'),
    ]

    drivers = [
        sysfs.Driver('platform', 'tegra-host1x'),
    ]

    allowlist = [
        r'.*: loading out-of-tree module taints kernel.',
        r'EINJ: ACPI disabled.',
        r'tegra-host1x 13e00000.host1x: Context device 0 has no IOMMU!',
        r'tegra-mgbe 6800000.ethernet: Cannot get CSR clock',
        r'urandom_read: [0-9]+ callbacks suppressed',
    ] + [
        warning for warning in [
            r'tegra194-pcie [0-f]+.pcie: Phy link never came up',
        ] if Kernel().version < Kernel.Version('6.2.0')
    ] + [
        warning for warning in [
            r'memfd_create\(\) without MFD_EXEC nor MFD_NOEXEC_SEAL, pid=[0-9]+ \'systemd\'',
        ] if Kernel().version >= Kernel.Version('6.3.0') and Kernel().version < Kernel.Version('6.6.0')
    ] + [
        warning for warning in [
            r'systemd\[[0-9]+\]: memfd_create\(\) called without MFD_EXEC or MFD_NOEXEC_SEAL set',
        ] if Kernel().version >= Kernel.Version('6.4.0')
    ]

    def __init__(self):
        self.soc = tegra234.SoC()
        self.eeproms = {}
