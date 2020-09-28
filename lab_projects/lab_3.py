"""FILE_NAME: PROGRAM_DESCRIPTION"""

import sys

__author__ = "William_Trout"
__license__ = "GPL"
__version__ = "1.0.1"
__date__ = "Sept_19_2020"


def transpose_string(str):
    """Transposes a string from end to start.
    Args:
            str (string): String to be transposed.
    Returns:
    string: Transposed string (read back to front).
    """
    reversed_string = ''
    for i in str:
        reversed_string = i + reversed_string
    print("Transposed string is: ", reversed_string)


transpose_string("Hello, World!")


def count_char(char, str):
    """Counts the number of occurrences of a character
            in a string.
    Args:
            char (string): Character to find and count.
            str (string): String to be searched.
    Returns:
    int: Number of occurrences of the character
                    in the string.
    """
    for char in str:
        if len(str) == 0:
            break
        char = str[0]
        if char == ' ' or char == '\t':
            continue
        count = 1
        for char in str[0]:
            if char == str[0]:
                count = + 1
        str = str.replace(char, '').strip()
        print(char + " - ", count)


count_char('', 'abcdefghijklmnopqrstuvwxyz')


def main(argv):
    """Main function of the script.
    Args:
            argv (list): Contains command-line arguments passed to the script.
    Returns:
    int: Error code after execution (0 if OK).
    """
    error_code = 0
    return error_code


if __name__ == '__main__':
    error_code = main(sys.argv[1:])
    print('[+] Terminated with code: ' + str(error_code))
    sys.exit(error_code)
