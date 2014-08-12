#!/usr/bin/python3

import ctypes
import os

def get_errno():
    return libc.__errno_location().contents.value

def errno_check(result, func, arguments):
    errno = get_errno()

    if result == -1:
        raise OSError(errno, os.strerror(errno))

    return result

def ioctl(fd, arg, value = 0):
    return libc.ioctl(fd, arg, value)

libc = ctypes.CDLL('libc.so.6')
libc.__errno_location.restype = ctypes.POINTER(ctypes.c_int)

libc.ioctl.restype = ctypes.c_int
libc.ioctl.errcheck = errno_check
