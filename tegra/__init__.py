import importlib
import os.path
import sys

class UnsupportedSoCException(Exception):
    pass

class SoC:
    compatible = 'nvidia,tegra'
    name = 'NVIDIA Tegra'

'''
Detect the type of SoC by looking at the compatible string of the device
tree's root node.
'''
def detect():
    with open('/sys/firmware/devicetree/base/compatible', 'r') as file:
        line = file.read()
        if line:
            # remove the last, empty element
            values = line.split('\0')[:-1]
            compatible = values[-1]

            for soc in socs:
                if compatible == soc.compatible:
                    return soc()

            raise UnsupportedSoCException('SoC: %s' % (compatible))

        raise IOError

#
# initialization
#
socs = []

path = os.path.dirname(__file__)
sys.path.append(path)

paths = sorted(os.listdir(path))
for path in paths:
    if not path.endswith('.py'):
        continue

    if path == '__init__.py':
        continue

    name = os.path.splitext(path)[0]
    module = importlib.import_module(name)

    socs.append(module.SoC)
