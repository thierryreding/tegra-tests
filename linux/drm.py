#!/usr/bin/python3

import ctypes
import os
import sys

class drmVersion(ctypes.Structure):
    _fields_ = [
        ('version_major', ctypes.c_int),
        ('version_minor', ctypes.c_int),
        ('version_patchlevel', ctypes.c_int),
        ('name_len', ctypes.c_int),
        ('name', ctypes.c_char_p),
        ('date_len', ctypes.c_int),
        ('date', ctypes.c_char_p),
        ('desc_len', ctypes.c_int),
        ('desc', ctypes.c_char_p)
    ]

drmVersionPtr = ctypes.POINTER(drmVersion)

class Version():
    def __init__(self, version):
        self.major = version.version_major
        self.minor = version.version_minor
        self.patch = version.version_patchlevel
        self.name = version.name.decode('ascii')
        self.date = version.date.decode('ascii')
        self.description = version.desc.decode('ascii')

    def __str__(self):
        return '\n'.join([
            'Version: %d.%d.%d' % (self.major, self.minor, self.patch),
            'Name: %s' % self.name,
            'Date: %s' % self.date,
            'Description: %s' % self.description
        ])

class libdrm(ctypes.CDLL):
    def __init__(self):
        ctypes.CDLL.__init__(self, 'libdrm.so.2')

        self.drmGetVersion.argstype = [ ctypes.c_int ]
        self.drmGetVersion.restype = drmVersionPtr

class DRM:
    def __init__(self, device):
        self.device = device

    def __enter__(self):
        self.libdrm = libdrm()

        if type(self.device) == str:
            self.fd = os.open(self.device, os.O_RDWR)
        elif type(self.device) == int:
            self.fd = self.device

        return self

    def __exit__(self, type, value, traceback):
        os.close(self.fd)

    def GetVersion(self):
        version = self.libdrm.drmGetVersion(self.fd)
        result = Version(version[0])
        self.libdrm.drmFreeVersion(version)
        return result

if __name__ == '__main__':
    with DRM(sys.argv[1]) as drm:
        version = drm.GetVersion()
        print(version)
