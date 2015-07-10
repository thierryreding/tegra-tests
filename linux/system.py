#!/usr/bin/python

import ctypes
import os
import sys
import time

from . import ioctl, libc, sysfs

'''
Represents one CPU present in the system.
'''
class CPU():
    def __init__(self, num):
        self.sysfs = sysfs.Object('devices/system/cpu/cpu%u' % num)
        self.hotpluggable = True
        self.num = num

        with self.sysfs.open('online', 'r') as file:
            online = file.readline().strip()
            if online == '0':
                self.online = False
            else:
                self.online = True

    '''
    Bring the CPU online or take it offline.
    '''
    def set_online(self, online):
        with self.sysfs.open('online', 'w') as file:
            if online:
                file.write('1')
            else:
                file.write('0')

            self.online = online

    '''
    Return the CPU mask.
    '''
    def mask(self):
        return 1 << self.num

    def __str__(self):
        if self.online:
            status = 'online'
        else:
            status = 'offline'

        return 'CPU#%u: %s' % (self.num, status)

'''
Maintain a list of CPUs available in the system and provide functionality for
bringing them online or taking them offline.
'''
class CPUSet():
    def __init__(self):
        with sysfs.open('devices/system/cpu/present', 'r') as file:
            present = file.readline().rstrip()
            self.start, self.end = map(int, present.split('-'))

        self.cpus = []

        for n in range(self.start, self.end + 1):
            cpu = CPU(n)

            if n == self.start:
                cpu.hotpluggable = False

            self.cpus.append(cpu)

    '''
    Return the number of CPUs in this set.
    '''
    def count(self):
        return len(self.cpus)

    def print(self, file = sys.stdout):
        print('CPU Set: %u CPUs' % self.count(), file = file)
        for cpu in self.cpus:
            print(' ', cpu, file = file)

    '''
    Generate a list of masks for all possible on/off combinations of all
    CPUs in this set.
    '''
    def generate_masks(self, cpu = None, cpus = None, mask = 0):
        masks = []

        if cpu == None or cpus == None:
            cpus = self.cpus[:]
            cpus.reverse()
            cpu, *cpus = cpus

        mask |= cpu.mask()

        if cpus:
            new = self.generate_masks(cpus[0], cpus[1:], mask)
            masks.extend(new)
        else:
            masks.append(mask)

        mask &= ~cpu.mask()

        if cpus:
            new = self.generate_masks(cpus[0], cpus[1:], mask)
            masks.extend(new)
        else:
            masks.append(mask)

        return masks

    '''
    Take all CPUs in this set offline.
    '''
    def offline(self):
        for cpu in self.cpus:
            if cpu.hotpluggable:
                cpu.set_online(False)

    '''
    Bring all CPUs in this set online.
    '''
    def online(self):
        for cpu in self.cpus:
            if cpu.hotpluggable:
                cpu.set_online(True)

    '''
    Applies a CPU mask to this set of CPUs. All CPUs for which a bit is set in
    the mask will be brought online. CPUs that have their corresponding bit in
    the mask cleared will be taken offline.
    '''
    def apply_mask(self, mask):
        for cpu in self.cpus:
            if not cpu.hotpluggable:
                continue

            if mask & cpu.mask():
                cpu.set_online(True)
            else:
                cpu.set_online(False)

    '''
    Return the iterator over the list of the CPUs in this set.
    '''
    def __iter__(self):
        return iter(self.cpus)

'''
Provides access to a realtime clock device in the system.
'''
class RTC:
    def __init__(self, name = 'rtc0'):
        self.sysfs = sysfs.Object('class/rtc/%s' % name)

    '''
    Set the RTC to raise an alarm a given number of seconds from now.
    '''
    def set_alarm_relative(self, alarm):
        alarm = int(time.time()) + alarm

        with self.sysfs.open('wakealarm', 'w') as file:
            file.write('%u' % alarm)

'''
Provides access to the system and system wide controls.
'''
class System:
    def __init__(self):
        pass

    def suspend(self):
        with sysfs.open('power/state', 'w') as file:
            file.write('mem')

'''
Provides access to a watchdog device in the system.
'''
class Watchdog():
    WDIOC_SETOPTIONS = ioctl.IOR(ord('W'), 4, 4)
    WDIOC_SETTIMEOUT = ioctl.IOWR(ord('W'), 6, 4)

    WDIOS_DISABLECARD = 0x0001
    WDIOS_ENABLECARD = 0x0002

    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.fd = os.open(self.path, os.O_RDWR)

    def disable(self):
        options = ctypes.pointer(ctypes.c_uint(Watchdog.WDIOS_DISABLECARD))

        libc.ioctl(self.fd, Watchdog.WDIOC_SETOPTIONS, options)

    def enable(self):
        options = ctypes.pointer(ctypes.c_uint(Watchdog.WDIOS_ENABLECARD))

        libc.ioctl(self.fd, Watchdog.WDIOC_SETOPTIONS, options)

    def set_timeout(self, timeout):
        timeout = ctypes.pointer(ctypes.c_uint(timeout))

        libc.ioctl(self.fd, Watchdog.WDIOC_SETTIMEOUT, timeout)

    def __exit__(self, type, value, traceback):
        options = ctypes.pointer(ctypes.c_uint(Watchdog.WDIOS_DISABLECARD))
        libc.ioctl(self.fd, Watchdog.WDIOC_SETOPTIONS, options)
        os.close(self.fd)
