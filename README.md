# Tegra Test Suite

This repository contains a set of scripts for basic sanity testing of
Tegra SoC-based boards.

The main focus of these scripts is to run on upstream versions of the
Linux kernel and make sure things work as expected.

## Directory structure

The `tegra` directory contains a list of SoC definitions. Each of these
defines a list of properties, such as a name or a compatible string for
the given SoC.

Board definitions can be found in the `boards` directory, which is
further divided into vendor directories (e.g. `nvidia`). Each board
is initialized with the corresponding SoC and contains information
describing the specifics of that board.

The `linux` directory contains a set modules that implement various
helpers that can be used to simplify the implementation of various
tests.

All runnable tests can be found in the `tests` directory. Typically
these will be executable scripts that can be passed a standard set of
command-line options.

## Tests

The `runner.py` module implements a basic class that can be used to
implement tests. Each executable script within the `tests` directory
implements one or more tests that will be run sequentially by default.

Common options that can be passed to a test are listed below:

* `--quiet`, `-q`: do not show any output unless a failure occurred
* `--list`, `-l`: display a list of subtests that can be selected
* `--summary`, `-s`: show a summary of the tests that have been run
* `--verbose`, `-v`: show verbose output messages

Furthermore, a space-separated list of subtests to run can be provided
on the command-line to override the default (run all tests).

### boot.py

One of the most useful tests is `tests/boot.py`. It will dump some
system information and inspect which devices have been registered with
the system, as well as detect which driver has been bound to each of
the devices. This will be compared to the desired configuration and any
deviation will be flagged as an error.

If specified for a given board, this can also attempt to unload and
reload a set of drivers, which is a useful sanity test to validate that
loadable module support is functional.

Finally, the kernel log is parsed and inspected for warnings and error
messages. Unless specified in an allow list, such warnings and errors
are flagged and cause the test to fail.

Overall, if this test succeeds it is a good indication that the system
has booted up and is in a sane state. What this test doesn't do is any
device-specific testing. For some devices this may test rudimentary
functionality such as PCI bus enumeration by checking that all expected
PCI devices have been added.

### system.py

This is a slightly more advanced test that will first try to suspend and
wake the system using an RTC. It will then try to find a watchdog device
and test that it works. Note that when successful this test will cause
the system to reboot, so it is not useful to run standalone because it
cannot determine success itself. Software external to the test system
would need to monitor if the device is successfully restarted by the
watchdog timeout.

A third test that this implements is to dump ID EEPROMs that may have
been detected on the board. Various NVIDIA devices ship with these ID
EEPROMs that serve as a way of identifying the system.

It is most useful to run subtests separately to test a particular
feature:

    $ tests/system.py suspend
    $ tests/system.py watchdog
    $ tests/system.py eeprom

### cpu.py

This test will transition between random CPU set permutations and run
through each supported CPU frequency.

### memory.py

If supported, this test will attempt to force any of the supported EMC
frequencies. Setting very low frequencies may cause various failures,
especially if a monitor or display is connected to the system.
