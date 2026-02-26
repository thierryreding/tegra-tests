import boards, tegra
from linux.system import Kernel
from linux import sysfs
from tegra import tegra124

class Board(boards.Board):
    __compatible__ = 'nvidia,jetson-tk1'
    name = 'NVIDIA Jetson TK1'

    def _build_devices(self, kernel):
        yield from super()._build_devices(kernel)

        # platform bus
        yield sysfs.Device(bus = 'platform', name = '1003000.pcie', driver = 'tegra-pcie')
        yield sysfs.Device(bus = 'platform', name = '50000000.host1x', driver = 'tegra-host1x')
        yield sysfs.Device(bus = 'platform', name = '54200000.dc', driver = 'tegra-dc')
        yield sysfs.Device(bus = 'platform', name = '54240000.dc', driver = 'tegra-dc')
        yield sysfs.Device(bus = 'platform', name = '54280000.hdmi', driver = 'tegra-hdmi')
        yield sysfs.Device(bus = 'platform', name = '54340000.vic', driver = 'tegra-vic')
        yield sysfs.Device(bus = 'platform', name = '60005000.timer', driver = 'tegra-wdt')
        yield sysfs.Device(bus = 'platform', name = '60007000.flow-controller', driver = 'tegra-flowctrl')
        yield sysfs.Device(bus = 'platform', name = '6000d000.gpio', driver = 'tegra-gpio')
        yield sysfs.Device(bus = 'platform', name = '60020000.dma', driver = 'tegra-apbdma')
        yield sysfs.Device(bus = 'platform', name = '70000868.pinmux', driver = 'tegra124-pinctrl')
        yield sysfs.Device(bus = 'platform', name = '70006000.serial', driver = 'serial-tegra')
        yield sysfs.Device(bus = 'platform', name = '70006040.serial', driver = 'serial-tegra')
        yield sysfs.Device(bus = 'platform', name = '70006300.serial', driver = [ 'of_serial', 'tegra-uart' ])
        yield sysfs.Device(bus = 'platform', name = '7000c000.i2c', driver = 'tegra-i2c')
        yield sysfs.Device(bus = 'platform', name = '7000c400.i2c', driver = 'tegra-i2c')
        yield sysfs.Device(bus = 'platform', name = '7000c500.i2c', driver = 'tegra-i2c')
        yield sysfs.Device(bus = 'platform', name = '7000c700.i2c', driver = 'tegra-i2c')
        yield sysfs.Device(bus = 'platform', name = '7000d000.i2c', driver = 'tegra-i2c')
        yield sysfs.Device(bus = 'platform', name = '7000d400.spi', driver = 'spi-tegra114')
        yield sysfs.Device(bus = 'platform', name = '7000da00.spi', driver = 'spi-tegra114')
        yield sysfs.Device(bus = 'platform', name = '7000e000.rtc', driver = 'tegra_rtc')
        yield sysfs.Device(bus = 'platform', name = '7000e400.pmc', driver = 'tegra-pmc')
        yield sysfs.Device(bus = 'platform', name = '7000f800.fuse', driver = 'tegra-fuse')
        yield sysfs.Device(bus = 'platform', name = '70019000.memory-controller', driver = 'tegra-mc')
        yield sysfs.Device(bus = 'platform', name = '7001b000.external-memory-controller', driver = 'tegra-emc')
        yield sysfs.Device(bus = 'platform', name = '70027000.sata', driver = 'tegra-ahci')
        yield sysfs.Device(bus = 'platform', name = '70030000.hda', driver = 'tegra-hda')
        yield sysfs.Device(bus = 'platform', name = '70090000.usb', driver = 'tegra-xusb')
        yield sysfs.Device(bus = 'platform', name = '7009f000.padctl', driver = 'tegra-xusb-padctl')
        yield sysfs.Device(bus = 'platform', name = '700e2000.thermal-sensor', driver = 'tegra_soctherm')
        yield sysfs.Device(bus = 'platform', name = '70110000.clock', driver = 'tegra124-dfll')
        yield sysfs.Device(bus = 'platform', name = '70300000.ahub', driver = 'tegra30-ahub')
        yield sysfs.Device(bus = 'platform', name = '70301100.i2s', driver = 'tegra30-i2s')
        yield sysfs.Device(bus = 'platform', name = '7d000000.usb', driver = [ 'tegra-udc', 'tegra-usb' ])
        yield sysfs.Device(bus = 'platform', name = '7d000000.usb-phy', driver = 'tegra-phy')
        yield sysfs.Device(bus = 'platform', name = '7d004000.usb', driver = [ 'tegra-ehci', 'tegra-usb' ])
        yield sysfs.Device(bus = 'platform', name = '7d004000.usb-phy', driver = 'tegra-phy')
        yield sysfs.Device(bus = 'platform', name = '7d008000.usb', driver = [ 'tegra-ehci', 'tegra-usb' ])
        yield sysfs.Device(bus = 'platform', name = '7d008000.usb-phy', driver = 'tegra-phy')
        yield sysfs.Device(bus = 'platform', name = 'as3722-pinctrl', driver = 'as3722-pinctrl')
        yield sysfs.Device(bus = 'platform', name = 'as3722-power-off', driver = 'as3722-power-off')
        yield sysfs.Device(bus = 'platform', name = 'as3722-regulator', driver = 'as3722-regulator')
        yield sysfs.Device(bus = 'platform', name = 'as3722-rtc', driver = 'as3722-rtc')
        yield sysfs.Device(bus = 'platform', name = 'ci_hdrc.0', driver = 'ci_hdrc')
        yield sysfs.Device(bus = 'platform', name = 'cpufreq-dt.0', driver = 'cpufreq-dt')
        yield sysfs.Device(bus = 'platform', name = 'cpufreq-tegra124', driver = 'cpufreq-tegra124')
        yield sysfs.Device(bus = 'platform', name = 'gpio-keys', driver = 'gpio-keys')
        yield sysfs.Device(bus = 'platform', name = 'pmu', driver = 'armv7-pmu')

        # Device trees in Linux v5.9 changed sdhci@... to mmc@...
        if kernel.version < '5.9.0':
            yield sysfs.Device(bus = 'platform', name = '700b0400.sdhci', driver = 'sdhci-tegra')
            yield sysfs.Device(bus = 'platform', name = '700b0600.sdhci', driver = 'sdhci-tegra')
        else:
            yield sysfs.Device(bus = 'platform', name = '700b0400.mmc', driver = 'sdhci-tegra')
            yield sysfs.Device(bus = 'platform', name = '700b0600.mmc', driver = 'sdhci-tegra')

        # Unified audio driver is called tegra-audio as of Linux v5.14
        if kernel.version < '5.14.0':
            yield sysfs.Device(bus = 'platform', name = 'sound', driver = 'tegra-snd-rt5640')
        else:
            yield sysfs.Device(bus = 'platform', name = 'sound', driver = 'tegra-audio')

        # HDA bus
        yield sysfs.Device(bus = 'hdaudio', name = 'hdaudioC0D3', driver = [ 'snd_hda_codec_hdmi', 'snd_hda_codec_tegrahdmi' ])

        # host1x bus
        yield sysfs.Device(bus = 'host1x', name = 'drm', driver = 'drm')

        # I2C bus
        yield sysfs.Device(bus = 'i2c', name = '0-001c', driver = 'rt5640')
        yield sysfs.Device(bus = 'i2c', name = '0-004c', driver = 'lm90')
        yield sysfs.Device(bus = 'i2c', name = '0-0056', driver = 'at24')
        yield sysfs.Device(bus = 'i2c', name = '4-0040', driver = 'as3722')

        # PCI bus
        yield sysfs.Device(bus = 'pci', name = '0000:00:02.0', driver = 'pcieport')
        yield sysfs.Device(bus = 'pci', name = '0000:01:00.0', driver = 'r8169')

        # SPI bus
        yield sysfs.Device(bus = 'spi', name = 'spi1.0', driver = 'spi-nor')

    def _build_drivers(self, kernel):
        yield from super()._build_drivers(kernel)

        yield sysfs.Driver('platform', 'tegra-host1x')

    def _build_allowlist(self, kernel):
        yield from super()._build_allowlist(kernel)

        yield r'/cpus/cpu@\d+missing clock-frequency property'
        yield r' usb\d+-\d+: usb\d+-\d+ supply vbus not found'
        yield r'.*Failed to get supply \'.*\': -517'
        yield r'\+.*: bypassed regulator has no supply!'
        yield r'\+.*: failed to get the current voltage\(-517\)'
        yield r'as3722-regulator as3722-regulator: regulator .* register failed -517'
        yield r'tegra124-dfll 70110000.clock: couldn\'t get vdd_cpu regulator'
        yield r'tegra-ahci 70027000\.sata: Failed to get regulators'
        yield r'tegra-xusb 70090000\.usb: failed to get regulators: -517'
        yield r'lm90 0-004c: 0-004c supply vcc not found, using dummy regulator'
        yield r'mmc\d+: Unknown controller version \(3\)\. You may experience problems\.'
        yield r'mmc\d+: Invalid maximum block size, assuming 512 bytes'
        yield r'tegra30-i2s 70301100\.i2s: DMA channels sourced from device 70300000\.ahub'
        yield r'as3722-regulator as3722-regulator: DMA mask not set'
        yield r'tegra-pcie 1003000\.pcie: Slot present pin change, signature: \d+'
        yield r'tegra-pcie 1003000\.pcie: link \d+ down, retrying'
        yield r'pci_bus [0-9a-fA-F]{4}:[0-9a-fA-F]{2}: \d+-byte config .* to [0-9a-fA-F]{4}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}\.\d offset 0x[0-9a-fA-F]+ may corrupt adjacent RW1C bits'
        yield r'pci [0-9a-fA-F]{4}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}\.[0-9a-fA-F]: nv_msi_ht_cap_quirk didn\'t locate host bridge'
        yield r'platform regulatory.0: Direct firmware load for regulatory.db failed with error -2'
        yield r'tegra-hdmi 54280000.hdmi: cannot set audio to 48000 Hz at 297000000 Hz pixel clock'
        yield r'urandom_read: [0-9]+ callbacks suppressed'

        if kernel.version < '5.13.0':
            yield r'.* sound: ASoC: no DMI vendor name!'

        if kernel.version >= '6.3.0' and kernel.version < '6.6.0':
            yield r'memfd_create\(\) without MFD_EXEC nor MFD_NOEXEC_SEAL, pid=[0-9]+ \'systemd\''

        if kernel.version >= '6.4.0':
            yield r'systemd\[[0-9]+\]: memfd_create\(\) called without MFD_EXEC or MFD_NOEXEC_SEAL set'

    def __init__(self, kernel = Kernel()):
        super().__init__(tegra124.SoC(), kernel)
