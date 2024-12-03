import boards, tegra
from linux.system import Kernel
from linux import sysfs,l4t
from tegra import tegra234

class Board(boards.Board):
    __compatible__ = 'nvidia,p3740-0002+p3701-0008'
    name = 'NVIDIA IGX Orin'

    devices = [
        sysfs.Device(bus = 'auxiliary', name = 'mlx5_core.eth.0', driver = 'mlx5_core.eth'),
        sysfs.Device(bus = 'auxiliary', name = 'mlx5_core.eth.1', driver = 'mlx5_core.eth'),
        sysfs.Device(bus = 'auxiliary', name = 'mlx5_core.rdma.0', driver = 'mlx5_ib.rdma'),
        sysfs.Device(bus = 'auxiliary', name = 'mlx5_core.rdma.1', driver = 'mlx5_ib.rdma'),
        # Device name changes after for hdaudio. Remove it from the list.
        # sysfs.Device(bus = 'hdaudio', name = 'hdaudioC2D0', driver = 'snd_hda_codec_hdmi'),
        # sysfs.Device(bus = 'hdaudio', name = 'hdaudioC3D0', driver = 'snd_hda_codec_hdmi'),
        sysfs.Device(bus = 'host1x', name = 'drm', driver = 'drm'),
        sysfs.Device(bus = 'host1x', name = 'tegra-se-host1x', driver = 'tegra-se-host1x'),
        sysfs.Device(bus = 'i2c', name = '0-0050', driver = 'at24'),
        sysfs.Device(bus = 'i2c', name = '1-0040', driver = 'ina3221'),
        sysfs.Device(bus = 'i2c', name = '1-0041', driver = 'ina3221'),
        sysfs.Device(bus = 'i2c', name = '2-002b', driver = 'lt6911uxc'),
        sysfs.Device(bus = 'i2c', name = '4-0020', driver = 'nvvrs11'),
        sysfs.Device(bus = 'i2c', name = '4-0022', driver = 'nvvrs11'),
        sysfs.Device(bus = 'i2c', name = '4-003c', driver = 'nvvrs_pseq'),
        sysfs.Device(bus = 'i2c', name = '4-004c', driver = 'lm90'),
        sysfs.Device(bus = 'i2c', name = '6-001c', driver = 'rt5640'),
        sysfs.Device(bus = 'i2c', name = '6-0028', driver = 'stusb160x'),
        sysfs.Device(bus = 'i2c', name = '6-0055', driver = 'at24'),
        sysfs.Device(bus = 'mmc', name = 'mmc0:0001', driver = 'mmcblk'),
        sysfs.Device(bus = 'pci', name = '0001:00:00.0', driver = 'pcieport'),
        sysfs.Device(bus = 'pci', name = '0001:02:01.0', driver = 'pcieport'),
        sysfs.Device(bus = 'pci', name = '0001:02:02.0', driver = 'pcieport'),
        sysfs.Device(bus = 'pci', name = '0001:02:03.0', driver = 'pcieport'),
        sysfs.Device(bus = 'pci', name = '0001:02:04.0', driver = 'pcieport'),
        sysfs.Device(bus = 'pci', name = '0001:02:05.0', driver = 'pcieport'),
        sysfs.Device(bus = 'pci', name = '0001:03:00.0', driver = 'r8168'),
        sysfs.Device(bus = 'pci', name = '0001:35:00.0', driver = 'r8168'),
        sysfs.Device(bus = 'pci', name = '0001:67:00.0', driver = 'wchpciserial'),
        # ast is blacklisted in some installations. Remove it from the list for now.
        # sysfs.Device(bus = 'pci', name = '0001:9a:00.0', driver = 'ast'),
        sysfs.Device(bus = 'pci', name = '0001:9a:02.0', driver = 'ehci-pci'),
        sysfs.Device(bus = 'pci', name = '0001:cb:00.0', driver = 'rtl88x2ce'),
        sysfs.Device(bus = 'pci', name = '0004:00:00.0', driver = 'pcieport'),
        sysfs.Device(bus = 'pci', name = '0004:01:00.0', driver = 'nvme'),
        sysfs.Device(bus = 'pci', name = '0005:00:00.0', driver = 'pcieport'),
        sysfs.Device(bus = 'pci', name = '0005:01:00.0', driver = 'pcieport'),
        sysfs.Device(bus = 'pci', name = '0005:02:00.0', driver = 'pcieport'),
        sysfs.Device(bus = 'pci', name = '0005:02:01.0', driver = 'pcieport'),
        sysfs.Device(bus = 'pci', name = '0005:02:02.0', driver = 'pcieport'),
        sysfs.Device(bus = 'pci', name = '0005:03:00.0', driver = 'mlx5_core'),
        sysfs.Device(bus = 'pci', name = '0005:03:00.1', driver = 'mlx5_core'),
        sysfs.Device(bus = 'pci', name = '0005:04:00.0', driver = 'pcieport'),
        sysfs.Device(bus = 'pci', name = '0005:05:08.0', driver = 'pcieport'),
        sysfs.Device(bus = 'pci', name = '0005:07:00.0', driver = 'pcieport'),
        sysfs.Device(bus = 'pci', name = '0005:08:00.0', driver = 'pcieport'),
        sysfs.Device(bus = 'pci', name = '0007:00:00.0', driver = 'pcieport'),
        sysfs.Device(bus = 'pci', name = '0007:01:00.0', driver = 'ahci'),
        sysfs.Device(bus = 'pci_express', name = '0001:00:00.0:pcie001', driver = 'pcie_pme'),
        sysfs.Device(bus = 'pci_express', name = '0001:00:00.0:pcie002', driver = 'aer'),
        sysfs.Device(bus = 'pci_express', name = '0001:02:01.0:pcie204', driver = 'pciehp'),
        sysfs.Device(bus = 'pci_express', name = '0001:02:02.0:pcie204', driver = 'pciehp'),
        sysfs.Device(bus = 'pci_express', name = '0001:02:03.0:pcie204', driver = 'pciehp'),
        sysfs.Device(bus = 'pci_express', name = '0001:02:04.0:pcie204', driver = 'pciehp'),
        sysfs.Device(bus = 'pci_express', name = '0001:02:05.0:pcie204', driver = 'pciehp'),
        sysfs.Device(bus = 'pci_express', name = '0004:00:00.0:pcie001', driver = 'pcie_pme'),
        sysfs.Device(bus = 'pci_express', name = '0004:00:00.0:pcie002', driver = 'aer'),
        sysfs.Device(bus = 'pci_express', name = '0005:00:00.0:pcie001', driver = 'pcie_pme'),
        sysfs.Device(bus = 'pci_express', name = '0005:00:00.0:pcie002', driver = 'aer'),
        sysfs.Device(bus = 'pci_express', name = '0005:05:08.0:pcie208', driver = 'dpc'),
        sysfs.Device(bus = 'pci_express', name = '0005:08:00.0:pcie208', driver = 'dpc'),
        sysfs.Device(bus = 'pci_express', name = '0007:00:00.0:pcie001', driver = 'pcie_pme'),
        sysfs.Device(bus = 'pci_express', name = '0007:00:00.0:pcie002', driver = 'aer'),
        sysfs.Device(bus = 'platform', name = '10000000.iommu', driver = 'arm-smmu'),
        sysfs.Device(bus = 'platform', name = '12000000.iommu', driver = 'arm-smmu'),
        sysfs.Device(bus = 'platform', name = '13a00000.cbb-fabric', driver = 'tegra234-cbb'),
        sysfs.Device(bus = 'platform', name = '13e00000.host1x', driver = 'tegra-host1x'),
        sysfs.Device(bus = 'platform', name = '13e00000.host1x:isp-thi@14b00000', driver = 'scare-pigeon'),
        sysfs.Device(bus = 'platform', name = '13e00000.host1x:nvcsi@15a00000', driver = 't194-nvcsi'),
        sysfs.Device(bus = 'platform', name = '13e00000.host1x:vi0-thi@15f00000', driver = 'scare-pigeon'),
        sysfs.Device(bus = 'platform', name = '13e00000.host1x:vi0@15c00000', driver = 'tegra194-vi5'),
        sysfs.Device(bus = 'platform', name = '13e00000.host1x:vi1-thi@14f00000', driver = 'scare-pigeon'),
        sysfs.Device(bus = 'platform', name = '13e00000.host1x:vi1@14c00000', driver = 'tegra194-vi5'),
        sysfs.Device(bus = 'platform', name = '140e0000.pcie', driver = 'tegra194-pcie'),
        sysfs.Device(bus = 'platform', name = '14100000.pcie', driver = 'tegra194-pcie'),
        sysfs.Device(bus = 'platform', name = '14160000.pcie', driver = 'tegra194-pcie'),
        sysfs.Device(bus = 'platform', name = '141a0000.pcie', driver = 'tegra194-pcie'),
        sysfs.Device(bus = 'platform', name = '141e0000.pcie', driver = 'tegra194-pcie'),
        sysfs.Device(bus = 'platform', name = '14800000.isp', driver = 'tegra194-isp5'),
        sysfs.Device(bus = 'platform', name = '15340000.vic', driver = 'tegra-vic'),
        sysfs.Device(bus = 'platform', name = '15380000.nvjpg', driver = 'tegra-nvjpg'),
        sysfs.Device(bus = 'platform', name = '15480000.nvdec', driver = 'tegra-nvdec'),
        sysfs.Device(bus = 'platform', name = '154c0000.nvenc', driver = 'tegra-nvenc'),
        sysfs.Device(bus = 'platform', name = '15500000.tsec', driver = 'tsec'),
        sysfs.Device(bus = 'platform', name = '15540000.nvjpg', driver = 'tegra-nvjpg'),
        sysfs.Device(bus = 'platform', name = '15880000.nvdla0', driver = 'nvdla'),
        sysfs.Device(bus = 'platform', name = '158c0000.nvdla1', driver = 'nvdla'),
        sysfs.Device(bus = 'platform', name = '15a50000.ofa', driver = 'tegra-ofa'),
        sysfs.Device(bus = 'platform', name = '16000000.pva0', driver = 'pva'),
        sysfs.Device(bus = 'platform', name = '16000000.pva0:pva0_niso1_ctx0', driver = 'pva_iommu_context_dev'),
        sysfs.Device(bus = 'platform', name = '16000000.pva0:pva0_niso1_ctx1', driver = 'pva_iommu_context_dev'),
        sysfs.Device(bus = 'platform', name = '16000000.pva0:pva0_niso1_ctx2', driver = 'pva_iommu_context_dev'),
        sysfs.Device(bus = 'platform', name = '16000000.pva0:pva0_niso1_ctx3', driver = 'pva_iommu_context_dev'),
        sysfs.Device(bus = 'platform', name = '16000000.pva0:pva0_niso1_ctx4', driver = 'pva_iommu_context_dev'),
        sysfs.Device(bus = 'platform', name = '16000000.pva0:pva0_niso1_ctx5', driver = 'pva_iommu_context_dev'),
        sysfs.Device(bus = 'platform', name = '16000000.pva0:pva0_niso1_ctx6', driver = 'pva_iommu_context_dev'),
        sysfs.Device(bus = 'platform', name = '16000000.pva0:pva0_niso1_ctx7', driver = 'pva_iommu_context_dev'),
        sysfs.Device(bus = 'platform', name = '2080000.timer', driver = 'tegra186-timer'),
        sysfs.Device(bus = 'platform', name = '2200000.gpio', driver = 'tegra186-gpio'),
        sysfs.Device(bus = 'platform', name = '2430000.pinmux', driver = 'tegra234-pinctrl'),
        sysfs.Device(bus = 'platform', name = '2600000.dma-controller', driver = 'tegra-gpcdma'),
        sysfs.Device(bus = 'platform', name = '2900800.ahub', driver = 'tegra210-ahub'),
        sysfs.Device(bus = 'platform', name = '2901000.i2s', driver = 'tegra210-i2s'),
        sysfs.Device(bus = 'platform', name = '2901100.i2s', driver = 'tegra210-i2s'),
        sysfs.Device(bus = 'platform', name = '2901200.i2s', driver = 'tegra210-i2s'),
        sysfs.Device(bus = 'platform', name = '2901300.i2s', driver = 'tegra210-i2s'),
        sysfs.Device(bus = 'platform', name = '2901400.i2s', driver = 'tegra210-i2s'),
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
        sysfs.Device(bus = 'platform', name = '2904000.dmic', driver = 'tegra210-dmic'),
        sysfs.Device(bus = 'platform', name = '2904100.dmic', driver = 'tegra210-dmic'),
        sysfs.Device(bus = 'platform', name = '2904200.dmic', driver = 'tegra210-dmic'),
        sysfs.Device(bus = 'platform', name = '2904300.dmic', driver = 'tegra210-dmic'),
        sysfs.Device(bus = 'platform', name = '2905000.dspk', driver = 'tegra186-dspk'),
        sysfs.Device(bus = 'platform', name = '2905100.dspk', driver = 'tegra186-dspk'),
        sysfs.Device(bus = 'platform', name = '2907000.afc', driver = 'tegra210-afc'),
        sysfs.Device(bus = 'platform', name = '2907100.afc', driver = 'tegra210-afc'),
        sysfs.Device(bus = 'platform', name = '2907200.afc', driver = 'tegra210-afc'),
        sysfs.Device(bus = 'platform', name = '2907300.afc', driver = 'tegra210-afc'),
        sysfs.Device(bus = 'platform', name = '2907400.afc', driver = 'tegra210-afc'),
        sysfs.Device(bus = 'platform', name = '2907500.afc', driver = 'tegra210-afc'),
        sysfs.Device(bus = 'platform', name = '2908000.processing-engine', driver = 'tegra210-ope'),
        sysfs.Device(bus = 'platform', name = '290a000.mvc', driver = 'tegra210-mvc'),
        sysfs.Device(bus = 'platform', name = '290a200.mvc', driver = 'tegra210-mvc'),
        sysfs.Device(bus = 'platform', name = '290bb00.amixer', driver = 'tegra210_mixer'),
        sysfs.Device(bus = 'platform', name = '290e400.arad', driver = 'tegra186-arad'),
        sysfs.Device(bus = 'platform', name = '290f000.admaif', driver = 'tegra210-admaif'),
        sysfs.Device(bus = 'platform', name = '2910000.asrc', driver = 'tegra186-asrc'),
        sysfs.Device(bus = 'platform', name = '2930000.dma-controller', driver = 'tegra-adma'),
        sysfs.Device(bus = 'platform', name = '2a41000.interrupt-controller', driver = 'gic'),
        sysfs.Device(bus = 'platform', name = '2c00000.memory-controller', driver = 'tegra-mc'),
        sysfs.Device(bus = 'platform', name = '2c10000.mc-hwpm', driver = 'tegra-mc-hwpm'),
        sysfs.Device(bus = 'platform', name = '2c60000.external-memory-controller', driver = 'tegra186-emc'),
        sysfs.Device(bus = 'platform', name = '3100000.serial', driver = 'serial-tegra'),
        sysfs.Device(bus = 'platform', name = '3110000.serial', driver = 'serial-tegra'),
        sysfs.Device(bus = 'platform', name = '3160000.i2c', driver = 'tegra-i2c'),
        sysfs.Device(bus = 'platform', name = '3180000.i2c', driver = 'tegra-i2c'),
        sysfs.Device(bus = 'platform', name = '3190000.i2c', driver = 'tegra-i2c'),
        sysfs.Device(bus = 'platform', name = '31b0000.i2c', driver = 'tegra-i2c'),
        sysfs.Device(bus = 'platform', name = '31c0000.i2c', driver = 'tegra-i2c'),
        sysfs.Device(bus = 'platform', name = '31d0000.serial', driver = 'sbsa-uart'),
        sysfs.Device(bus = 'platform', name = '31e0000.i2c', driver = 'tegra-i2c'),
        sysfs.Device(bus = 'platform', name = '3460000.mmc', driver = 'sdhci-tegra'),
        sysfs.Device(bus = 'platform', name = '3510000.hda', driver = 'tegra-hda'),
        sysfs.Device(bus = 'platform', name = '3520000.padctl', driver = 'tegra-xusb-padctl'),
        sysfs.Device(bus = 'platform', name = '3550000.usb', driver = 'tegra-xudc'),
        sysfs.Device(bus = 'platform', name = '3610000.usb', driver = 'tegra-xusb'),
        sysfs.Device(bus = 'platform', name = '3810000.fuse', driver = 'tegra-fuse'),
        sysfs.Device(bus = 'platform', name = '39c0000.tachometer', driver = 'pwm-tegra-tachometer'),
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
        sysfs.Device(bus = 'platform', name = '40000000.sram', driver = 'sram'),
        sysfs.Device(bus = 'platform', name = '8000000.iommu', driver = 'arm-smmu'),
        sysfs.Device(bus = 'platform', name = 'alarmtimer.0.auto', driver = 'alarmtimer'),
        # Device b600000.sce-fabric is not present in JP6.1
        # sysfs.Device(bus = 'platform', name = 'b600000.sce-fabric', driver = 'tegra234-cbb'),
        sysfs.Device(bus = 'platform', name = 'b950000.tegra-hsp', driver = 'tegra-hsp'),
        sysfs.Device(bus = 'platform', name = 'bc00000.rtcpu', driver = 'tegra186-cam-rtcpu'),
        sysfs.Device(bus = 'platform', name = 'be00000.rce-fabric', driver = 'tegra234-cbb'),
        sysfs.Device(bus = 'platform', name = 'bpmp', driver = 'tegra-bpmp'),
        sysfs.Device(bus = 'platform', name = 'bpmp:i2c', driver = 'tegra-bpmp-i2c'),
        sysfs.Device(bus = 'platform', name = 'bpmp:thermal', driver = 'tegra-bpmp-thermal'),
        sysfs.Device(bus = 'platform', name = 'bus@0', driver = 'simple-pm-bus'),
        sysfs.Device(bus = 'platform', name = 'bus@0:aconnect@2900000', driver = 'tegra-aconnect'),
        sysfs.Device(bus = 'platform', name = 'c150000.hsp', driver = 'tegra-hsp'),
        sysfs.Device(bus = 'platform', name = 'c240000.i2c', driver = 'tegra-i2c'),
        sysfs.Device(bus = 'platform', name = 'c250000.i2c', driver = 'tegra-i2c'),
        sysfs.Device(bus = 'platform', name = 'c2a0000.rtc', driver = 'tegra_rtc'),
        sysfs.Device(bus = 'platform', name = 'c2f0000.gpio', driver = 'tegra186-gpio'),
        sysfs.Device(bus = 'platform', name = 'c300000.pinmux', driver = 'tegra234-pinctrl'),
        sysfs.Device(bus = 'platform', name = 'c310000.mttcan', driver = 'mttcan'),
        sysfs.Device(bus = 'platform', name = 'c320000.mttcan', driver = 'mttcan'),
        sysfs.Device(bus = 'platform', name = 'c360000.pmc', driver = 'tegra-pmc'),
        sysfs.Device(bus = 'platform', name = 'c600000.aon-fabric', driver = 'tegra234-cbb'),
        sysfs.Device(bus = 'platform', name = 'cpu-throttle-alert', driver = 'thermal-trip-event'),
        sysfs.Device(bus = 'platform', name = 'cv0-throttle-alert', driver = 'thermal-trip-event'),
        sysfs.Device(bus = 'platform', name = 'cv1-throttle-alert', driver = 'thermal-trip-event'),
        sysfs.Device(bus = 'platform', name = 'cv2-throttle-alert', driver = 'thermal-trip-event'),
        sysfs.Device(bus = 'platform', name = 'd230000.actmon', driver = 'tegra-cactmon-mc-all'),
        sysfs.Device(bus = 'platform', name = 'd600000.bpmp-fabric', driver = 'tegra234-cbb'),
        sysfs.Device(bus = 'platform', name = 'd800000.dce', driver = 'tegra-dce'),
        sysfs.Device(bus = 'platform', name = 'de00000.dce-fabric', driver = 'tegra234-cbb'),
        sysfs.Device(bus = 'platform', name = 'dsu-pmu0', driver = 'arm_dsu_pmu'),
        sysfs.Device(bus = 'platform', name = 'dsu-pmu1', driver = 'arm_dsu_pmu'),
        sysfs.Device(bus = 'platform', name = 'dsu-pmu2', driver = 'arm_dsu_pmu'),
        sysfs.Device(bus = 'platform', name = 'e000000.ccplex', driver = 'tegra194-cpufreq'),
        sysfs.Device(bus = 'platform', name = 'e100000.tegra_mce', driver = 't23x-mce'),
        sysfs.Device(bus = 'platform', name = 'e2cdf0000.ramoops_carveout', driver = 'ramoops'),
        sysfs.Device(bus = 'platform', name = 'f100000.hwpm', driver = 'tegra-soc-hwpm'),
        sysfs.Device(bus = 'platform', name = 'firmware:optee', driver = 'optee'),
        sysfs.Device(bus = 'platform', name = 'gpio-keys', driver = 'gpio-keys'),
        sysfs.Device(bus = 'platform', name = 'gpu-throttle-alert', driver = 'thermal-trip-event'),
        sysfs.Device(bus = 'platform', name = 'hot-surface-alert', driver = 'thermal-trip-event'),
        sysfs.Device(bus = 'platform', name = 'kgdboc', driver = 'kgdboc'),
        sysfs.Device(bus = 'platform', name = 'nvpmodel', driver = 'nvpmodel-clk-cap'),
        sysfs.Device(bus = 'platform', name = 'nvsciipc', driver = 'nvsciipc'),
        sysfs.Device(bus = 'platform', name = 'nvvrs-pseq-rtc', driver = 'nvvrs-pseq-rtc'),
        sysfs.Device(bus = 'platform', name = 'pmu', driver = 'armv8-pmu'),
        sysfs.Device(bus = 'platform', name = 'psci', driver = 'psci-cpuidle-domain'),
        sysfs.Device(bus = 'platform', name = 'psci-cpuidle', driver = 'psci-cpuidle'),
        sysfs.Device(bus = 'platform', name = 'reg-dummy', driver = 'reg-dummy'),
        sysfs.Device(bus = 'platform', name = 'regulator-vdd-0v95-AO', driver = 'reg-fixed-voltage'),
        sysfs.Device(bus = 'platform', name = 'regulator-vdd-12v-sys', driver = 'reg-fixed-voltage'),
        sysfs.Device(bus = 'platform', name = 'regulator-vdd-1v0-sys', driver = 'reg-fixed-voltage'),
        sysfs.Device(bus = 'platform', name = 'regulator-vdd-1v05-AO', driver = 'reg-fixed-voltage'),
        sysfs.Device(bus = 'platform', name = 'regulator-vdd-1v1-sys', driver = 'reg-fixed-voltage'),
        sysfs.Device(bus = 'platform', name = 'regulator-vdd-1v8-AO', driver = 'reg-fixed-voltage'),
        sysfs.Device(bus = 'platform', name = 'regulator-vdd-1v8-ao', driver = 'reg-fixed-voltage'),
        sysfs.Device(bus = 'platform', name = 'regulator-vdd-1v8-hs', driver = 'reg-fixed-voltage'),
        sysfs.Device(bus = 'platform', name = 'regulator-vdd-1v8-ls', driver = 'reg-fixed-voltage'),
        sysfs.Device(bus = 'platform', name = 'regulator-vdd-1v8-sys', driver = 'reg-fixed-voltage'),
        sysfs.Device(bus = 'platform', name = 'regulator-vdd-2v5-sys', driver = 'reg-fixed-voltage'),
        sysfs.Device(bus = 'platform', name = 'regulator-vdd-2v8-sys', driver = 'reg-fixed-voltage'),
        sysfs.Device(bus = 'platform', name = 'regulator-vdd-3v3-AO', driver = 'reg-fixed-voltage'),
        sysfs.Device(bus = 'platform', name = 'regulator-vdd-3v3-ao', driver = 'reg-fixed-voltage'),
        sysfs.Device(bus = 'platform', name = 'regulator-vdd-3v3-dp', driver = 'reg-fixed-voltage'),
        sysfs.Device(bus = 'platform', name = 'regulator-vdd-3v3-sys', driver = 'reg-fixed-voltage'),
        sysfs.Device(bus = 'platform', name = 'regulator-vdd-3v3-wifi', driver = 'reg-fixed-voltage'),
        sysfs.Device(bus = 'platform', name = 'regulator-vdd-3v7-AO', driver = 'reg-fixed-voltage'),
        sysfs.Device(bus = 'platform', name = 'regulator-vdd-5v-sys', driver = 'reg-fixed-voltage'),
        sysfs.Device(bus = 'platform', name = 'regulator-vdd-5v0-sys', driver = 'reg-fixed-voltage'),
        sysfs.Device(bus = 'platform', name = 'serial', driver = 'tegra-tcu'),
        sysfs.Device(bus = 'platform', name = 'serial8250', driver = 'serial8250'),
        sysfs.Device(bus = 'platform', name = 'snd-soc-dummy', driver = 'snd-soc-dummy'),
        sysfs.Device(bus = 'platform', name = 'soc0-throttle-alert', driver = 'thermal-trip-event'),
        sysfs.Device(bus = 'platform', name = 'soc1-throttle-alert', driver = 'thermal-trip-event'),
        sysfs.Device(bus = 'platform', name = 'soc2-throttle-alert', driver = 'thermal-trip-event'),
        sysfs.Device(bus = 'platform', name = 'soctherm-oc-event', driver = 'tegra234-oc-event'),
        sysfs.Device(bus = 'platform', name = 'sound', driver = 'tegra-asoc:'),
        sysfs.Device(bus = 'platform', name = 'tegra-camera-platform', driver = 'tegra_camera_platform'),
        sysfs.Device(bus = 'platform', name = 'tegra-capture-vi', driver = 'tegra-camrtc-capture-vi'),
        sysfs.Device(bus = 'platform', name = 'tegra-carveouts', driver = 'tegra-carveouts'),
        sysfs.Device(bus = 'tegra-ivc-bus', name = 'bc00000.rtcpu:ivc-bus:ivccapture@4', driver = 'tegra-capture-ivc'),
        sysfs.Device(bus = 'tegra-ivc-bus', name = 'bc00000.rtcpu:ivc-bus:ivccontrol@3', driver = 'tegra-capture-ivc'),
    ] + [
        device for device in [
            sysfs.Device(bus = 'platform', name = '15820000.se', driver = 'tegra-se'),
            sysfs.Device(bus = 'platform', name = '15840000.se', driver = 'tegra-se'),
        ] if '36.3.' in l4t.Firmware().version
    ] + [
        device for device in [
            sysfs.Device(bus = 'platform', name = '15840000.crypto', driver = 'tegra-se'),
            sysfs.Device(bus = 'platform', name = '15840000.crypto', driver = 'tegra-se'),
        ] if '36.4.' in l4t.Firmware().version
    ] + [
        device for device in [
            sysfs.Device(bus = 'pci', name = '0005:09:00.1', driver = 'snd_hda_intel'),
            sysfs.Device(bus = 'pci', name = '0005:09:00.0', driver = 'nvidia'),
        ] if 'NVIDIA RTX 6000 Ada Generation' == tegra.gpu_detect() or 'NVIDIA RTX A6000 Generation' == tegra.gpu_detect()
    ] + [
        device for device in [
            sysfs.Device(bus = 'platform', name = '13800000.display', driver = 'nv_platform'),
            sysfs.Device(bus = 'platform', name = '17000000.gpu', driver = 'gk20a'),
        ] if 'Orin (nvgpu)' == tegra.gpu_detect()
    ]

    # Add devices here that are to be ignored in the devices test
    ignore_devices = [
    ]

    drivers = [
        sysfs.Driver('platform', 'tegra-host1x'),
    ]

    allowlist = [
        # err
        r'usb usb\d-port\d: Cannot enable. Maybe the USB cable is bad?',
        r'tegra-xusb 3610000.usb: IRQ wake0 not found',
        r'tegra-hsp b950000.tegra-hsp: Try increasing MBOX_TX_QUEUE_LEN',
        # warn
        r'.*: loading out-of-tree module taints kernel.',
        r'device-mapper: core: CONFIG_IMA_DISABLE_HTABLE is disabled.*',
        r'r8168  Copyright .*',
        r'mlx5_core 0005:03:00.\d: mlx5_pcie_event:\d*:\(pid \d*\): Detected insufficient power on the PCIe slot \(27W\).',
        r'mlx5_core 0005:03:00.\d: mlx5_fw_tracer_handle_traces:\d*:\(pid \d*\): FWTracer: Events were lost',
        r'usb usb\d-port\d: config error',
        r'using random (host|self) ethernet address',
        r'pstore: ignoring unexpected backend \'efi\'',
        r'tegra-ivc-bus bc00000.rtcpu:ivc-bus:.*: ivc channel driver missing',
        r'SPI driver altr_a10sr has no spi_device_id for altr,a10sr',
        r'\(NULL device \*\): fops function table already registered',
        r'rtl8822ce_interrupt: \d* callbacks suppressed',
        r'kauditd_printk_skb: \d* callbacks suppressed',
        r'NVRM: loading NVIDIA UNIX Open Kernel Module for aarch64 .*',
    ]

    # Add additional dmesg warn, err here that are to be ignored in the logs test
    additional_allowlist = [
    ]

    def __init__(self):
        self.soc = tegra234.SoC()
        self.eeproms = {}

        for x in self.ignore_devices:
            self.devices.remove(x)

        self.allowlist = self.allowlist + self.additional_allowlist

