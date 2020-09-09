# Variables store information to referenced and manipulated
# variable does not contain information, only references it
# variable contains a pointer to information
# in Python a vriable must be assigned either:
# something (eg a value, object,etc) x = 5
# or nothing (ie null) x = None
# String: searies of characters var = "i am a string with double quotes" var = 'i am a string with single quotes' var = '''i am a string with triple quotes''' var """i am a string with triple-double"""
# can we use const and let here?
# Boolean: stores a single true or false constant bool = False
# NoneType: stores nothing nada = None
# Variable names 
#   can only contain: a-Z, 0-9, and _ (underscore)
#   cannot start with a number
#   case sensitive 
#   Python variable names should be all lower-case, with _ as word seperator
#   All variable names should be descriptive (in human terms...)
# examples:
#   Bad: diy = 365.2422
#   Good: days_in_year = 365.2422
# camel case does not work for python!!! daysInYear = 365.2422
# Reserved words: def, if, for, while, return, import, etc....
#   Cannot be used by the programmer for anything  but that.



import sys

__author__ = "Wiliam Trout"
__license__ = "GPL"
__version__ = "1.0.1"
__date__ = "Sept 31, 2019"


def main(argv):
    x = None
    print(type(x))

    x = 5
    print(type(x))

    abc_stock = 5.00

    abc_stock = abc_stock + 1.5
    
    abc_stock = abc_stock - 3.45

    print("Tomorrow's forcasted prics is: $" + str(abc_stock))



if __name__ == '__main__':
    error_code = main(sys.argv[1:])
    print('[+] Terminated with code: ' + str(error_code))
    sys.exit(error_code)
