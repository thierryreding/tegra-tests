#!/usr/bin/python3

import os, os.path, sys
import runner

from linux import kmsg, system, util
import boards, tegra

module = sys.modules[__name__]
module.name = 'boot'

class sysinfo(runner.Test):
    def __call__(self, log, *args, **kwargs):
        log.debug('System information:')
        log.debug('-------------------')

        (opsys, hostname, release, version, machine) = os.uname()
        log.debug('OS:', opsys, release, version)
        log.debug('Hostname:', hostname)
        log.debug('Machine:', machine)
        log.debug('Board:', boards.detect())
        log.debug('SoC:', tegra.detect())

        cpus = system.CPUSet()

        log.debug('CPUs:', cpus.count())

        for cpu in cpus:
            log.debug(' ', cpu)

class devices(runner.Test):
    def __call__(self, log, *args, **kwargs):
        board = boards.detect()
        failed = False

        log.debug('board:', board.name)

        for device in board.devices:
            path = os.path.join('/sys', 'bus', device.bus, 'devices', device.name)

            log.debug('  device: %s ... ' % path, end = '', flush = True)

            if os.path.exists(path):
                log.cont('exists')
            else:
                log.cont('failed')
                failed = True
                continue

            path = os.path.join(path, 'driver')

            if os.path.exists(path):
                path = os.path.realpath(path)
                driver = os.path.basename(path)

                log.debug('    bound: %s ... ' % driver, end = '', flush = True)

                if driver != device.driver:
                    log.cont('failed')
                    failed = True
                else:
                    log.cont('done')
            else:
                log.debug('unbound')

                if device.driver:
                    failed = True

        if failed:
            raise runner.Error()

class logs(runner.Test):
    def __call__(self, log, *args, **kwargs):
        board = boards.detect()
        kernel = system.Kernel()
        count = 0

        if hasattr(board, 'whitelist'):
            whitelist = util.WhiteList(board.whitelist)
        else:
            whitelist = None

        with kmsg.open('/dev/kmsg') as dmesg:
            for entry in dmesg:
                if entry.header.facility == kmsg.LOG_KERN and \
                   entry.header.level <= kmsg.LOG_WARNING:
                    if not whitelist or entry not in whitelist:
                        log.debug(entry)
                        count += 1

        if whitelist:
            unmatched = whitelist.unmatched()

            for pattern in unmatched:
                log.debug('pattern \'%s\' had no matches' % pattern)

        if count > 0:
            andor = 'and/or' if count > 1 else 'or'
            plural = 's' if count > 1 else ''

            raise runner.Error('%u warning%s %s error%s found in the kernel log' % (count, plural, andor, plural))

if __name__ == '__main__':
    runner.standalone(module)
