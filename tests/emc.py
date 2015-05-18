#!/usr/bin/python3

import os.path
import sys
import unittest

def emc_supported():
    return os.path.exists('/sys/kernel/debug/emc')

def emc_set_rate(rate):
    with open('/sys/kernel/debug/emc/rate', 'w') as f:
        f.write(rate)

    with open('/sys/kernel/debug/emc/rate', 'r') as f:
        rate = f.read().strip();

    return rate

@unittest.skipUnless(emc_supported(), 'EMC frequency scaling not supported')
class EMC(unittest.TestCase):
    def test_set_rates(self):
        supported_rates = []

        print('EMC frequency scaling:')
        print('======================')

        with open('/sys/kernel/debug/emc/supported_rates') as f:
            for line in f:
                supported_rates.extend(line.split())

        width = max([len(x) for x in supported_rates])

        with open('/sys/kernel/debug/emc/rate') as f:
            current = f.read().strip()

        print('- supported rates: (* = current)');

        for rate in supported_rates:
            if rate == current:
                print('  - %*s' % (width, rate), '*')
            else:
                print('  - %*s' % (width, rate))

        print('- testing:')

        for rate in supported_rates:
            print('  - %*s...' % (width, rate), end = '')
            sys.stdout.flush()

            actual = emc_set_rate(rate)
            if actual != rate:
                print('failed (reported %s)' % actual)
            else:
                print('done')

        print('- resetting to old rate: %s...' % current, end = '')
        sys.stdout.flush()

        actual = emc_set_rate(current)
        if actual != current:
            print('failed (reported %s)' % actual)
        else:
            print('done')

if __name__ == '__main__':
    unittest.main()
