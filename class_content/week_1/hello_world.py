# hello_world.py: Prints out the message 'Hello, world!.'

import sys

__author__ = "Wiliam Trout"
__license__ = "GPL"
__version__ = "1.0.1"
__date__ = "Sept 31, 2019"


def main(argv):
    error_code = 0
    print('Hello, world!')
    return error_code


if __name__ == '__main__':
    error_code = main(sys.argv[1:])
    print('[+] Terminated with code: ' + str(error_code))
    sys.exit(error_code)
