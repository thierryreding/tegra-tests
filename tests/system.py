import os
import unittest

class SystemInfo(unittest.TestCase):
    def test_show(self):
        print('System information:')
        print('-------------------')

        (opsys, hostname, release, version, machine) = os.uname()
        print('OS:', opsys, release, version)
        print('Hostname:', hostname)
        print('Machine:', machine)

        board = detect()
        board.print()

        cpus = system.CPUSet()
        cpus.print()
