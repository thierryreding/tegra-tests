#!/usr/bin/python3

import inspect, re

def listify(arguments):
    *start, last = arguments

    if start:
        return ' and '.join([', '.join('%s' % x for x in start), last])

    return last

def require_arguments(**kwargs):
    missing = []

    for key, value in kwargs.items():
        if not value:
            missing.append(key)

    if missing:
        caller = inspect.stack()[1].function

        raise TypeError("%s() missing %u required argument%s: %s" %
                (caller, len(missing), 's' if len(missing) > 1 else '',
                    listify(missing)))

class AllowList():
    class Pattern:
        def __init__(self, re):
            self.matches = []
            self.re = re

    def __init__(self, patterns):
        self.patterns = []

        for pattern in patterns:
            pattern = re.compile(pattern)
            pattern = AllowList.Pattern(pattern)
            self.patterns.append(pattern)

    def unmatched(self):
        result = []

        for pattern in self.patterns:
            if not pattern.matches:
                result.append(pattern.re.pattern)

        return result

    def __contains__(self, item):
        for pattern in self.patterns:
            if pattern.re.match(item.message):
                pattern.matches.append(item.message)
                return True

        return False
