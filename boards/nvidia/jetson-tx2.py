import boards

class Board(boards.Board):
    __compatible__ = 'nvidia,p2771-0000'
    name = 'NVIDIA Jetson TX2 Development Kit'

    devices = [
        # platform bus
        # I2C bus
    ]
