import boards
import tegra

class Board(boards.Board):
    __compatible__ = 'nvidia,jetson-tk1'
    name = 'NVIDIA Jetson TK1'

    def check_devices_mmc(self):
        check_device('/dev/mmcblk0') # eMMC
        check_device('/dev/mmcblk1') # MMC/SD

    def check_devices(self):
        super().check_devices()
        self.check_devices_mmc()
