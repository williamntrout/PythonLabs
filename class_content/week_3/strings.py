"""FILE_NAME: PROGRAM_DESCRIPTION"""

import sys

__author__ = "WILLIAM_TROUT"
__license__ = "GPL"
__version__ = "1.0.1"
__date__ = "TODAY'S DATE"

def main(argv):
    """Main function of the script.
    Args:
            argv (list): Contains command-line arguments passed to the script.
    Returns:
    int: Error code after execution (0 if OK).
    """
    error_code = 0

    str = "Hello, world!"
    print(str)
    print(str[-1])
    print(str[-2])
    print(str[-999])
    return error_code

if __name__ == '__main__':
    error_code = main(sys.argv[1:])
    print('[+] Terminated with code: ' + str(error_code))
    sys.exit(error_code)

