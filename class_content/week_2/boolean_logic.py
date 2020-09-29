"""boolean_logic.py: Demonstrates boolean logic.
"""

import sys

__author__ = "Mikhail Sudakov"
__license__ = "GPL"
__version__ = "1.0.1"
__date__ = "October 3, 2019"


def main(argv):
    """Main function of the script.
    Args:
            argv (list): Contains command-line arguments passed to the script.
    Returns:
    int: Error code after execution (0 if OK).
    """
    error_code = 0
    x = True
    y = False
    z = True
    print('x == ' + str(x) + '; y == ' + str(y) + '; z == ' + str(z))
    print('------------------------------------')
    print('NOT x: ' + str(not x))
    print('x AND y: ' + str(x and y))
    print('x OR y: ' + str(x or y))
    print('x OR y AND z: ' + str(x or y and z))
    print('(x AND y) OR (z AND (NOT x)): ' + str((x and y) or (z and (not x))))
    # ------------------------------------------------------------------------ #
    print('------------------------------------')
    x = 13.37 > 3.14159
    print('x is: ' + str(x))
    y = 5 <= 1
    print('y is: ' + str(y))
    z = "Hello, world!" == 'Hello, world!'
    print('z is: ' + str(z))
    print('(x AND y) OR (z AND (NOT x)): ' + str((x and y) or (z and (not x))))
    return error_code


if __name__ == '__main__':
    error_code = main(sys.argv[1:])
    print('[+] Terminated with code: ' + str(error_code))
    sys.exit(error_code)
