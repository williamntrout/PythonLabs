"""list_mutation.py: Demonstrates the list mutation property."""

import sys
import random

__author__ = "William_Trout"
__license__ = "GPL"
__version__ = "1.0.1"
__date__ = "September 25, 2020"


def count_even(num_list):
    """Counts total of odd and even numbers in the list.
        Args:
            num_list (list): List of numbers to be checked.
         Returns:
          count: Count of odd and even numbers."""
    even_count, odd_count = 0, 0
    for num in num_list:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print("Even numbers in the lits: ", even_count)
    print("Odd numbers in the list: ", odd_count)


def has_odd(num_list):
    """Checks t0 see if there are odd numbers in the list.
        Args:
            Num_list(list): List of numbers to be checked."""
    for num in num_list:
        if num % 2 == 1:
            print("List has odd numbers.")
        break


def delete_odd(num_list):
    """Removes all odd numbers from a list of numbers.
    Args:
        num_list (list): List of numbers to be checked.
    Returns:
        list: List of numbers with all odd numbers removed.
    """
    new_list = []
    for num in num_list:
        if num % 2 == 0:
            new_list.append(num)
    return new_list


def delete_last_even(num_list):
    """Looks over list of numbers and deletes the last even number in the list.
        Args:
        num_list (list): List of numbers to be checked.
    Returns:
        list: List of numbers with the last even number removed.
    """
    rev_num = num_list[::-1]
    for num in rev_num:
        if num % 2 == 0:
            rev_num.pop(0)
            num_list = rev_num[::-1]
            return num_list


def rand_int(min, max):
    """Generates a random number within a given range.
        Args:
        min(int): Bottom of the number range.
        max(int): Top of the number range.
    Returns:
        integer: Randomly generated number.
    """
    r1 = random.randint(min, max)
    return r1


def odds_evens(num_list):
    """Looks over list of numbers and labels odd or even accordingly.
        Args:
        num_list (list): List of numbers to be checked.
    Returns:
        List: List of numbers labeled as odd or even.
    """
    for num in num_list:
        if num % 2 == 0:
            print(num, "is even")
        else:
            print(num, "is odd")


def main(argv):
    """Main function of the script.
    Args:
            argv (list): Contains command-line arguments passed to the script.
    Returns:
    int: Error code after execution (0 if OK).
    """

    error_code = 0

    # Task 2

    # count_even([7, 65, 1337, 8, -2, 24, 6, 67, 54, 36, 25, 1, 42, 9, 138, 4356, 6])

    # Task 3

    # has_odd([7, 65, 1337, 8, -2, 24, 6, 67, 54, 36, 25, 1, 42, 9, 138, 4356, 6])

    # Task 4

    # print(delete_odd([7, 56, 1337, 8, -2, 24, 6,67, 54, 36, 25, 1, 42, 9, 138, 4356, 6]))

    # Task 5

    # print(delete_last_even([7, 65, 1337, 8, -2, 24, 6, 67, 54, 36, 25, 1, 42, 9, 138, 4356, 6]))

    # Task 6

    # print(rand_int(1, 100))

    # Checking odds and evens.

    # print(odds_evens([7, 65, 1337, 8, -2, 24, 6, 67, 54, 36, 25, 1, 42, 9, 138, 4356, 6]))

    return error_code


if __name__ == '__main__':
    error_code = main(sys.argv[1:])
    print('[+] Terminated with code: ' + str(error_code))
    sys.exit(error_code)
