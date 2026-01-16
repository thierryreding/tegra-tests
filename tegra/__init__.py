import importlib
import os.path
import re
import sys

from linux import sysfs

class UnsupportedSoCException(Exception):
    pass

class MissingSoCIdException(Exception):
    pass

class SoC:
    compatible = 'nvidia,tegra'
    name = 'NVIDIA Tegra'

    def __str__(self):
        return self.name

    @property
    def id(self):
        for device in sysfs.enumerate():
            match = re.match(r'soc(\d+)', device.name)
            if match:
                with device.open('soc_id') as fobj:
                    content = fobj.read().strip()

                    # try SMCCC format first
                    match = re.match(r'jep106:([0-9a-fA-F]{2})([0-9a-fA-F]{2}):([0-9a-fA-F]+)', content)
                    if match:
                        soc_id = int(match.group(3), 16)
                        return soc_id

                    match = re.match(r'[0-9a-fA-F]+', content)
                    if match:
                        soc_id = int(content, 10)

                        if soc_id == 0x23:
                            with device.open('major') as major:
                                major = major.read().strip()

                            soc_id = soc_id << 4 | int(major)

                        return soc_id

        raise MissingSoCIdException('failed to find SoC ID')

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
