#!/usr/bin/python3

import random, sys
import runner

module = sys.modules[__name__]
module.name = 'cpu'

class hotplug(runner.Test):
    def __call__(self, log, *args, **kwargs):
        from linux import system

        cpus = system.CPUSet()

        for cpu in cpus:
            log.debug('CPU#%u: mask:' % cpu.num, 1 << cpu.num)

        masks = cpus.generate_masks()

        # go through all combinations once
        for mask in masks:
            log.debug('applying mask %#x' % mask)
            cpus.apply_mask(mask)

        # select random combinations
        for i in range(0, 100):
            mask = random.choice(masks)
            log.debug('applying mask %#x' % mask)
            cpus.apply_mask(mask)

        # bring all CPUs online
        cpus.online()

class cpufreq(runner.Test):
    class CPU:
        def __init__(self, num):
            from linux import sysfs

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

    def __call__(self, log, *args, **kwargs):
        from linux import sysfs, system

        cpuset = system.CPUSet()

        # output supported governors and frequencies
        for cpu in cpuset:
            log.debug('- CPU#%u:' % cpu.num)

            cpu = cpufreq.CPU(cpu.num)

            log.debug('  - supported governors:')

            for governor in cpu.supported_governors:
                if governor == cpu.governor:
                    log.debug('    - %s *' % governor)
                else:
                    log.debug('    - %s' % governor)

            width = max([len(x) for x in cpu.supported_rates])

            log.debug('  - supported rates:')

            for rate in cpu.supported_rates:
                if rate == cpu.rate:
                    log.debug('    - %*s' % (width, rate), '*')
                else:
                    log.debug('    - %*s' % (width, rate))

        # test each frequency on each CPU
        for cpu in cpuset:
            log.debug('- CPU#%u' % cpu.num)
            cpu = cpufreq.CPU(cpu.num)

            log.debug('  - switching to userspace governor...', end = '')
            governor = cpu.governor

            try:
                cpu.governor = 'userspace'
            except Exception as e:
                log.cont('skip (%s)' % e)
                continue
            else:
                log.cont('done')

            for rate in cpu.supported_rates:
                log.debug('  - setting rate %s...' % rate, end = '')

                try:
                    cpu.rate = rate
                except Exception as e:
                    log.cont('fail (%s)' % e)
                else:
                    log.cont('done')

            log.debug('  - restoring %s governor...' % governor, end = '')

            try:
                cpu.governor = governor
            except Exception as e:
                log.cont('fail (%s)' % e)
            else:
                log.cont('done')

tests = [
    hotplug,
    cpufreq,
]

if __name__ == '__main__':
    runner.standalone(module)
