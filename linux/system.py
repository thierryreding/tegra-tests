#!/usr/bin/python

import ctypes
import os
import platform
import re
import sys
import time

from . import ioctl, libc, sysfs

'''
Represents one CPU present in the system.
'''
class CPU():
    def __init__(self, num):
        self.sysfs = sysfs.Object('devices/system/cpu', 'cpu%u' % num)
        self.num = num

        try:
            file = self.sysfs.open('online', 'r')
        except FileNotFoundError:
            self.hotpluggable = False
            self.online = True
        else:
            with file:
                online = file.readline().strip()
                if online == '0':
                    self.online = False
                else:
                    self.online = True

            self.hotpluggable = True

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
            if '-' in present:
                self.start, self.end = map(int, present.split('-'))
            else:
                self.start = self.end = int(present)

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
        self.sysfs = sysfs.Object('class/rtc', name)

    '''
    Set the RTC to raise an alarm a given number of seconds from now.
    '''
    def set_alarm_relative(self, alarm):
        alarm = int(time.time()) + alarm

        with self.sysfs.open('wakealarm', 'w') as file:
            file.write('%u' % alarm)

class Kernel:
    class Version:
        def __init__(self, release = None):
            if not release:
                self.release = platform.release()
            else:
                self.release = release

            try:
                self.version, self.extra = self.release.split('-', maxsplit = 1)
            except:
                self.version = self.release
                self.extra = None

            try:
                major, minor, patch = self.version.split('.')
            except:
                major, minor = self.version.split('.')
                patch = 0

            self.major = int(major)
            self.minor = int(minor)
            self.patch = int(patch)
            self.next = None
            self.rc = 0

            if self.extra:
                parts = self.extra.split('-')

                match = re.match('rc(\d+)', parts[0])
                if match:
                    self.rc = int(match.group(1))
                    del parts[0:1]

                if parts:
                    if parts[0] == 'next':
                        self.next = parts[1]
                        del parts[0:2]

        def numerical(self):
            #
            # linux-next is a special case: it contains code that will usually
            # become part of the next release, so version checks usually want
            # to succeed for the next release when run on linux-next.
            #
            if self.next:
                return self.major << 16 | self.minor + 1 << 8 | self.patch

            return self.major << 16 | self.minor << 8 | self.patch

        def __lt__(self, other):
            if isinstance(other, str):
                other = Version(other)

            return self.numerical() < other.numerical()

        def __le__(self, other):
            if isinstance(other, str):
                other = Version(other)

            return self.numerical() <= other.numerical()

        def __eq__(self, other):
            if isinstance(other, str):
                other = Version(other)

            return self.numerical() == other.numerical()

        def __gt__(self, other):
            if isinstance(other, str):
                other = Version(other)

            return self.numerical() > other.numerical()

        def __ge__(self, other):
            if isinstance(other, str):
                other = Version(other)

            return self.numerical() >= other.numerical()

        def __repr__(self):
            return '%u.%u.%u' % (self.major, self.minor, self.patch)

        def __str__(self):
            if self.extra:
                return '%u.%u.%u-%s' % (self.major, self.minor, self.patch, self.extra)
            else:
                return repr(self)

    def __init__(self):
        self.version = Kernel.Version()

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
        self.fd = os.open(path, os.O_RDWR)

    def disable(self):
        options = ctypes.pointer(ctypes.c_uint(Watchdog.WDIOS_DISABLECARD))

        libc.ioctl(self.fd, Watchdog.WDIOC_SETOPTIONS, options)

    def enable(self):
        options = ctypes.pointer(ctypes.c_uint(Watchdog.WDIOS_ENABLECARD))

        libc.ioctl(self.fd, Watchdog.WDIOC_SETOPTIONS, options)

    def set_timeout(self, timeout):
        timeout = ctypes.pointer(ctypes.c_uint(timeout))

        libc.ioctl(self.fd, Watchdog.WDIOC_SETTIMEOUT, timeout)

    def __del__(self):
        options = ctypes.pointer(ctypes.c_uint(Watchdog.WDIOS_DISABLECARD))
        libc.ioctl(self.fd, Watchdog.WDIOC_SETOPTIONS, options)
        os.close(self.fd)

class UnknownVersion(Exception):
    def __init__(self, version):
        super().__init__('unknown version %s' % version)

class EEPROM():
    class MACAddress():
        def __init__(self, data):
            self.data = data

        def __str__(self):
            return ':'.join('%02x' % byte for byte in self.data)

    class ConfigurationBlock():
        def __init__(self, data):
            self.signature = data[0:4].decode('ascii')
            self.length = data[5] << 8 | data[4]
            self.type = data[6:8].decode('ascii')
            self.version = data[9] << 8 | data[8]

            self.mac = {
                    'wifi': EEPROM.MACAddress(data[15:9:-1]),
                    'bluetooth': EEPROM.MACAddress(data[21:15:-1]),
                    'ethernet': EEPROM.MACAddress(data[27:21:-1])
                }

        def dump(self, fobj = sys.stdout):
            print('NV Configuration Block:', file = fobj)
            print('  Signature: %s' % self.signature, file = fobj)
            print('  Length: %u' % self.length, file = fobj)
            print('  Type: %s' % self.type, file = fobj)
            print('  Version: %04x' % self.version, file = fobj)
            print('  MAC addresses:', file = fobj)
            print('    WiFi: %s' % self.mac['wifi'], file = fobj)
            print('    Bluetooth: %s' % self.mac['bluetooth'], file = fobj)
            print('    Ethernet: %s' % self.mac['ethernet'], file = fobj)

    def __init__(self, bus, name):
        self.sysfs = sysfs.Object(os.path.join('bus', bus, 'devices'), name)
        self.nvcb = None

        with self.sysfs.open('eeprom', 'rb') as eeprom:
            data = eeprom.read(-1)

        if data[1] != 0 or data[0] != 1:
            raise UnknownVersion('%04x' % (data[1] << 8 | data[0]))

        self.version = data[1] << 8 | data[0]
        self.size = data[3] << 8 | data[2]
        self.board = data[5] << 8 | data[4]
        self.sku = data[7] << 8 | data[6]
        self.fab = data[8]
        self.rev = chr(data[9])
        self.minor = data[10]

        self.memory = data[11]
        self.power = data[12]
        self.misc = data[13]
        self.modem = data[14]
        self.touchscreen = data[15]
        self.display = data[16]
        self.rework = data[17]
        self.sno = data[19] << 8 | data[18]
        self.product = data[20:50].decode('ascii')

        self.mac = {
                'wifi': EEPROM.MACAddress(data[55:49:-1]),
                'bluetooth': EEPROM.MACAddress(data[61:55:-1]),
                'wifi_secondary': EEPROM.MACAddress(data[67:61:-1]),
                'ethernet': EEPROM.MACAddress(data[73:67:-1])
            }

        self.serial = data[74:89].decode('ascii')

        if data[150:154] == b'NVCB':
            self.nvcb = EEPROM.ConfigurationBlock(data[150:255])

        checksum = EEPROM.checksum(data[0:255])
        crc = data[255]

        if crc != checksum:
            print('checksum mismatch: %02x, should be %02x' % (checksum, crc))

    def dump(self, fobj = sys.stdout):
        print('Version: %04x' % self.version, file = fobj)
        print('Size: %u' % self.size, file = fobj)
        print('Board: %u' % self.board, file = fobj)
        print('SKU: %u' % self.sku, file = fobj)
        print('Fab: %u' % self.fab, file = fobj)
        print('Revision: %s' % self.rev, file = fobj)
        print('Minor: %u' % self.minor, file = fobj)
        print('Memory: %u' % self.memory, file = fobj)
        print('Power: %u' % self.power, file = fobj)
        print('Misc: %u' % self.misc, file = fobj)
        print('Modem: %u' % self.modem, file = fobj)
        print('Touchscreen: %u' % self.touchscreen, file = fobj)
        print('Display: %u' % self.display, file = fobj)
        print('Rework: %u' % self.rework, file = fobj)
        print('SNO: %u' % self.sno, file = fobj)
        print('Product: %s' % self.product, file = fobj)
        print('MAC addresses:', file = fobj)
        print('  WiFi: %s' % self.mac['wifi'], file = fobj)
        print('  Bluetooth: %s' % self.mac['bluetooth'], file = fobj)
        print('  Secondary WiFi: %s' % self.mac['wifi_secondary'], file = fobj)
        print('  Ethernet: %s' % self.mac['ethernet'], file = fobj)
        print('Serial: %s' % self.serial, file = fobj)

        if self.nvcb:
            self.nvcb.dump(fobj)

    @staticmethod
    def checksum(data):
        crc = 0

        for byte in data:
            for i in range(8):
                odd = ((crc ^ byte) & 1) == 1

                byte >>= 1
                crc >>= 1

                if odd:
                    crc ^= 0x8c

        return crc & 0xff
