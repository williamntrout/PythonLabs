"""inheritance.py: Demonstrates class inheritance."""

import sys

__author__ 	= "Mikhail Sudakov"
__license__ = "GPL"
__version__ = "1.0.1"
__date__ 	= "October 29, 2019"

class Person:
	"""Defines the Person class."""
	def __init__(self, first_name, last_name):
		"""Instantiates a Person object.
		Args:
			first_name (str): Person's first name.
			last_name (str): Person's last name.
		"""
		self.first_name = first_name
		self.last_name = last_name
		
	def __str__(self):
		"""Gets the string representation of a Person object.
		Returns:
			str: String representation of a Person object.
		"""
		return 'FIRST NAME: ' + str(self.first_name) + '\nLAST NAME: ' + str(self.last_name)
	
	def get_full_name(self):
		"""Gets person's full name.
		Returns:
			str: Person's full name.
		"""
		return self.first_name + ' ' + self.last_name

class Student(Person):
	"""Defines the Student class."""	
	def __init__(self, first_name, last_name, grade):
		"""Instantiates a Student object.
		Args:
			first_name (str): Student's first name.
			last_name (str): Student's last name.
			grade (str): Student's initial grade letter.
		"""
		# The super() method makes the child class inherit all methods from the parent class,
		# 	but, without having to reference the parent class by name.
		super().__init__(first_name, last_name)
		# After inheriting all the properties of the parent class, the child class might
		#	have some properties of its own.
		self.grade = grade
	
	def __str__(self):
		"""Gets the string representation of a Student object.
		Returns:
			str: String representation of a Student object.
		"""
		return 'FIRST NAME: ' + str(self.first_name) + '\nLAST NAME: ' + str(self.last_name) + '\nGRADE: ' + str(self.grade)
	
	def set_grade(self, new_grade):
		"""Updates student's grade.
		Args:
			new_grade (str): New grade letter.
		"""
		self.grade = new_grade
	
def main(argv):
	"""Main function of the script.
	Args:
		argv (list): Contains command-line arguments passed to the script.
	Returns:
        int: Error code after execution (0 if OK).
	"""
	error_code = 0
	# Create a Person object.
	per = Person('John', 'Doe')
	# Print the Person object.
	print('Printing Person object:')
	print(per)
	print('------------------------------')
	print('Printing Person\'s full name: ' + per.get_full_name())
	print('------------------------------')
	# Create a Student object that is also a Person.
	stu = Student('John', 'Doe', 'F')
	# Print the Student object.
	print('Printing Student object:')
	print(stu)
	print('------------------------------')
	print('Printing Student\'s full name: ' + stu.get_full_name())
	print('------------------------------')
	# Assign new grade and re-print the Student object.
	stu.set_grade('A')
	print('Printing Student object:')
	print(stu)
	print('------------------------------')
	# Person class does not have the set_grade method!
	# per.set_grade('A')
	return error_code

if __name__ == '__main__':
	error_code = main(sys.argv[1:])
	print('[+] Terminated with code: ' + str(error_code))
	sys.exit(error_code)