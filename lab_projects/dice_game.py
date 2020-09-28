"""dice_game.py: Mini project for lab 4. Classes and lists"""

import sys
import random

__author__ = "William_Trout"
__license__ = "GPL"
__version__ = "1.0.1"
__date__ = "September 25, 2020"


class Dice:
    """defines the Dice class"""

    def __init__(self, side):
        """Instantiates a Dice object.
        Args:
            sides(int): Value of individual die face.
        """
        self.side = side

    def __str__(self):
        """Gets the string representation of a Die object.
        Returns:
            str: String representation of a Die object.
        """
        return str(self.side) + ' '

    def role(self, side):
        """Gets the randomized value of the dice when 'Rolled' by the player.
        Args:
            sides(int): Value of individual die face.
        Returns:
            int: result of dice role.
        """
        role_value = (random.randint(side, 6))
        return role_value


def main(argv):
    """Main function of the script.
    Args:
        argv (list): Contains command-line arguments passed to the script.
    Returns:
        int: Error code after execution (0 if OK).
    """
    error_code = 0

    # Instantiate 2 dice objects.
    die_1 = Dice(1)
    die_2 = Dice(1)

    # # Print values of die_1 and die_2
    print("Dice 1 has an initial value of: " + str(die_1))
    print("Dice 2 has an initial value of: " + str(die_2))

    # # Role die_1 and die_2

    print("On first role, Die 1 roles a: " + str(die_1.role(1)))
    print("On first role, Die 2 roles a: " + str(die_2.role(1)))

    # # Print values of die_1 and die_2
    print(str(die_1))
    print(str(die_2))

    # # Role die_1 and die_2
    print("On second role, Die 1 roles a: " + str(die_1.role(1)))
    print("On second role, Die 2 roles a: " + str(die_2.role(1)))

    # # Print out the combined value of both dice (2-12).
    print("Role 3 had a combined value of " +
          str((die_1.role(1)) + (die_2.role(1))))

    return error_code


if __name__ == '__main__':
    error_code = main(sys.argv[1:])
    print('[+] Terminated with code: ' + str(error_code))
    sys.exit(error_code)
