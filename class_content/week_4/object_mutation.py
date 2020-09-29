"""object_mutation.py: Demonstrates the object mutation property."""

import sys

__author__ = "Mikhail Sudakov"
__license__ = "GPL"
__version__ = "1.0.1"
__date__ = "October 16, 2019"


class Point:
    """Defines the Point class."""

    def __init__(self, coords):
        """Instantiates a Point object.
        Args:
                coords (list): List or [x, y] point coordinates.
        """
        self.coords = list(coords)

    def __str__(self):
        """Gets the string representation of a Point object.
        Returns:
                str: String representation of a Point object.
        """
        return 'X: ' + str(self.coords[0]) + '; Y: ' + str(self.coords[1])

    def get_coord(self, idx):
        """Gets a coordinate of the Point object.
        Args:
                idx (int): Index of a coordinate to fetch:
                        0: X-coordinate;
                        1: Y-coordinate.
        Returns:
                float: A coordinate of the Point object.
        """
        return self.coords[idx]

    def set_coord(self, idx, val):
        """Updates a coordinate of the Point object.
        Args:
                idx (int): Index of a coordinate to update:
                        0: X-coordinate;
                        1: Y-coordinate.
                val (float): Value of the given coordinate.
        """
        self.coords[idx] = val


def main(argv):
    """Main function of the script.
    Args:
            argv (list): Contains command-line arguments passed to the script.
    Returns:
    int: Error code after execution (0 if OK).
    """
    error_code = 0

    coordinates = [1.0, 3.0]
    a = Point(coordinates)
    b = Point(coordinates)
    c = Point([1.0, 3.0])
    print(a)

    # set_coord(a, 0, 5.0)
    a.set_coord(0, 5.0)
    print(a.get_coord(0))
    print(b.get_coord(0))
    print(c.get_coord(0))

    return error_code


if __name__ == '__main__':
    error_code = main(sys.argv[1:])
    print('[+] Terminated with code: ' + str(error_code))
    sys.exit(error_code)
