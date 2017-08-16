#!/usr/bin/python3

import time, unittest

from linux import log, sysfs

def find_fbcon():
    for console in sysfs.list('class/vtconsole'):
        with console.open('name', 'r') as f:
            for line in f:
                line = line.strip()
                if line.endswith('frame buffer device'):
                    return console

class kms(unittest.TestCase):
    def test_fbcon_unbind_bind(self):
        console = find_fbcon()

        time.sleep(1)

        with console.open('bind', 'w') as f:
            print('unbinding %s...' % console.path)
            f.write('0')

        time.sleep(1)

        with console.open('bind', 'w') as f:
            print('binding %s...' % console.path)
            f.write('1')
