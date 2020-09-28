"""FILE_NAME: PROGRAM_DESCRIPTION"""

import sys

__author__ 	= "YOUR_NAME"
__license__ = "GPL"
__version__ = "1.0.1"
__date__ 	= "TODAY'S DATE"

def factorial(num):
	"""Recursively computes the factorial of a number.
	Args:
		num (int): Number to compute factorial of.
	Returns:
        int: The factorial result of a number.
	"""
	pass

def fibonacci(n):
	"""Recursively computes the nth number in the
		Fibonacci Sequence.
	Args:
		n (int): The number's position in the Fibonacci
			Sequence, starting at 0.
	Returns:
        int: The nth number in the Fibonacci Sequence,
			starting at 0.
	"""
	pass

def main(argv):
	"""Main function of the script.
	Args:
		argv (list): Contains command-line arguments passed to the script.
	Returns:
        int: Error code after execution (0 if OK).
	"""
	error_code = 0
	
	##################
	# TEST YOUR CODE #
	##################
	print(factorial(13))
	print(fibonacci(10))
	
	return error_code

if __name__ == '__main__':
	error_code = main(sys.argv[1:])
	print('[+] Terminated with code: ' + str(error_code))
	sys.exit(error_code)