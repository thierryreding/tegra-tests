#!/usr/bin/python3

import io, sys
import runner

from linux import system
import boards

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

class eeprom(runner.Test):
    def __call__(self, log, *args, **kwargs):
        board = boards.detect()

        if not hasattr(board, 'eeproms'):
            raise runner.Error()

        if 'module' in board.eeproms:
            device = board.eeproms['module']
            buf = io.StringIO()

            eeprom = system.EEPROM(device.sysfs)

            log.debug('module ID EEPROM:')
            eeprom.dump(output = buf)
            buf.seek(0, io.SEEK_SET)

            for line in buf:
                log.debug('  %s' % line.rstrip())

        if 'system' in board.eeproms:
            device = board.eeproms['system']
            buf = io.StringIO()

            try:
                eeprom = system.EEPROM(device.sysfs)
            except Exception as e:
                log.info('ERROR:', e)

            log.debug('system ID EEPROM:')
            eeprom.dump(output = buf)
            buf.seek(0, io.SEEK_SET)

            for line in buf:
                log.debug('  %s' % line.rstrip())

if __name__ == '__main__':
    runner.standalone(module)
