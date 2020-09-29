"""simplifying_conditions.py: Demonstrates how to simplify
	logic of conditional statements.
"""

import sys

__author__ 	= "Mikhail Sudakov"
__license__ = "GPL"
__version__ = "1.0.1"
__date__ 	= "October 4, 2019"

def foo(x, y):
	"""This dummy function returns True when and only when x is True,
		and y is False; otherwise, it returns False.
	Args:
		x (bool): Some boolean variable.
		y (bool): Some other boolean variable.
	Returns:
        bool: True when x is True and y is False; False otherwise.
	"""
	if x == True and y == False:
		return True
	else:
		return False

def bar(x, y):
	"""This dummy function returns False when both x and y are True,
		and True otherwise.
	Args:
		x (bool): Some boolean variable.
		y (bool): Some other boolean variable.
	Returns:
        bool: False when x is True and y is True; True otherwise.
	"""
	if x and y:
		return False
	else:
		return True

def main(argv):
	"""Main function of the script.
	Args:
		argv (list): Contains command-line arguments passed to the script.
	Returns:
        int: Error code after execution (0 if OK).
	"""
	error_code = 0
	
	print(foo(False, False))
	print(foo(False, True))
	print(foo(True, False))
	print(foo(True, True))
	print(bar(False, False))
	print(bar(False, True))
	print(bar(True, False))
	print(bar(True, True))
	return error_code

if __name__ == '__main__':
	error_code = main(sys.argv[1:])
	print('[+] Terminated with code: ' + str(error_code))
	sys.exit(error_code)