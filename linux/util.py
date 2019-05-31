#!/usr/bin/python3

import re

class WhiteList():
    class Pattern:
        def __init__(self, re):
            self.matches = []
            self.re = re

    def __init__(self, patterns):
        self.patterns = []

        for pattern in patterns:
            pattern = re.compile(pattern)
            pattern = WhiteList.Pattern(pattern)
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
