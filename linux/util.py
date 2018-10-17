#!/usr/bin/python3

import re

class WhiteList():
    def __init__(self, patterns):
        self.patterns = [ re.compile(pattern) for pattern in patterns ]

    def __contains__(self, item):
        for pattern in self.patterns:
            if pattern.match(item.message):
                return True

        return False
