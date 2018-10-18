#!/usr/bin/python3

import os, pyudev, sys
import runner

from linux import drm

module = sys.modules[__name__]
module.name = 'drm'

class devices(runner.Test):
    def __call__(self, log, *args, **kwargs):
        context = pyudev.Context()
        devices = context.list_devices(subsystem = 'drm')

        log.debug('DRM devices:')

        for device in devices:
            if not device.device_node:
                continue

            if 'seat' not in device.tags:
                continue

            devno = device.device_number

            log.debug('  %s (%u, %u)' % (device.device_node, os.major(devno),
                                         os.minor(devno)))

            dev = drm.open(device.device_node)
            version = dev.GetVersion()
            log.debug('    Driver:', version.name)
            log.debug('      Description:', version.description)
            log.debug('      Version: %u.%u.%u (%s)' % (version.major,
                                                        version.minor,
                                                        version.patch,
                                                        version.date))

tests = [
    devices,
]

if __name__ == '__main__':
    runner.standalone(module)
