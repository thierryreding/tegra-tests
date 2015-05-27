import sys

color = True

def begin(message, end = ''):
    print('%s...' % message, end = end)
    sys.stdout.flush()

def end(error = None):
    if error:
        if color:
            print('\033[31mfailed\033[0m:', error)
        else:
            print('failed:', error)
    else:
        if color:
            print('\033[32mdone\033[0m')
        else:
            print('done')
