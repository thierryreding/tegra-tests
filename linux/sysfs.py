import io, os.path

mountpoint = '/sys'

def exists(path):
    return os.path.exists('%s/%s' % (mountpoint, path))

def open(path, *args, **kwargs):
    return io.open('%s/%s' % (mountpoint, path), *args, **kwargs)

class Object:
    def __init__(self, path):
        self.path = path

    def open(self, path, *args, **kwargs):
        return open('%s/%s' % (self.path, path), *args, **kwargs)

class Device:
    def __init__(self, bus, name, driver):
        self.bus = bus
        self.name = name
        self.driver = driver
