#!/usr/bin/python3

import hashlib, os, subprocess, sys
import runner

from linux import sysfs

module = sys.modules[__name__]
module.name = 'camera'

def find_executable(program):
    for path in os.environ['PATH'].split(os.pathsep):
        filename = os.path.join(path, program)
        if os.path.isfile(filename) and os.access(filename, os.X_OK):
            return filename

    raise FileNotFoundError(filename)

class V4L2Device:
    def __init__(self, path):
        self.path = path

class sanity(runner.Test):
    formats = {
            (1280,  720, 'XR24'): 'bd9790f2ec3e82207c42fe6cbb817a3e',
            (1920, 1080, 'XR24'): 'f17836371f7d8727a5ad9117b7691b64',
            (3840, 2160, 'XR24'): '1fdc0626eab878f3b7d5dc25285d7264',
            (1280,  720, 'RG10'): '270f82cc567a2f14a886ec2467a4d177',
            (1920, 1080, 'RG10'): '6bfe9fd8f18a485d7619f6431d1390e9',
            (3840, 2160, 'RG10'): 'b9175ec8ec0e7ee42fb175ccfd42d399',
        }

    def __call__(self, log, *args, **kwargs):
        failures = 0

        try:
            v4l2_ctl = find_executable('v4l2-ctl')
        except FileNotFoundError as e:
            raise runner.Skip(e.message)

        # XXX parameterize stream index
        bus = sysfs.Bus('host1x')
        dev = bus.device('tegra-video')
        cls = dev.child('video4linux')

        for child in cls:
            path = os.path.join(os.path.sep, 'dev', child.uevent['DEVNAME'])
            device = V4L2Device(path)

            log.debug('testing device %s:' % path)

            for (width, height, pixelformat), checksum in sanity.formats.items():
                fmt = 'width=%u,height=%u,pixelformat=%s' % (width, height,
                                                             pixelformat)

                log.debug('  - capturing frame at %ux%u (%s)...' % (width, height,
                                                                    pixelformat),
                          end = '', flush = True)

                filename = 'tpg-%ux%u-%s.raw' % (width, height,
                                                 pixelformat.lower())

                command = [ v4l2_ctl, '--set-fmt-video=%s' % fmt, '--set-ctrl',
                            'test_pattern=1', '--stream-count=1',
                            '--stream-mmap', '--device=%s' % device.path,
                            '--stream-to=%s' % filename ]

                proc = subprocess.run(command, capture_output = True)
                if proc.returncode != 0:
                    log.cont('failed')
                    log.debug('proc:', proc)
                    failures += 1
                    continue

                log.cont('done')


                log.debug('    - %u bytes captured' % os.path.getsize(filename))
                log.debug('    - checksum...', end = '', flush = True)

                digest = hashlib.md5()

                with open(filename, 'rb') as fobj:
                    digest.update(fobj.read())

                if digest.hexdigest() != checksum:
                    log.cont('failed')
                    failures += 1
                else:
                    log.cont('okay')

        if failures > 0:
            raise runner.Error()

if __name__ == '__main__':
    runner.standalone(module)
