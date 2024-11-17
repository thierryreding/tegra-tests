#!/usr/bin/python

class IGX():
    def __init__(self):
        self.release = {}

        with open('/etc/igx-release', 'r') as fobj:
            for line in fobj:
                key, value = line.strip().split('=')
                self.release[key] = value.strip('"')

    def __getattr__(self, name):
        return self.release[name]


class Firmware():
    def __init__(self):

        with open('/sys/class/dmi/id/bios_version', 'r') as f:
            self.version = f.readline().strip()

