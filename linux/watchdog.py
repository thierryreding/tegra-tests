import ctypes
import os

from . import ioctl
from . import libc

class Watchdog():
    WDIOC_SETOPTIONS = ioctl.IOR(ord('W'), 4, 4)
    WDIOC_SETTIMEOUT = ioctl.IOWR(ord('W'), 6, 4)

    WDIOS_DISABLECARD = 0x0001
    WDIOS_ENABLECARD = 0x0002

    def __init__(self, path):
        self.fd = os.open(path, os.O_RDWR)

    def disable(self):
        options = ctypes.pointer(ctypes.c_uint(Watchdog.WDIOS_DISABLECARD))

        libc.ioctl(self.fd, Watchdog.WDIOC_SETOPTIONS, options)

    def enable(self):
        options = ctypes.pointer(ctypes.c_uint(Watchdog.WDIOS_ENABLECARD))

        libc.ioctl(self.fd, Watchdog.WDIOC_SETOPTIONS, options)

    def set_timeout(self, timeout):
        timeout = ctypes.pointer(ctypes.c_uint(timeout))

        libc.ioctl(self.fd, Watchdog.WDIOC_SETTIMEOUT, timeout)

    def __del__(self):
        options = ctypes.pointer(ctypes.c_uint(Watchdog.WDIOS_DISABLECARD))
        libc.ioctl(self.fd, Watchdog.WDIOC_SETOPTIONS, options)
        os.close(self.fd)
