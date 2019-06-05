#!/usr/bin/python3

import mmap, os, re, sys, time
import runner

from linux import sysfs

module = sys.modules[__name__]
module.name = 'sdmmc'

class SDMMC:
    def __init__(self, name):
        self.path = os.path.join('/dev', name)

    def __str__(self):
        return 'SDMMC(\'%s\')' % self.path

    @staticmethod
    def enumerate():
        for obj in sysfs.enumerate(subsystem = 'block', DEVTYPE = 'disk'):
            if re.match('^mmcblk\d+$', obj.name):
                if 'DEVNAME' in obj.uevent:
                    yield SDMMC(obj.uevent['DEVNAME'])

class benchmark(runner.Test):
    def __call__(self, log, *args, **kwargs):
        buf = mmap.mmap(-1, 4 * 1024 * 1024)

        for sdmmc in SDMMC.enumerate():
            log.debug('%s: ' % sdmmc.path, end = '', flush = True)

            fd = os.open(sdmmc.path, os.O_DIRECT | os.O_RDONLY)
            count = 0

            start = time.perf_counter()

            while True:
                num = os.readv(fd, [buf])
                end = time.perf_counter()

                delta = end - start
                count += num

                if delta > 3.0:
                    break

            os.close(fd)

            count = count / (1024 * 1024)

            log.cont('%.2f MiB in %.2f seconds = %.2f MiB/s' % (count, delta,
                                                                count / delta))

        buf.close()

if __name__ == '__main__':
    runner.standalone(module)
