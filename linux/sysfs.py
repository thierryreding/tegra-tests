import io, os.path

mountpoint = '/sys'

def exists(path):
    return os.path.exists('%s/%s' % (mountpoint, path))

def open(path, *args, **kwargs):
    return io.open('%s/%s' % (mountpoint, path), *args, **kwargs)

class Object:
    def __init__(self, path, name):
        self.path = os.path.join(path, name)
        self.name = name

    def open(self, path, *args, **kwargs):
        path = os.path.join(mountpoint, self.path, path)

        return io.open(path, *args, **kwargs)

    @property
    def uevent(self):
        properties = {}

        for line in self.open('uevent'):
            key, value = line.strip().split('=')
            properties[key] = value

        return properties

    def __str__(self):
        return 'Object(\'%s\')' % self.path

def enumerate(subsystem = None, DEVTYPE = None):
    if subsystem:
        top = os.path.join(mountpoint, 'class', subsystem)
    else:
        top = os.path.join(mountpoint, 'devices')

    for dirpath, dirnames, filenames in os.walk(top):
        for name in dirnames:
            parts = dirpath.split(os.path.sep)
            path = os.path.join(*parts[2:])

            device = Object(path, name)

            if DEVTYPE:
                if 'DEVTYPE' in device.uevent:
                    if device.uevent['DEVTYPE'] == DEVTYPE:
                        yield device
            else:
                yield device

class Device:
    def __init__(self, bus, name, driver):
        self.bus = bus
        self.name = name
        self.driver = driver
