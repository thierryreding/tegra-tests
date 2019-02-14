import fnmatch
import importlib
import os.path

class Vendor:
    def __init__(self, name):
        self.name = name
        self.boards = []

    def load(self, path):
        self.boards[:]

        vendor = os.path.basename(path)

        for path in os.listdir(path):
            if fnmatch.fnmatch(path, '*.py'):

                if path == '__init__.py':
                    continue

                board = os.path.splitext(path)[0]

                name = 'boards.%s.%s' % (vendor, board)
                module = importlib.import_module(name)
                self.boards.append(module.Board)

        return self.boards

class UnsupportedBoardException(Exception):
    pass

class Board:
    def __str__(self):
        return self.name

boards = []

'''
Detect the type of board by looking at the compatible string of the device
tree's root node.
'''
def detect():
    with open('/sys/firmware/devicetree/base/compatible', 'r') as file:
        line = file.read()
        if line:
            compatible = line.split('\0')[0]

            for board in boards:
                if compatible == board.__compatible__:
                    return board()

            raise UnsupportedBoardException('Board: %s' % compatible)

        raise IOError

parent = os.path.dirname(__file__)

for directory in os.listdir(parent):
    path = os.path.join(parent, directory)

    if os.path.exists(os.path.join(path, '__init__.py')):
        name = 'boards.%s' % directory
        module = importlib.import_module(name)
        boards.extend(module.vendor.load(path))
