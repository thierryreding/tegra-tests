#!/usr/bin/python3

import os
import pyudev
import sys
import unittest
import subprocess

import linux.drm

class drm(unittest.TestCase):
    def test_list_devices(self):
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

submit_vic_path = '/root/drm/tests/tegra/submit_vic'
def submit_vic_exists():
    return os.path.exists(submit_vic_path)

@unittest.skipUnless(submit_vic_exists(), 'submit_vic DRM test not present')
class submitvic(unittest.TestCase):
    def test(self):
        subprocess.check_call(submit_vic_path, stdout = subprocess.DEVNULL,
                              stderr = subprocess.DEVNULL)
