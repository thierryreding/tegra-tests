#!/usr/bin/python3

IOC_NONE = 0
IOC_WRITE = 1
IOC_READ = 2

IOC_DIR_SHIFT = 30
IOC_SIZE_SHIFT = 16
IOC_TYPE_SHIFT = 8
IOC_NR_SHIFT = 0

def IOC(dir, type, nr, size):
    return dir << IOC_DIR_SHIFT | size << IOC_SIZE_SHIFT | type << IOC_TYPE_SHIFT | nr << IOC_NR_SHIFT

def IO(type, nr, size):
    return IOC(IOC_NONE, type, nr, size)

def IOW(type, nr, size):
    return IOC(IOC_WRITE, type, nr, size)

def IOR(type, nr, size):
    return IOC(IOC_READ, type, nr, size)

def IOWR(type, nr, size):
    return IOC(IOC_WRITE | IOC_READ, type, nr, size)
