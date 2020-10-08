"""private_variables.py: Demonstrates properties of public and private
		class variables.
"""

import sys

__author__ 	= "Mikhail Sudakov"
__license__ = "GPL"
__version__ = "1.0.1"
__date__ 	= "November 1, 2019"

class Person:
	"""Defines the Person class."""
	def __init__(self, first_name, last_name):
		"""Instantiates a Person object.
		Args:
			first_name (str): Person's first name.
			last_name (str): Person's last name.
		"""
		self.__first_name = first_name
		self.last_name = last_name		# Public internal variable
		# self.__last_name = last_name		# Private internal variable
		
	def __str__(self):
		"""Gets the string representation of a Person object.
		Returns:
			str: String representation of a Person object.
		"""
		return 'FULL NAME: ' + str(self.__first_name) + ' ' + str(self.last_name)
		# return 'FULL NAME: ' + str(self.__first_name) + ' ' + str(self.__last_name)
	
	def change_last_name(self, new_lname):
		"""Updates person's last name.
		Args:
			new_lname (str): New last name.
		"""
		self.last_name = new_lname
		# self.__last_name = new_lname
	
def main(argv):
	"""Main function of the script.
	Args:
		argv (list): Contains command-line arguments passed to the script.
	Returns:
        int: Error code after execution (0 if OK).
	"""
	error_code = 0
	
	person_1 = Person('John', 'Doe')
	print(person_1)
	person_1.change_last_name('Smith')
	print(person_1)
	person_1.last_name = 'Shmoe'
	# person_1.__last_name = 'Shmoe'
	print(person_1)
	
	return error_code

if __name__ == '__main__':
	error_code = main(sys.argv[1:])
	print('[+] Terminated with code: ' + str(error_code))
	sys.exit(error_code)