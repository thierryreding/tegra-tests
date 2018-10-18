#!/usr/bin/python3

import sys
import runner

from linux import debugfs

module = sys.modules[__name__]
module.name = 'memory'

class emc(runner.Test):
    def __call__(self, log, *args, **kwargs):
        supported_rates = []
        errors = 0

        with debugfs.open('emc/supported_rates') as f:
            for line in f:
                supported_rates.extend(line.split())

        width = max([len(x) for x in supported_rates])

        with debugfs.open('emc/rate') as f:
            current = f.read().strip()

        log.debug('- supported rates: (* = current)');

        for rate in supported_rates:
            if rate == current:
                log.debug('  - %*s' % (width, rate), '*')
            else:
                log.debug('  - %*s' % (width, rate))

        log.debug('- testing:')

        for rate in supported_rates:
            log.debug('  - %*s...' % (width, rate), end = '')

            actual = self.set_rate(rate)
            if actual != rate:
                log.cont('reported %s' % actual)
                errors += 1
            else:
                log.cont('done')

        log.debug('- resetting to old rate: %s...' % current, end = '')

        actual = self.set_rate(current)
        if actual != current:
            log.cont('reported %s' % actual)
        else:
            log.cont()

        if errors != 0:
            raise runner.Error('not all rate changes succeeded')

    def set_rate(self, rate):
        with debugfs.open('emc/rate', 'w') as f:
            f.write(rate)

        with debugfs.open('emc/rate', 'r') as f:
            rate = f.read().strip();

        return rate

tests = [
    emc,
]

if __name__ == '__main__':
    runner.standalone(module)
