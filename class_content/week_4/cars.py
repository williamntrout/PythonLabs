"""cars.py: Demonstrates the concept of objects."""

import sys

__author__ 	= "Mikhail Sudakov"
__license__ = "GPL"
__version__ = "1.0.1"
__date__ 	= "October 14, 2019"

class Car:
	"""Defines the Car class."""
	def __init__(self, make, model, year, colour, odometer):
		"""Instantiates a Car object.
		Args:
			make (str): Manufacturer of the vehicle.
			model (str): Model of the vehicle.
			year (int): Year the vehicle was made.
			colour (str): Colour of the vehicle.
			odometer (int): Odometer reading of the vehicle.
		"""
		self.make = make
		self.model = model
		self.year = year
		self.colour = colour
		self.odometer = odometer
		
	def __str__(self):
		"""Gets the string representation of a Car object.
		Returns:
			str: String representation of a Car object.
		"""
		return str(self.year) + ' ' + str(self.colour) + ' ' + str(self.make) + ' ' + str(self.model)
	
	def get_make_and_model(self):
		"""Gets the make and model of a Car object.
		Returns:
			str: Make and model of a Car object.
		"""
		return str(self.make) + ' ' + str(self.model)
	
	def travel(self, distance):
		"""Updates odometer reading of a Car object.
		Args:
			distance (int): Number of units traveled.
		"""
		self.odometer += distance
	
	def get_odometer(self):
		"""Gets the current odometer reading of a Car object.
		Returns:
			int: Odometer reading of a Car object.
		"""
		return self.odometer

def main(argv):
	"""Main function of the script.
	Args:
		argv (list): Contains command-line arguments passed to the script.
	Returns:
        int: Error code after execution (0 if OK).
	"""
	error_code = 0
	
	# Instantiate three Car objects.
	car_1 = Car('Mercedes-Benz', 'AMG GT Roadster', 2019, 'Black', 100)
	car_2 = Car('Chevrolet', 'Cruze', 2018, 'Yellow', 200)
	car_3 = Car('Ford', 'Mustang', 2017, 'Brown', 300)
	
	# Print string representation of the three Car objects.
	print(str(car_1))
	print(str(car_2))
	print(str(car_3))
	
	# List of Car objects.
	cars = []
	cars.append(car_1)
	cars.append(car_2)
	cars.append(car_3)
	for car in cars:
		print(str(car) + ' (odometer reading: ' + str(car.get_odometer()) + ')')
	
	# Get the make and model of the second Car object.
	print(car_2.get_make_and_model())
	
	# Travel 500 units (km/miles/etc) on Car 1 object.
	car_1.travel(500)
	
	# Get odometer reading of the Car 1 object.
	print(car_1.get_odometer())
	
	return error_code

if __name__ == '__main__':
	error_code = main(sys.argv[1:])
	print('[+] Terminated with code: ' + str(error_code))
	sys.exit(error_code)