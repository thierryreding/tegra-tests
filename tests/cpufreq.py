#!/usr/bin/python3

import unittest

from linux import log, sysfs, system

class CPU:
    def __init__(self, num):
        self.sysfs = sysfs.Object('devices/system/cpu/cpu%u/cpufreq' % num)
        self.supported_governors = []
        self.supported_rates = []

        with self.sysfs.open('scaling_available_governors', 'r') as f:
            for line in f:
                self.supported_governors.extend(line.split())

        with self.sysfs.open('scaling_available_frequencies', 'r') as f:
            for line in f:
                self.supported_rates.extend(line.split())

    def __getattr__(self, name):
        if name == 'governor':
            with self.sysfs.open('scaling_governor') as file:
                return file.read().strip()

        if name == 'rate':
            with self.sysfs.open('scaling_cur_freq') as file:
                return file.read().strip()

        return super.__getattr__(self, name)

    def __setattr__(self, name, value):
        if name == 'governor':
            with self.sysfs.open('scaling_governor', 'w') as file:
                file.write(value)

            return

        if name == 'rate':
            with self.sysfs.open('scaling_setspeed', 'w') as file:
                file.write(value)

            with self.sysfs.open('scaling_cur_freq', 'r') as file:
                rate = file.read().strip()

            if rate != value:
                raise Exception

            return

        return super.__setattr__(self, name, value)

    def has_governor(self, name):
        return name in self.supported_governors

def cpufreq_supported():
    return sysfs.exists('devices/system/cpu/cpu0/cpufreq')

def cpufreq_has_governor(name):
    cpuset = system.CPUSet()

    for cpu in cpuset:
        cpu = CPU(cpu.num)

        if not cpu.has_governor(name):
            return False

    return True

@unittest.skipUnless(cpufreq_supported(), 'CPUfreq not supported')
class cpufreq(unittest.TestCase):
    def test_list_governors(self):
        cpuset = system.CPUSet()

        for cpu in cpuset:
            print('- CPU#%u:' % cpu.num)

            cpu = CPU(cpu.num)

            print('  - supported governors:')

            for governor in cpu.supported_governors:
                if governor == cpu.governor:
                    print('    - %s *' % governor)
                else:
                    print('    - %s' % governor)

    def test_list_rates(self):
        cpuset = system.CPUSet()

        for cpu in cpuset:
            print('- CPU#%u:' % cpu.num)
            cpu = CPU(cpu.num)

            width = max([len(x) for x in cpu.supported_rates])

            print('  - supported rates:')

            for rate in cpu.supported_rates:
                if rate == cpu.rate:
                    print('    - %*s' % (width, rate), '*')
                else:
                    print('    - %*s' % (width, rate))

    @unittest.skipUnless(cpufreq_has_governor('userspace'),
                         'userspace governor not supported')
    def test_set_rates(self):
        cpuset = system.CPUSet()

        for cpu in cpuset:
            print('- CPU#%u' % cpu.num)
            cpu = CPU(cpu.num)

            log.begin('  - switching to userspace governor')
            governor = cpu.governor

            try:
                cpu.governor = 'userspace'
            except Exception as e:
                log.end(e)
                continue
            else:
                log.end()

            for rate in cpu.supported_rates:
                log.begin('  - setting rate %s' % rate)

                try:
                    cpu.rate = rate
                except Exception as e:
                    log.end(e)
                else:
                    log.end()

            log.begin('  - restoring %s governor' % governor)

            try:
                cpu.governor = governor
            except Exception as e:
                log.end(e)
            else:
                log.end()
