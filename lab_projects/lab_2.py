"""CYB-500B-71L01-20FA, lab_2"""

import sys

__author__ = "William_Trout"
__license__ = "GPL"
__version__ = "1.0.1"
__date__ = "TODAY'S DATE"


def triangle_area(base, height):
    """Computes the area of a triangle.
    Args:
            base (float): Base of the triangle.
            height (float): Height of the triangle.
    Returns:
    float: Area of the triangle.
    """
    area = 0.5 * base * height
    return area


def cube_volume(side):
    """Computes the volume of a cube.
    Args:
            side (float): Length of the cube's side.
    Returns:
    float: Volume of the cube.
    """
    volume = 6.0 * side ** 2
    return volume


def inch_to_centimeter(len_inch):
    """Converts length unit of inches into centimeters.
    Args:
            len_inch (float): Length in inches.
    Returns:
    float: Length in centimeters.
    """
    length = len_inch * 2.54
    return length


def kilogram_to_pound(mass_kilogram):
    """Converts mass unit of kilograms into pounds.
    Args:
            mass_kilogram (float): Mass in kilograms.
    Returns:
    float: Mass in pounds.
    """
    weight = mass_kilogram * 2.2046
    return weight


def kmh_to_mph(speed_kmh):
    """Converts speed unit of kilometers per hour into
            miles per hour.
    Args:
            speed_kmh (float): Speed in kilometers per hour.
    Returns:
    float: Speed in miles per hour.
    """
    velocity = speed_kmh * 1.60934
    return velocity


def is_leap_year(year):
    """Checks whether a given year is a leap year.
    Args:
            year (int): Year to check for leap year.
    Returns:
    bool: True if the year is a leap year; false otherwise.
    """
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False


def is_valid_date(day, month, year):
    """Checks whether a given date is valid.
    Args:
            day (int): Day part of the date.
            month (int): Month part of the date.
            year (int): Year part of the date.
    Returns:
    bool: True if the date is valid; false otherwise.
    """
    if month == 1 or month == 3 or month == 5 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        max_day_value = 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        max_day_value = 30
    elif year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        max_day_value = 29
    else:
        max_day_value = 28

    if month < 1 or month > 12:
        return False
    elif day < 1 or day > max_day_value:
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
    print(triangle_area(3, 8))
    print(cube_volume(2))
    print(inch_to_centimeter(2))
    print(kilogram_to_pound(80))
    print(kmh_to_mph(120))
    print(is_leap_year(1400))
    print(is_leap_year(1600))
    print(is_leap_year(2020))
    print(is_leap_year(1998))
    print(is_valid_date(31, 4, 2019))
    print(is_valid_date(25, 13, 2019))
    print(is_valid_date(29, 2, 2019))
    print(is_valid_date(29, 2, 1400))

    return error_code


if __name__ == '__main__':
    error_code = main(sys.argv[1:])
    print('[+] Terminated with code: ' + str(error_code))
    sys.exit(error_code)
