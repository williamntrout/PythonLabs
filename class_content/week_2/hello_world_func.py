"""hello_world_func.py: Prints out the message 'Hello, world!'."""

import sys

__author__ = "Mikhail Sudakov"
__license__ = "GPL"
__version__ = "1.0.1"
__date__ = "October 2, 2019"


def print_hello_world():
    """Prints out the message 'Hello, world!'."""
    print('Hello, world!')


def main(argv):
    """Main function of the script.
    Args:
            argv (list): Contains command-line arguments passed to the script.
    Returns:
    int: Error code after execution (0 if OK).
    """
    error_code = 0

    print_hello_world()
    str = print_hello_world()
    print(str)

    return error_code


if __name__ == '__main__':
    error_code = main(sys.argv[1:])
    print('[+] Terminated with code: ' + str(error_code))
    sys.exit(error_code)
