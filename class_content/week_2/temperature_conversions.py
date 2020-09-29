"""temperature_conversions.py: Contains functions to convert between
	different temperature scales.
"""

import sys

__author__ = "Mikhail Sudakov"
__license__ = "GPL"
__version__ = "1.0.1"
__date__ = "October 1, 2019"


def fahrenheit_to_celsius(temp_fahrenheit):
    """Converts degrees Fahrenheit to degrees Celsius.
    Args:
            temp_fahrenheit (float): Temperature in Fahrenheit.
    Returns:
    float: Temperature in Celsius.
    """
    temp_celsius = (temp_fahrenheit - 32) * 5.0 / 9.0
    return temp_celsius


def celsius_to_fahrenheit(temp_celsius):
    """Converts degrees Celsius to degrees Fahrenheit.
    Args:
            temp_celsius (float): Temperature in Celsius.
    Returns:
    float: Temperature in Fahrenheit.
    """
    temp_fahrenheit = 9.0 / 5.0 * temp_celsius + 32
    return temp_fahrenheit


def fahrenheit_to_kelvin(temp_fahrenheit):
    """Converts degrees Fahrenheit to degrees Kelvin.
    Args:
            temp_fahrenheit (float): Temperature in Fahrenheit.
    Returns:
    float: Temperature in Kelvin.
    """
    temp_celsius = fahrenheit_to_celsius(temp_fahrenheit)
    temp_kelvin = temp_celsius + 273.15
    return temp_kelvin


def main(argv):
    """Main function of the script.
    Args:
            argv (list): Contains command-line arguments passed to the script.
    Returns:
    int: Error code after execution (0 if OK).
    """
    error_code = 0
    print(fahrenheit_to_celsius(212))
    print(celsius_to_fahrenheit(0))
    print(fahrenheit_to_kelvin(212))
    return error_code


if __name__ == '__main__':
    error_code = main(sys.argv[1:])
    print('[+] Terminated with code: ' + str(error_code))
    sys.exit(error_code)
