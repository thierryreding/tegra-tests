#!/usr/bin/python3

import sys
import runner

from linux import debugfs

module = sys.modules[__name__]
module.name = 'memory'

def emc_legacy(log, *args, **kwargs):
    def set_rate(rate):
        with debugfs.open('emc/rate', 'w') as f:
            f.write(rate)

        with debugfs.open('emc/rate', 'r') as f:
            rate = f.read().strip();

    supported_rates = []
    errors = 0

    with debugfs.open('emc/supported_rates') as fobj:
        for line in fobj:
            supported_rates.extend(line.split())

    width = max([len(x) for x in supported_rates])

    with debugfs.open('emc/rate') as fobj:
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

        actual = set_rate(rate)
        if actual != rate:
            log.cont('reported %s' % actual)
            errors += 1
        else:
            log.cont('done')

    log.debug('- resetting to old rate: %s...' % current, end = '')

    actual = set_rate(current)
    if actual != current:
        log.cont('reported %s' % actual)
    else:
        log.cont()

    if errors != 0:
        raise runner.Error('not all rate changes succeeded')

def emc_modern(log, *args, **kwargs):
    def get_rate():
        with debugfs.open('clk/emc/clk_rate', 'r') as fobj:
            current = int(fobj.read().strip())

        with debugfs.open('emc/min_rate', 'r') as fobj:
            min_rate = int(fobj.read().strip())

        with debugfs.open('emc/max_rate', 'r') as fobj:
            max_rate = int(fobj.read().strip())

        return current, min_rate, max_rate

    def set_rate(min_rate, max_rate):
        current, lower, upper = get_rate()

        #
        # If an attempt is made to set the minimum rate higher than the
        # currently configured maximum rate, the common clock framework will
        # return an error because the new range would be invalid.
        #
        # Fix this by updating the maximum rate before the minimum rate in
        # that case.
        #
        if min_rate > upper:
            with debugfs.open('emc/max_rate', 'w') as fobj:
                fobj.write('%u' % max_rate)

        with debugfs.open('emc/min_rate', 'w') as fobj:
            fobj.write('%u' % min_rate)

        #
        # If the new minimum rate is lower than the currently configured
        # maximum rate, it's safe to write the maximum rate second.
        #
        if min_rate <= upper:
            with debugfs.open('emc/max_rate', 'w') as fobj:
                fobj.write('%u' % max_rate)

        #
        # Read the actual clock rate from the standard debugfs files. This
        # should always be within the range given by the minimum and maximum
        # rates.
        #
        with debugfs.open('clk/emc/clk_rate', 'r') as fobj:
            rate = int(fobj.read().strip())

        return rate

    available_rates = []
    errors = 0

    with debugfs.open('emc/available_rates', 'r') as fobj:
        for line in fobj:
            rates = [int(rate) for rate in line.strip().split()]
            available_rates.extend(rates)

    width = max([len(str(x)) for x in available_rates])

    current, min_rate, max_rate = get_rate()

    log.debug('- available rates: (* = current)');

    for rate in available_rates:
        if rate == current:
            log.debug('  - %*u' % (width, rate), '*')
        else:
            log.debug('  - %*u' % (width, rate))

    log.debug('- testing:')

    for rate in available_rates:
        log.debug('  - %*u...' % (width, rate), end = '')

        actual = set_rate(rate, rate)
        if actual != rate:
            log.cont('reported %u' % actual)
            errors += 1
        else:
            log.cont('done')

    log.debug('- resetting rate: %u...' % current, end = '')

    actual = set_rate(current, current)
    if actual != current:
        log.cont('reported %u' % actual)
    else:
        log.cont('done')

    log.debug('- resetting range: %u-%u...' % (min_rate, max_rate), end = '')

    actual = set_rate(min_rate, max_rate)
    if actual != current:
        log.cont('reported %u' % actual)
    else:
        log.cont('done')

    if errors != 0:
        raise runner.Error('not all rate changes succeeded')

class emc(runner.Test):
    def __call__(self, log, *args, **kwargs):
        if debugfs.exists('emc/available_rates'):
            return emc_modern(log, *args, **kwargs)

        if debugfs.exists('emc/supported_rates'):
            return emc_legacy(log, *args, **kwargs)

        raise runner.Skip('EMC frequency scaling is not supported')

if __name__ == '__main__':
    runner.standalone(module)
