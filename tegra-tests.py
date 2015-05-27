#!/usr/bin/python3

import argparse
import boards
import io
import os
import sys
import tegra
import unittest

from linux import kmsg, log, system

class TegraTestLoader(unittest.TestLoader):
    pass

#class TegraTestRunner(unittest.TextTestRunner):
#    pass

class WritelnDecorator(object):
    def __init__(self, stream):
        self.stream = stream

    def __getattr__(self, attr):
        if attr in ('stream', '__getstate__'):
            raise AttributeError(attr)

        return getattr(self.stream, attr)

    def writeln(self, arg = None):
        if arg:
            self.write(arg)

        self.write('\n')

def strclass(cls):
    return '%s.%s' % (cls.__module__, cls.__name__)

class RedirectOutput(io.IOBase):
    def __init__(self, stream = sys.stdout):
        self.stream = stream
        self.newline = True

    def write(self, b):
        if self.newline:
            self.stream.write('| ')

        self.stream.write(b)

        self.newline = b.endswith('\n')

class TegraTestResult(unittest.TestResult):
    def __init__(self, stream = None, descriptions = True, verbosity = 1):
        super().__init__(stream, descriptions, verbosity)
        self.stream = WritelnDecorator(stream)
        self.verbosity = verbosity

    def startTest(self, test):
        self.stdout = sys.stdout
        self.stderr = sys.stderr

        if self.verbosity > 0:
            log.begin('running: %s (%s)' % (strclass(test.__class__),
                                            test._testMethodName),
                      end = '\n')
            sys.stdout = RedirectOutput(sys.stdout)
            sys.stderr = RedirectOutput(sys.stderr)
        else:
            log.begin('running: %s (%s)' % (strclass(test.__class__),
                                            test._testMethodName))
            sys.stdout = None
            sys.stderr = None

        super().startTest(test)

    def stopTest(self, test):
        super().stopTest(test)
        sys.stderr = self.stderr
        sys.stdout = self.stdout
        log.end()

class TegraTestRunner(object):
    def __init__(self, stream = None, descriptions = True, verbosity = 1):
        if not stream:
            stream = sys.stderr

        self.stream = stream
        self.descriptions = descriptions
        self.verbosity = verbosity

    def run(self, test):
        result = TegraTestResult(self.stream, self.descriptions, self.verbosity)
        test(result)
        return result

def show_system_info():
    print('System information:')
    print('-------------------')

    (opsys, hostname, release, version, machine) = os.uname()
    print('OS:', opsys, release, version)
    print('Hostname:', hostname)
    print('Machine:', machine)

    board = boards.detect()
    print('Board:', board.name)

    soc = tegra.detect()
    print('SoC:', soc.name)

    cpus = system.CPUSet()
    cpus.print()

    print()

def show_kmsg():
    with kmsg.open('/dev/kmsg') as log:
        for entry in log:
            print(entry)

if __name__ == '__main__':
    parser = argparse.ArgumentParser('')
    parser.add_argument('--batch', '-b', action = 'store_const', const = True)
    parser.add_argument('--verbose', '-v', default = 1, action = 'count')
    parser.add_argument('--quiet', '-q', action = 'store_const', const = True)
    parser.add_argument('tests', type = str, nargs = '*')
    args = parser.parse_args(sys.argv[1:])

    if args.quiet:
        args.verbose -= 1

    if args.verbose > 0:
        show_system_info()
        #show_kmsg()

    tests = []

    for module in args.tests:
        tests.append('tests.%s' % module)

    loader = TegraTestLoader()

    if args.batch:
        runner = unittest.TextTestRunner(verbosity = args.verbose)
        log.color = False
    else:
        runner = TegraTestRunner(verbosity = args.verbose)
        log.color = False

    if not tests:
        suite = loader.discover('tests', '*.py', '.')
    else:
        suite = loader.loadTestsFromNames(tests)

    runner.run(suite)
