#!/usr/bin/python3

import unittest

from linux import debugfs, log

def emc_supported():
    return debugfs.exists('emc')

def emc_set_rate(rate):
    with debugfs.open('emc/rate', 'w') as f:
        f.write(rate)

    with debugfs.open('emc/rate', 'r') as f:
        rate = f.read().strip();

    return rate

@unittest.skipUnless(emc_supported(), 'EMC frequency scaling not supported')
class emc(unittest.TestCase):
    def test_set_rates(self):
        supported_rates = []
        errors = 0

        print('EMC frequency scaling:')
        print('======================')

        with debugfs.open('emc/supported_rates') as f:
            for line in f:
                supported_rates.extend(line.split())

        width = max([len(x) for x in supported_rates])

        with debugfs.open('emc/rate') as f:
            current = f.read().strip()

        print('- supported rates: (* = current)');

        for rate in supported_rates:
            if rate == current:
                print('  - %*s' % (width, rate), '*')
            else:
                print('  - %*s' % (width, rate))

        print('- testing:')

        for rate in supported_rates:
            log.begin('  - %*s...' % (width, rate))

            actual = emc_set_rate(rate)
            if actual != rate:
                log.end('reported %s' % actual)
                errors += 1
            else:
                log.end()

        log.begin('- resetting to old rate: %s...' % current)

        actual = emc_set_rate(current)
        if actual != current:
            log.end('reported %s' % actual)
        else:
            log.end()

        self.longMessage = False
        self.assertEqual(errors, 0, 'not all rate changes succeeded')
