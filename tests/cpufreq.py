#!/usr/bin/python3

import os.path
import unittest

def cpufreq_supported():
    return os.path.exists('/sys/devices/system/cpu/cpufreq')

@unittest.skipUnless(cpufreq_supported(), 'CPUfreq not supported')
class CPUfreq(unittest.TestCase):
    def test_list_governors(self):
        sysfs_cpufreq = '/sys/devices/system/cpu/cpu%u/cpufreq' % 0
        supported_governors = []

        with open('%s/scaling_available_governors' % sysfs_cpufreq, 'r') as f:
            for line in f:
                supported_governors.extend(line.split())

        with open('%s/scaling_governor' % sysfs_cpufreq) as f:
            current_governor = f.read().strip()

        print('- supported governors:')

        for governor in supported_governors:
            if governor == current_governor:
                print('  - %s *' % governor)
            else:
                print('  - %s' % governor)

    def test_list_rates(self):
        sysfs_cpufreq = '/sys/devices/system/cpu/cpu%u/cpufreq' % 0
        supported_rates = []

        with open('%s/scaling_available_frequencies' % sysfs_cpufreq, 'r') as f:
            for line in f:
                supported_rates.extend(line.split())

        width = max([len(x) for x in supported_rates])

        with open('%s/scaling_cur_freq' % sysfs_cpufreq, 'r') as f:
            current = f.read().strip()

        print('- supported rates:')

        for rate in supported_rates:
            if rate == current:
                print('  - %*s' % (width, rate), '*')
            else:
                print('  - %*s' % (width, rate))
