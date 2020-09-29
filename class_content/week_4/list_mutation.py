"""list_mutation.py: Demonstrates the list mutation property."""

import sys

__author__ 	= "Mikhail Sudakov"
__license__ = "GPL"
__version__ = "1.0.1"
__date__ 	= "October 14, 2019"

def main(argv):
	"""Main function of the script.
	Args:
		argv (list): Contains command-line arguments passed to the script.
	Returns:
        int: Error code after execution (0 if OK).
	"""
	error_code = 0
	# Immutable data types
	print('1337 == 1337: ' + str(1337 == 1337))
	print('1337 is 1337: ' + str(1337 is 1337))
	print('3.14159 == 3.14159: ' + str(3.14159 == 3.14159))
	print('3.14159 is 3.14159: ' + str(3.14159 is 3.14159))
	print('True == True: ' + str(True == True))
	print('True is True: ' + str(True is True))
	print("'woot' == 'woot': " + str('woot' == 'woot'))
	print("'woot' is 'woot': " + str('woot' is 'woot'))
	
	# Lists are mutable...
	x = ['A', 'B', 'C']
	y = ['A', 'B', 'C']
	print(x)
	print(y)
	print('Are the lists equal?: ' + str(x == y))
	print('Are the lists the same?: ' + str(x is y))
	x[0] = 'Z'
	print(x)
	print(y)
	
	# Copying the reference to the same list 
	x = ['A', 'B', 'C']
	y = x
	print(x)
	print(y)
	print('Are the lists equal?: ' + str(x == y))
	print('Are the lists the same?: ' + str(x is y))
	x[0] = 'Z'
	print(x)
	print(y)
	
	return error_code

if __name__ == '__main__':
	error_code = main(sys.argv[1:])
	print('[+] Terminated with code: ' + str(error_code))
	sys.exit(error_code)