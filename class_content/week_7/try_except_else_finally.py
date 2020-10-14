"""try_except_else_finally.py: Demonstrates catching multiple exceptions and using
	the else and the finally clauses in the try-except code block.
."""

import sys

__author__ = "Mikhail Sudakov"
__license__ = "GPL"
__version__ = "1.0.1"
__date__ = "November 11, 2019"


def main(argv):
    """Main function of the script.
    Args:
            argv (list): Contains command-line arguments passed to the script.
    Returns:
    int: Error code after execution (0 if OK).
    """
    error_code = 0

    try:
        # Open a file 'file.txt' in the same directory with read-only privilege.
        fp = open('file.txt', 'r')		# 'fp' for File Pointer
        # Read the first line from the file.
        line = fp.readline()
        # Convert the data in the line to an integer.
        i = int(line.strip())
    except OSError as os_err:
        print("OS error: {0}".format(os_err))
    except ValueError:
        print("ERROR: Could not convert data to an integer.")
    else:
        print('Successfully converted ' + str(i) + ' to integer!')
        # Close the file.
        fp.close()
    finally:
        print('Exiting program...')

    return error_code


if __name__ == '__main__':
    error_code = main(sys.argv[1:])
    print('[+] Terminated with code: ' + str(error_code))
    sys.exit(error_code)
