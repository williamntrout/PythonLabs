"""bubble_sort.py: Demonstrates the Bubble Sort algorithm."""

import sys

__author__ 	= "Mikhail Sudakov"
__license__ = "GPL"
__version__ = "1.0.1"
__date__ 	= "October 28, 2019"

def bubble_sort(unsorted_list):
	"""Sorts a list of items with the Bubble Sort algorithm.
	Args:
		unsorted_list (list): Unsorted list of items.
	Returns:
        list: Sorted list of items.
	"""
	sorted_list = list(unsorted_list)
	n = len(sorted_list)
	for i in range(0, n, 1):
		for j in range(0, n - i - 1, 1):
			if sorted_list[j] > sorted_list[j + 1]:
				sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
	return sorted_list

def main(argv):
	"""Main function of the script.
	Args:
		argv (list): Contains command-line arguments passed to the script.
	Returns:
        int: Error code after execution (0 if OK).
	"""
	error_code = 0
	list = [5, 9, 8, 2, 0, 4, 7, 6, 1, 7]
	print('Unsorted list:')
	print(list)
	list = bubble_sort(list)
	print('Sorted list:')
	print(list)
	return error_code

if __name__ == '__main__':
	error_code = main(sys.argv[1:])
	print('[+] Terminated with code: ' + str(error_code))
	sys.exit(error_code)