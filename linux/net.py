#!/usr/bin/python3

import json, subprocess
from . import sysfs

class Host:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '%s' % self.name

    def __eq__(self, other):
        return self.name == other

class Speed:
    def __init__(self, bits, seconds = 1.0):
        self.bits = bits
        self.seconds = seconds

    @staticmethod
    def format(bps):
        units = [ 'bps', 'Kbps', 'Mbps', 'Gbps', 'Tbps' ]
        index = 0

        while bps > 1000:
            bps /= 1000
            index += 1

        return bps, units[index]

    def __lt__(self, other):
        return self.bits / self.seconds < other.bits / other.seconds

    def __mul__(self, other):
        if not isinstance(other, float):
            raise Exception()

        return Speed(self.bits * other, self.seconds)

    def __str__(self):
        return '%u %s' % Speed.format(self.bits / self.seconds)

class Interface:
    def __init__(self, name):
        self.name = name
        self.sysfs = sysfs.Device(subsystem = 'net', name = name)

        try:
            file = self.sysfs.open('speed')
        except FileNotFoundError:
            self.speed = None
        else:
            with file:
                value = file.readline().strip()
                self.speed = Speed(int(value) * 1000000)

    def __str__(self):
        return '%s' % self.name

def find_gateway():
    args = [ 'ip', '--json', 'route' ]

    proc = subprocess.run(args, capture_output = True)
    if proc.returncode != 0:
        raise Exception('"%s" failed: %u' % (args[0], proc.returncode))

    table = json.loads(proc.stdout)

    for route in table:
        if route['dst'] == 'default' and 'gateway' in route:
            return Host(route['gateway'])

    return None

def find_interface(gateway = None):
    args = [ 'ip', '--json', 'route' ]

    proc = subprocess.run(args, capture_output = True)
    if proc.returncode != 0:
        raise Exception('"%s" failed: %u' % (args[0], proc.returncode))

    table = json.loads(proc.stdout)

    for route in table:
        if gateway:
            if 'gateway' in route and route['gateway'] == gateway:
                return Interface(route['dev'])
        else:
            if route['dst'] == 'default' and 'dev' in route:
                return Interface(route['dev'])

    return None

if __name__ == '__main__':
    gateway = find_gateway()
    interface = find_interface(gateway)

    print('default gateway:', gateway, 'interface:', interface, '(speed: %u)' % interface.speed)
    print('default interface:', find_interface())
