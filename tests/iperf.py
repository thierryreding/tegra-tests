#!/usr/bin/python3

import json, os, subprocess, sys
import runner

import linux.net

module = sys.modules[__name__]
module.name = 'iperf'

class Endpoint:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def __str__(self):
        return '%s:%u' % (self.host, self.port)

class Connection:
    def __init__(self, data):
        self.local = Endpoint(data['remote_host'], data['remote_port'])
        self.remote = Endpoint(data['local_host'], data['local_port'])

    def __str__(self):
        return 'local: %s, remote: %s' % (self.local, self.remote)

class Interval:
    def __init__(self, data):
        self.start = data['sum']['start']
        self.end = data['sum']['end']
        self.seconds = data['sum']['seconds']
        self.bytes = data['sum']['bytes']
        self.bps = data['sum']['bits_per_second']

    def __str__(self):
        bps, unit = linux.net.Speed.format(self.bps)

        return 'interval: %.3f-%.3f, %.3f seconds, %.3f %s' % (self.start, self.end, self.seconds, bps, unit)

class Summary:
    def __init__(self, data):
        sent, recv = data['sum_sent'], data['sum_received']
        self.send = linux.net.Speed(sent['bytes'] * 8, sent['seconds'])
        self.recv = linux.net.Speed(recv['bytes'] * 8, recv['seconds'])

    def __str__(self):
        return 'in: %s out: %s' % (self.send, self.recv)

    def check(self, speed):
        if self.send < speed:
            return False

        if self.recv < speed:
            return False

        return True

def setup_parser(parser):
    parser.add_argument('--ip', type = str, default = None,
                        help = 'IP to connect to')

class host(runner.Test):
    def __call__(self, log, *args, **kwargs):
        args = [ 'iperf3', '--server', '--one-off', '--json' ]

        proc = subprocess.run(args, capture_output = True)
        if proc.returncode != 0:
            raise runner.Error('"%s" failed: %d' % (args[0], proc.returncode))

        report = json.loads(proc.stdout)

        for item in report['start']['connected']:
            connection = Connection(item)
            log.debug(connection)

        for interval in report['intervals']:
            interval = Interval(interval)
            log.debug(interval)

        summary = Summary(report['end'])
        log.debug(summary)

class target(runner.Test):
    def __call__(self, log, *args, **kwargs):
        gateway = kwargs['args'].ip

        if not gateway:
            gateway = linux.net.find_gateway()

        interface = linux.net.find_interface(gateway)

        args = [ 'iperf3', '--client', str(gateway), '--time', '16', '--json' ]

        proc = subprocess.run(args, capture_output = True)
        if proc.returncode != 0:
            raise runner.Error('"%s" failed: %d' % (args[0], proc.returncode))

        report = json.loads(proc.stdout)

        log.debug('interface:', interface, '(%s)' % interface.speed)

        for item in report['start']['connected']:
            connection = Connection(item)
            log.debug(connection)

        for interval in report['intervals']:
            interval = Interval(interval)
            log.debug(interval)

        summary = Summary(report['end'])
        log.debug(summary)

        # impossible to reach the maximum, so settle for 90%
        expected = interface.speed * 0.90

        if not summary.check(expected):
            raise runner.Error('bad performance: send: %s, receive: %s, expected: %s' % (summary.send, summary.recv, expected))

if __name__ == '__main__':
    runner.standalone(module)
