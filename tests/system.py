import os.path
import random
import unittest

from linux import system

class suspend(unittest.TestCase):
    def test(self, rtc = 'rtc0'):
        print('Testing suspend/resume')

        rtc = system.RTC(rtc)
        rtc.set_alarm_relative(2)

        sys = system.System()
        sys.suspend()

class cpuhotplug(unittest.TestCase):
    def test(self):
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

def watchdog_supported():
    return os.path.exists('/dev/watchdog')

@unittest.skipUnless(watchdog_supported(), 'Watchdog not supported')
class watchdog(unittest.TestCase):
    def test(self):
        print('Testing watchdog')

        with system.Watchdog('/dev/watchdog') as wdt:
            wdt.set_timeout(30)
            wdt.enable()
