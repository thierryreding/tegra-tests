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

def standalone(module):
    output = sys.stdout

    parser = argparse.ArgumentParser('')
    parser.add_argument('--quiet', '-q', action = 'store_true')
    parser.add_argument('--summary', '-s', action = 'store_true')
    parser.add_argument('--verbose', '-v', action = 'store_true')
    args = parser.parse_args(sys.argv[1:])

    if args.quiet:
        output = io.StringIO()

    log = Log(module, output)

    if args.verbose or args.quiet:
        log.verbose = True

    okay = 0
    fail = 0
    skip = 0

    for test in module.tests:
        log.test = test()

        try:
            log.test(log = log)

            if args.summary:
                log.info('OKAY')

            okay += 1
        except Error as e:
            log.info(e)

            if args.summary:
                log.info('FAIL')

            fail += 1
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
