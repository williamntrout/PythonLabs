"""console_args.py: Demonstrates working with command line arguments."""

import sys

__author__ 	= "Mikhail Sudakov"
__license__ = "GPL"
__version__ = "1.0.1"
__date__ 	= "October 27, 2019"

def sum(nums):
	"""Sums up a list of integers.
	Args:
		nums (list): List of integers to add to the sum.
	Returns:
        int: The sum of all integers.
	"""
	sum = 0
	for num in nums:
		sum += int(num)
	return sum

def main(argv):
	"""Main function of the script.
	Args:
		argv (list): Contains command-line arguments passed to the script.
	Returns:
        int: Error code after execution (0 if OK).
	"""
	error_code = 0
	
	for i in range(0, len(argv), 1):
		print('Argument #' + str(i + 1) + ': ' + str(argv[i]))
	# print(sum(argv))
	
	return error_code

if __name__ == '__main__':
	error_code = main(sys.argv[1:])
	print('[+] Terminated with code: ' + str(error_code))
	sys.exit(error_code)