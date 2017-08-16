#!/usr/bin/python3

import boards
import os.path
import unittest

class sysfs(unittest.TestCase):
    def test_check(self):
        board = boards.detect()

        print('board:', board.name)

        for device in board.devices:
            path = '/sys/bus/%s/devices/%s' % (device.bus, device.name)
            print('  device:', path, '... ', end = '', flush = True)

            if os.path.exists(path):
                print('exists')
            else:
                print('failed')

            path = '%s/driver' % path

            if os.path.exists(path):
                driver = os.path.realpath(path)
                driver = os.path.basename(driver)

                print('    bound: %s ... ' % driver, end = '', flush = True)

                if driver != device.driver:
                    print('failed')
                else:
                    print('done')
            else:
                print('    unbound')
