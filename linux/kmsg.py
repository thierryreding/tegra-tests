#!/usr/bin/python3

import fcntl
import io
import os

'''
Kernel log levels
'''
LOG_EMERG = 0
LOG_ALERT = 1
LOG_CRIT = 2
LOG_ERR = 3
LOG_WARNING = 4
LOG_NOTICE = 5
LOG_INFO = 6
LOG_DEBUG = 7

'''
Kernel log facilities
'''
LOG_KERN = 0
LOG_USER = 1
LOG_MAIL = 2
LOG_DAEMON = 3
LOG_AUTH = 4
LOG_SYSLOG = 5
LOG_LPR = 6
LOG_NEWS = 7
LOG_UUCP = 8
LOG_CRON = 9
LOG_AUTHPRIV = 10
LOG_FTP = 11

'''
A timestamp as embedded in kernel log buffer entries. /dev/kmsg returns this
in microseconds, but it's stored in a seconds/microseconds pair here to make
it easier to print out a meaningful timestamp.
'''
class Timestamp():
    def __init__(self, microseconds):
        self.seconds = microseconds / 1000000
        self.microseconds = microseconds % 1000000

    def __str__(self):
        return '%8u.%06u' % (self.seconds, self.microseconds)

'''
The header of a kernel log buffer entry. It contains the log level, facility,
sequence number, timestamp and flags.
'''
class Header():
    def __init__(self, header):
        prefix, seqno, timestamp, flags, *reserved = header.split(',')

        if reserved:
            print('Excess field(s) in header:', reserved)

        self.level = int(prefix) & 0x7
        self.facility = int(prefix) >> 3
        self.seqno = int(seqno)
        self.timestamp = Timestamp(int(timestamp))
        self.flags = flags

    def __str__(self):
        levels = {
                LOG_EMERG: 'EMERG',
                LOG_ALERT: 'ALERT',
                LOG_CRIT: 'CRIT',
                LOG_ERR: 'ERR',
                LOG_WARNING: 'WARNING',
                LOG_NOTICE: 'NOTICE',
                LOG_INFO: 'INFO',
                LOG_DEBUG: 'DEBUG',
            }

        facilities = {
                LOG_KERN: 'KERN',
                LOG_USER: 'USER',
                LOG_MAIL: 'MAIL',
                LOG_DAEMON: 'DAEMON',
                LOG_AUTH: 'AUTH',
                LOG_SYSLOG: 'SYSLOG',
                LOG_LPR: 'LPR',
                LOG_NEWS: 'NEWS',
                LOG_UUCP: 'UUCP',
                LOG_CRON: 'CRON',
                LOG_AUTHPRIV: 'AUTHPRIV',
                LOG_FTP: 'FTP',
            }

        if self.level in levels:
            level = levels[self.level]
        else:
            level = str(self.level)

        if self.facility in facilities:
            facility = facilities[self.facility]
        else:
            facility = str(self.facility)

        return '[%s] %s %s' % (self.timestamp, level, facility)

'''
A kernel log buffer entry, composed of a header, a message and zero or more
variables attached to the entry.
'''
class Entry():
    def __init__(self, line):
        header, message = line.rstrip().split(';', 1)

        self.header = Header(header)
        self.message = message
        self.variables = {}

    def append(self, line):
        key, value = line.strip().split('=', 1)
        self.variables[key] = value

    def __str__(self):
        return '%s %s' % (self.header, self.message)

'''
A kernel log buffer context used to read entries from the kernel log buffer.
'''
class Kmsg():
    def __init__(self, path = '/dev/kmsg'):
        self.kmsg = io.open(path, 'r')

        fd = self.kmsg.fileno()
        flags = fcntl.fcntl(fd, fcntl.F_GETFL)
        flags |= os.O_NONBLOCK
        fcntl.fcntl(fd, fcntl.F_SETFL, flags)

        self.entry = None

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.kmsg.close()

    def read(self):
        while True:
            line = self.kmsg.readline()
            if not line:
                break

            # continuation lines start with a single space
            if not line.startswith(' '):
                entry = None

                if self.entry:
                    entry = self.entry

                self.entry = Entry(line)

                if entry:
                    return entry
            else:
                self.entry.append(line)

        entry = self.entry
        self.entry = None
        return entry

'''
Open the /dev/kmsg device and set the file descriptor to non-blocking. The
returned Kmsg object can be used to read entries from the device one at a
time.
'''
def open(*args):
    return Kmsg(*args)
