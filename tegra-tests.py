#!/usr/bin/python3

import boards
import os
import sys
import tegra
import unittest

def test_show_info():
    print('System information:')
    print('-------------------')

    (opsys, hostname, release, version, machine) = os.uname()
    print('OS:', opsys, release, version)
    print('Hostname:', hostname)
    print('Machine:', machine)

    board = detect()
    board.print()

    cpus = system.CPUSet()
    cpus.print()

def test_kmsg():
    with kmsg.open('/dev/kmsg') as log:
        for entry in log:
            print(entry)

'''
Provides access to a realtime clock device in the system.
'''
class RTC:
    def __init__(self, name = 'rtc0'):
        self.alarm = '/sys/class/rtc/%s/wakealarm' % name

    '''
    Set the RTC to raise an alarm a given number of seconds from now.
    '''
    def set_alarm_relative(self, alarm):
        alarm = int(time.time()) + alarm

        with io.open(self.alarm, 'w') as rtc:
            rtc.write('%u' % alarm)

def test_suspend(rtc = 'rtc0'):
    print('Testing suspend/resume')

    rtc = RTC(rtc)
    rtc.set_alarm_relative(10)

    sys = system.System()
    sys.suspend()

def test_cpu_hotplug():
    print('Testing CPU hotplugging')

    cpus = system.CPUSet()

    for cpu in cpus:
        print('CPU#%u: mask:' % cpu.num, 1 << cpu.num)

    masks = cpus.generate_masks()

    # go through all combinations once
    for mask in masks:
        cpus.apply_mask(mask)

    # select random combinations
    for i in range(0, 100):
        mask = random.choice(masks)
        cpus.apply_mask(mask)

    # bring all CPUs online
    cpus.online()

def test_watchdog():
    print('Testing watchdog')

    wdt = watchdog.Watchdog('/dev/watchdog')
    wdt.set_timeout(30)
    wdt.enable()

class UnsupportedBoard(Exception):
    pass

'''
Detect the type of board by looking at the compatible string of the device
tree's root node.
'''
def detect():
    with open('/sys/firmware/devicetree/base/compatible', 'r') as file:
        line = file.read()
        if line:
            # remove the last, empty element
            values = line.split('\0')[:-1]

            name = values[0]
            soc = values[-1]

            for board in boards:
                if name == board.__compatible__:
                    return board()

            raise UnsupportedBoardException('SoC: %s, Board: %s' % (soc, name))

        raise IOError

def test_board():
    board = detect()
    board.check()

#def test_drm():
#    context = pyudev.Context()
#    devices = context.list_devices(subsystem = 'drm')
#
#    print('DRM devices:')
#
#    for device in devices:
#        if not device.device_node:
#            continue
#
#        if 'seat' not in device.tags:
#            continue
#
#        devno = device.device_number
#
#        print('  %s (%u, %u)' % (device.device_node, os.major(devno),
#                                 os.minor(devno)))
#
#        dev = drm.open(device.device_node)
#        version = dev.GetVersion()
#        print('    %s (%u.%u.%u, %s, %s)' % (version.name, version.major,
#                                             version.minor, version.patch,
#                                             version.date,
#                                             version.description))

class TegraTestLoader(unittest.TestLoader):
    pass

class TegraTestRunner(unittest.TextTestRunner):
    pass

if __name__ == '__main__':
    board = boards.detect()
    soc = tegra.detect()

    print('Detected:', board.name, '(%s)' % soc.name)
    print()

    if len(sys.argv) > 1:
        if sys.argv[1] == 'info':
            test_show_info()

        if sys.argv[1] == 'kmsg':
            test_kmsg()

        if sys.argv[1] == 'suspend':
            test_suspend()

        if sys.argv[1] == 'cpu-hotplug':
            test_cpu_hotplug()

        if sys.argv[1] == 'watchdog':
            test_watchdog()

        if sys.argv[1] == 'board':
            test_board()

#        if sys.argv[1] == 'drm':
#            test_drm()

        if sys.argv[1] == 'all':
            loader = TegraTestLoader()
            runner = TegraTestRunner()

            suite = loader.discover('tests', '*.py', '.')
            runner.run(suite)

    else:
        test_show_info()
