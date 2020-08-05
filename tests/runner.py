#!/usr/bin/python3

import argparse, builtins, io, os.path, sys

class Log:
    def __init__(self, module, output):
        self.module = module
        self.output = output
        self.verbose = False
        self.test = None

    def print(self, *args, **kwargs):
        if self.output:
            kwargs['file'] = self.output

            builtins.print(*args, **kwargs)

    def info(self, *args, **kwargs):
        if self.test:
            args = [ '%s:' % type(self.test).__name__, *args ]

        args = [ '%s:' % self.module.name, *args ]

        self.print(*args, **kwargs)
        self.next = self.print

    def debug(self, *args, **kwargs):
        if self.verbose:
            self.info(*args, **kwargs)
            self.next = self.print
        else:
            self.next = None

    def cont(self, *args, **kwargs):
        if self.next:
            kwargs['file'] = self.output

            self.next(*args, **kwargs)

class Test:
    pass

class Error(Exception):
    pass

class Skip(Exception):
    pass

def skip(reason):
    def decorator(test):
        class SkipTest(Test):
            def __call__(self, log, *args, **kwargs):
                raise Skip(reason)

        # need to overwrite this in case we have test filters in place
        SkipTest.__name__ = test.__name__

        return SkipTest

    return decorator

def _id(obj):
    return obj

def skipIf(condition, reason):
    if condition:
        return skip(reason)

    return _id

def skipUnless(condition, reason):
    if not condition:
        return skip(reason)

    return _id

def standalone(module):
    parser = argparse.ArgumentParser('')
    parser.add_argument('--quiet', '-q', action = 'store_true',
                        help = 'do not show any output unless a failure occurred')
    parser.add_argument('--kernel', '-k', type = str, default = '',
                        help = 'override kernel version')
    parser.add_argument('--list', '-l', action = 'store_true',
                        help = 'display a list of subtests that can be selected')
    parser.add_argument('--summary', '-s', action = 'store_true',
                        help = 'show a summary of the tests that have been run')
    parser.add_argument('--verbose', '-v', action = 'store_true',
                        help = 'show verbose output messages')
    parser.add_argument('subtests', metavar = 'SUBTEST', nargs = '*',
                        help = 'a list of tests that should be run')
    args = parser.parse_args(sys.argv[1:])

    if args.kernel:
        # need to do the import here because it needs to run after the Python
        # path was set up
        from linux import system

        system.Kernel.release = args.kernel

    if args.quiet:
        output = io.StringIO()
    else:
        output = sys.stdout

    log = Log(module, output)

    if args.verbose or args.quiet:
        log.verbose = True

    okay = 0
    fail = 0
    skip = 0

    num_tests = 0
    tests = []

    for key, value in module.__dict__.items():
        if isinstance(value, type) and issubclass(value, Test):
            if not args.subtests or value.__name__ in args.subtests:
                tests.append(value)

            num_tests += 1

    if num_tests == 0:
        log.error('no tests found in module', module)
        return

    if args.list:
        for test in tests:
            log.info(test.__name__)

        sys.exit(0)

    for test in tests:
        log.test = test()

        try:
            log.test(log = log)
            log.info('OKAY')
            okay += 1
        except Error as e:
            log.info('FAIL')
            fail += 1
        except Skip as e:
            log.info(e)
            log.info('SKIP')
            skip += 1
        except Exception as e:
            raise

        log.test = None

    if args.summary:
        log.info('Tests:', okay + fail + skip)
        log.info('  okay:', okay)
        log.info('  fail:', fail)
        log.info('  skip:', skip)

    if fail > 0:
        log.info('FAIL')

        if args.quiet:
            output.seek(0, io.SEEK_SET)
            message = output.read()
            print(message, file = sys.stderr, end = '')

        sys.exit(1)
    else:
        log.info('OKAY')
        sys.exit(0)

module = sys.modules[__name__]

path = os.path.dirname(module.__file__)
path = os.path.join(path, '..')
path = os.path.abspath(path)

sys.path.append(path)
