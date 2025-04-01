from linux import sysfs

class Controller(sysfs.Device):
    def __init__(self, parent = None, path = None, bus = None, subsystem = None, name = None, driver = None):
        if not parent:
            if path:
                parent = sysfs.Device(path = path)
            else:
                bus = sysfs.Bus(bus)
                parent = bus.device(name)
                # need to clear the name because it is part of the parent now
                name = None

        try:
            alias = parent.uevent['OF_ALIAS_0']
            self.index = int(alias[3:])
        except FileNotFoundError:
            self.index = -1
        except KeyError:
            for child in parent:
                if child.name.startswith('i2c-'):
                    self.index = int(child.name[4:])
                    break
            else:
                raise

        super().__init__(parent = parent, path = path, bus = bus, subsystem = subsystem, name = name, driver = driver)

        if self.index >= 0:
            self.child_bus = parent.child('i2c-%u' % self.index)
        else:
            self.child_bus = None

    def client(self, address, driver = None):
        return Device(self, address, driver)

class Device(sysfs.Device):
    def __init__(self, parent, address, driver = None):
        if not parent.child_bus:
            raise sysfs.DeviceNotAvailable(parent)

        name = '%u-%04x' % (parent.index, address)
        child = parent.child_bus.child(name)

        super().__init__(parent = child, driver = driver)
        self.parent = parent
        self.address = address
