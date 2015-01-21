#!/usr/bin/python3

import io
import os
import random
import sys
import time

from linux import kmsg
from linux import system
from linux import watchdog

def check_device(path, indent = 2):
    print('%s- %s: ' % (' ' * indent, path), end = '')

    if os.access(path, os.F_OK):
        print('OK')
    else:
        print('failed')

class Tegra():
    def check_devices(self):
        print('- checking for devices:')

    def check(self):
        print('%s detected' % self.__description__)
        print('running tests:')
        self.check_devices()

    def print(self, file = sys.stdout):
        print('Board:', self.__description__, file = file)

class Tegra20(Tegra):
    __compatible__ = 'nvidia,tegra20'

class Tegra30(Tegra):
    __compatible__ = 'nvidia,tegra30'

class Tegra114(Tegra):
    __compatible__ = 'nvidia,tegra114'

class Tegra124(Tegra):
    __compatible__ = 'nvidia,tegra124'

class JetsonTK1(Tegra124):
    __compatible__ = 'nvidia,jetson-tk1'
    __description__ = 'NVIDIA Jetson TK1'

    def check_devices_mmc(self):
        check_device('/dev/mmcblk0') # eMMC
        check_device('/dev/mmcblk1') # MMC/SD

    def check_devices(self):
        super().check_devices()
        self.check_devices_mmc()

class Tegra132(Tegra):
    __compatible__ = 'nvidia,tegra132'

socs = [
        Tegra20,
        Tegra30,
        Tegra114,
        Tegra124,
        Tegra132,
    ]

boards = [
        JetsonTK1,
    ]

def test_show_info():
    print('System information:')
    print('-------------------')

    (system, hostname, release, version, machine) = os.uname()
    print('OS:', system, release, version)
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
    with io.open('/sys/firmware/devicetree/base/compatible', 'r') as file:
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

if __name__ == '__main__':
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

    else:
        test_show_info()
