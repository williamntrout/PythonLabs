"""quick_sort.py: Demonstrates the Quicksort algorithm."""

import sys

__author__ 	= "Mikhail Sudakov"
__license__ = "GPL"
__version__ = "1.0.1"
__date__ 	= "October 28, 2019"

def quick_sort(unsorted_list):
	"""Sorts a list of items with the Quicksort algorithm.
	Args:
		unsorted_list (list): Unsorted list of items.
	Returns:
        list: Sorted list of items.
	"""
	sorted_list = list(unsorted_list)
	less = []
	equal = []
	greater = []
	if len(sorted_list) > 1:
		pivot = sorted_list[0]
		for item in sorted_list:
			if item < pivot:
				less.append(item)
			elif item == pivot:
				equal.append(item)
			elif item > pivot:
				greater.append(item)
		return quick_sort(less) + equal + quick_sort(greater)
	else:
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
	list = quick_sort(list)
	print('Sorted list:')
	print(list)
	return error_code

if __name__ == '__main__':
	error_code = main(sys.argv[1:])
	print('[+] Terminated with code: ' + str(error_code))
	sys.exit(error_code)