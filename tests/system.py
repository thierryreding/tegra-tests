#!/usr/bin/python3

import sys
import runner

from linux import system

module = sys.modules[__name__]
module.name = 'system'

class suspend(runner.Test):
    def __call__(self, log, *args, **kwargs):
        rtc = system.RTC('rtc0')
        rtc.set_alarm_relative(5)

        sys = system.System()
        sys.suspend()

'''
Note that this is merely an API test, because when this test finishes running,
the watchdog object will be deleted, which in turn will disable the watchdog.
The reason for this is that the watchdog will reboot the system if successful,
at which point we have no way of determining whether or not it actually
worked from this test suite.
'''
class watchdog(runner.Test):
    def __call__(self, log, *args, **kwargs):
        watchdog = system.Watchdog('/dev/watchdog')
        watchdog.set_timeout(30)
        watchdog.enable()

tests = [
    suspend,
    watchdog,
]

if __name__ == '__main__':
    runner.standalone(module)
