"""FILE_NAME: PROGRAM_DESCRIPTION"""

import sys

__author__ = "YOUR_NAME"
__license__ = "GPL"
__version__ = "1.0.1"
__date__ = "TODAY'S DATE"


def count_char(str, total, i):
    """counts the characters in a given strint
        Args:
                str(string): string of characters to be counted.
                char(char): characters inside the string.
        """
    str = input("enter your string : ")
    total = 0

    for i in str:
        total = total + 1
    print("total number of characters in this string = ", total)






def main(argv):
    print("hello, world")
    # str = "Hello, world!"
    # print(str)
    # print(str[-1])
    # print(str[-2])
    # print(str[-3])
    # print(str[-4])
 
    
    


if __name__ == '__main__':
    error_code = main(sys.argv[1:])
    print('[+] Terminated with code: ' + str(error_code))
    sys.exit(error_code)
