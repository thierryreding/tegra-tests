import boards
from linux.system import Kernel
from linux import sysfs

class Board(boards.Board):
    __compatible__ = 'nvidia,jetson-tk1'
    name = 'NVIDIA Jetson TK1'

    devices = [
        # platform bus
        sysfs.Device(bus = 'platform', name = '1003000.pcie', driver = 'tegra-pcie'),
        sysfs.Device(bus = 'platform', name = '50000000.host1x', driver = 'tegra-host1x'),
        sysfs.Device(bus = 'platform', name = '54200000.dc', driver = 'tegra-dc'),
        sysfs.Device(bus = 'platform', name = '54240000.dc', driver = 'tegra-dc'),
        sysfs.Device(bus = 'platform', name = '54280000.hdmi', driver = 'tegra-hdmi'),
        sysfs.Device(bus = 'platform', name = '54340000.vic', driver = 'tegra-vic'),
        sysfs.Device(bus = 'platform', name = '60005000.timer', driver = 'tegra-wdt'),
        sysfs.Device(bus = 'platform', name = '60007000.flow-controller', driver = 'tegra-flowctrl'),
        sysfs.Device(bus = 'platform', name = '6000d000.gpio', driver = 'tegra-gpio'),
        sysfs.Device(bus = 'platform', name = '60020000.dma', driver = 'tegra-apbdma'),
        sysfs.Device(bus = 'platform', name = '70000868.pinmux', driver = 'tegra124-pinctrl'),
        sysfs.Device(bus = 'platform', name = '70006000.serial', driver = 'serial-tegra'),
        sysfs.Device(bus = 'platform', name = '70006040.serial', driver = 'serial-tegra'),
        sysfs.Device(bus = 'platform', name = '70006300.serial', driver = [ 'of_serial', 'tegra-uart' ]),
        sysfs.Device(bus = 'platform', name = '7000c000.i2c', driver = 'tegra-i2c'),
        sysfs.Device(bus = 'platform', name = '7000c400.i2c', driver = 'tegra-i2c'),
        sysfs.Device(bus = 'platform', name = '7000c500.i2c', driver = 'tegra-i2c'),
        sysfs.Device(bus = 'platform', name = '7000c700.i2c', driver = 'tegra-i2c'),
        sysfs.Device(bus = 'platform', name = '7000d000.i2c', driver = 'tegra-i2c'),
        sysfs.Device(bus = 'platform', name = '7000d400.spi', driver = 'spi-tegra114'),
        sysfs.Device(bus = 'platform', name = '7000da00.spi', driver = 'spi-tegra114'),
        sysfs.Device(bus = 'platform', name = '7000e000.rtc', driver = 'tegra_rtc'),
        sysfs.Device(bus = 'platform', name = '7000e400.pmc', driver = 'tegra-pmc'),
        sysfs.Device(bus = 'platform', name = '7000f800.fuse', driver = 'tegra-fuse'),
        sysfs.Device(bus = 'platform', name = '70019000.memory-controller', driver = 'tegra-mc'),
        sysfs.Device(bus = 'platform', name = '7001b000.external-memory-controller', driver = 'tegra-emc'),
        sysfs.Device(bus = 'platform', name = '70027000.sata', driver = 'tegra-ahci'),
        sysfs.Device(bus = 'platform', name = '70030000.hda', driver = 'tegra-hda'),
        sysfs.Device(bus = 'platform', name = '70090000.usb', driver = 'tegra-xusb'),
        sysfs.Device(bus = 'platform', name = '7009f000.padctl', driver = 'tegra-xusb-padctl'),
        sysfs.Device(bus = 'platform', name = '700e2000.thermal-sensor', driver = 'tegra_soctherm'),
        sysfs.Device(bus = 'platform', name = '70110000.clock', driver = 'tegra124-dfll'),
        sysfs.Device(bus = 'platform', name = '70300000.ahub', driver = 'tegra30-ahub'),
        sysfs.Device(bus = 'platform', name = '70301100.i2s', driver = 'tegra30-i2s'),
        sysfs.Device(bus = 'platform', name = '7d000000.usb', driver = [ 'tegra-udc', 'tegra-usb' ]),
        sysfs.Device(bus = 'platform', name = '7d000000.usb-phy', driver = 'tegra-phy'),
        sysfs.Device(bus = 'platform', name = '7d004000.usb', driver = [ 'tegra-ehci', 'tegra-usb' ]),
        sysfs.Device(bus = 'platform', name = '7d004000.usb-phy', driver = 'tegra-phy'),
        sysfs.Device(bus = 'platform', name = '7d008000.usb', driver = [ 'tegra-ehci', 'tegra-usb' ]),
        sysfs.Device(bus = 'platform', name = '7d008000.usb-phy', driver = 'tegra-phy'),
        sysfs.Device(bus = 'platform', name = 'as3722-pinctrl', driver = 'as3722-pinctrl'),
        sysfs.Device(bus = 'platform', name = 'as3722-power-off', driver = 'as3722-power-off'),
        sysfs.Device(bus = 'platform', name = 'as3722-regulator', driver = 'as3722-regulator'),
        sysfs.Device(bus = 'platform', name = 'as3722-rtc', driver = 'as3722-rtc'),
        sysfs.Device(bus = 'platform', name = 'ci_hdrc.0', driver = 'ci_hdrc'),
        sysfs.Device(bus = 'platform', name = 'cpufreq-dt.0', driver = 'cpufreq-dt'),
        sysfs.Device(bus = 'platform', name = 'cpufreq-tegra124', driver = 'cpufreq-tegra124'),
        sysfs.Device(bus = 'platform', name = 'gpio-keys', driver = 'gpio-keys'),
        sysfs.Device(bus = 'platform', name = 'pmu', driver = 'armv7-pmu'),
    # Device trees in Linux v5.9 changed sdhci@... to mmc@...
    ] + [
        device for device in [
            sysfs.Device(bus = 'platform', name = '700b0400.sdhci', driver = 'sdhci-tegra'),
            sysfs.Device(bus = 'platform', name = '700b0600.sdhci', driver = 'sdhci-tegra'),
        ] if Kernel().version < Kernel.Version('5.9.0')
    ] + [
        device for device in [
            sysfs.Device(bus = 'platform', name = '700b0400.mmc', driver = 'sdhci-tegra'),
            sysfs.Device(bus = 'platform', name = '700b0600.mmc', driver = 'sdhci-tegra'),
        ] if Kernel().version < Kernel.Version('5.9.0')
    # Unified audio driver is called tegra-audio as of Linux v5.14
    ] + [
        device for device in [
            sysfs.Device(bus = 'platform', name = 'sound', driver = 'tegra-snd-rt5640'),
        ] if Kernel().version < Kernel.Version('5.14.0')
    ] + [
        device for device in [
            sysfs.Device(bus = 'platform', name = 'sound', driver = 'tegra-audio'),
        ] if Kernel().version >= Kernel.Version('5.14.0')
    # HDA bus
    ] + [
        sysfs.Device(bus = 'hdaudio', name = 'hdaudioC0D3', driver = 'snd_hda_codec_hdmi'),
    # host1x bus
    ] + [
        sysfs.Device(bus = 'host1x', name = 'drm', driver = 'drm'),
    # I2C bus
    ] + [
        sysfs.Device(bus = 'i2c', name = '0-001c', driver = 'rt5640'),
        sysfs.Device(bus = 'i2c', name = '0-004c', driver = 'lm90'),
        sysfs.Device(bus = 'i2c', name = '0-0056', driver = 'at24'),
        sysfs.Device(bus = 'i2c', name = '4-0040', driver = 'as3722'),
    # PCI bus
    ] + [
        sysfs.Device(bus = 'pci', name = '0000:00:02.0', driver = 'pcieport'),
        sysfs.Device(bus = 'pci', name = '0000:01:00.0', driver = 'r8169'),
    # SPI bus
    ] + [
        sysfs.Device(bus = 'spi', name = 'spi1.0', driver = 'spi-nor'),
    ]

    drivers = [
        sysfs.Driver('platform', 'tegra-host1x'),
    ]

    allowlist = [
        r'/cpus/cpu@\d+missing clock-frequency property',
        r' usb\d+-\d+: usb\d+-\d+ supply vbus not found',
        r'.*Failed to get supply \'.*\': -517',
        r'\+.*: bypassed regulator has no supply!',
        r'\+.*: failed to get the current voltage\(-517\)',
        r'as3722-regulator as3722-regulator: regulator .* register failed -517',
        r'tegra124-dfll 70110000.clock: couldn\'t get vdd_cpu regulator',
        r'tegra-ahci 70027000\.sata: Failed to get regulators',
        r'tegra-xusb 70090000\.usb: failed to get regulators: -517',
        r'lm90 0-004c: 0-004c supply vcc not found, using dummy regulator',
        r'mmc\d+: Unknown controller version \(3\)\. You may experience problems\.',
        r'mmc\d+: Invalid maximum block size, assuming 512 bytes',
        r'tegra30-i2s 70301100\.i2s: DMA channels sourced from device 70300000\.ahub',
        r'as3722-regulator as3722-regulator: DMA mask not set',
        r'tegra-pcie 1003000\.pcie: Slot present pin change, signature: \d+',
        r'tegra-pcie 1003000\.pcie: link \d+ down, retrying',
        r'pci_bus [0-9a-fA-F]{4}:[0-9a-fA-F]{2}: \d+-byte config .* to [0-9a-fA-F]{4}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}\.\d offset 0x[0-9a-fA-F]+ may corrupt adjacent RW1C bits',
        r'pci [0-9a-fA-F]{4}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}\.[0-9a-fA-F]: nv_msi_ht_cap_quirk didn\'t locate host bridge',
        r'platform regulatory.0: Direct firmware load for regulatory.db failed with error -2',
        r'tegra-hdmi 54280000.hdmi: cannot set audio to 48000 Hz at 297000000 Hz pixel clock',
        r'urandom_read: [0-9]+ callbacks suppressed',
    ] + [
        warning for warning in [
            r'.* sound: ASoC: no DMI vendor name!',
        ] if Kernel().version < Kernel.Version('5.13.0')
    ]
