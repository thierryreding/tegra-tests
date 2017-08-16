#!/usr/bin/python3

import os
import sys
import unittest

def has_pyudev():
    try:
        import pyudev
        return True
    except:
        return False

import linux.drm

@unittest.skipUnless(has_pyudev(), 'pyudev required')
class drm(unittest.TestCase):
    def test_list_devices(self):
        import pyudev

        context = pyudev.Context()
        devices = context.list_devices(subsystem = 'drm')

        print('DRM devices:')

        for device in devices:
            if not device.device_node:
                continue

            if 'seat' not in device.tags:
                continue

            devno = device.device_number

            print('  %s (%u, %u)' % (device.device_node, os.major(devno),
                                     os.minor(devno)))

            dev = linux.drm.open(device.device_node)
            version = dev.GetVersion()
            print('    Driver:', version.name)
            print('      Description:', version.description)
            print('      Version: %u.%u.%u (%s)' % (version.major,
                                                    version.minor,
                                                    version.patch,
                                                    version.date))
