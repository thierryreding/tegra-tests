#!/usr/bin/python3

import sys, time
import runner

from linux import sysfs

module = sys.modules[__name__]
module.name = 'kms'

class framebuffer_console(runner.Test):
    def __call__(self, log, *args, **kwargs):
        fbcon = None

        for console in sysfs.list('class/vtconsole'):
            with console.open('name', 'r') as f:
                for line in f:
                    line = line.strip()
                    if line.endswith('frame buffer device'):
                        log.debug('found:', console.path)
                        fbcon = console
                        break

            if fbcon:
                break
        else:
            raise runner.Error('framebuffer console not found')

        log.debug('framebuffer console found:', console.path)

        time.sleep(1)

        with console.open('bind', 'w') as f:
            log.debug('unbinding %s...' % console.path)
            f.write('0')

        time.sleep(1)

        with console.open('bind', 'w') as f:
            log.debug('binding %s...' % console.path)
            f.write('1')

if __name__ == '__main__':
    runner.standalone(module)
