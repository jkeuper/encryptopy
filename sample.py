#!/usr/bin/env python3

import sys

class Example(object):
    def run(self):
        for arg in sys.argv:
            print(arg)
if __name__ == '__main__':
    Example().run()
