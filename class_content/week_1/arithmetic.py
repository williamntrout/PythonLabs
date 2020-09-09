# basic math from class material.
# basic math rules apply, order of operations invoked
# whole numbers are integers (int)
# Floating point, decimals are (float)
# long integer (long) unbelievably long number
# complex  numbers (complex) scientific notation
# type() function accepts a single value and returns the class of the resolved value as type


import sys

__author__ = "William Trout"
__license__ = "GPL"
__version__ = "1.0.1"
__date__ = "Sept 31, 2019"


def main(argv):
    print(type(7))
    print(type(7.0))
    print(2 + 2)
    print(2 - 3)
    print(3 * 3)
    print(3 / 3)
    print(10 / 4)
    print(2 ** 4)
    print(9.999999999999999999999999)
    print(type(7 - 1))
    print(float(5))
    print(((2 - 5)** 13 / ((157 + 594 * 7)** 23 % 1337) - 4 ** 19) % 664)
    
   

    
    
    

    


if __name__ == '__main__':
    error_code = main(sys.argv[1:])
    print('[+] Terminated with code: ' + str(error_code))
    sys.exit(error_code)
