"""FILE_NAME: CYB_500B_Lab_1"""

import sys

__author__ = "William_Trout"
__license__ = "GPL"
__version__ = "1.0.1"
__date__ = "09/01/2020"


def main(argv):
    """Main function of the script.
    Args:
            argv (list): Contains command-line arguments passed to the script.
    Returns:
    int: Error code after execution (0 if OK).
    """
    error_code = 0

    # Task #1 (1 point):
    print(type(2 - 0.5))

    # Task #2 (1 point):
    print(type(10 // 2))

    # Task #3 (1 point):
    print(type(10 / 2))

    # Task #4 (1 point):
    print(float(5))

    # Task #5 (1 point):
    print(int(5.795))

    # Task #6 (1 point):
    print(((2 - 5) ** 13 / ((157 + 594 * 7) ** 23 % 1337) - 4 ** 19) % 664)

    # Task #7 (1 point):
    print(str(5 == "5"))
    # this will return a falsey statement as the object 5 is not the same as the string of "5". it would return a true statement if we used print(str(5==5)). as that would mean the object of 5 is the same as 5.

    # Task #8 (1 point):
    x = None
    print(str(x == "None"))
    # this will return a falsey statement as the value assigned to x is None (or null or a NoneType) and cannot have a value.  to say the None is the same as (==) the string of "None" is not accurate as the the existence of the string is a value unto it's self and does not represent a null value.

    # Task #9 (2 points):
    x = True
    y = 1
    print(str(x == y))
    x = False
    print(str(x == y))
    # if the bool value passed for x is True it will return True regardless of the value of y.  Inversely, if you pass False as the value of x it will return false regardless of the value of y.

    # Task #10 (2 points):
    num_apples = 12
    num_apples += 5
    print(num_apples)
    # there are 17 apples at this point. The += operator is 'add and assign' meaning it "Adds the values on either side and assigns it to the expression on the left." basically original number of apples is 12, If we take 5 more apples and add them in and assign them to the number of apples we end up with 17 apples. Basically we took more apples and put them in the num_apples bucket.

    # Task #11 (3 points):
    # Write and run the following code... Variable my_first_name gets your first name as a string. Variable my_last_name gets your last name as a string. Execute three print statements one after another:
    my_first_name = "William"
    my_last_name = "Trout"

    # 1
    print("My first name is " + my_first_name)
    # 2
    print("My last name is " + my_last_name)
    # 3
    print("My full name is " + my_first_name + " " + my_last_name)

    # Example output:
    #

    temp_fahrenheit = 32
    temp_celsius = (temp_fahrenheit - 32) * 5.0 / 9.0
    print(str(temp_fahrenheit) + " degrees Fahrenheit is " +
          str(temp_celsius) + " degrees Celsius")

    # Task #12 (1 point):

    temp_fahrenheit = 212
    temp_celsius = (temp_fahrenheit - 32) * 5.0 / 9.0
    print(str(temp_fahrenheit) + " degrees Fahrenheit is " +
          str(temp_celsius) + " degrees Celsius")

    # 212 degrees Fahrenheit is 100.0 degrees Celsius

    # Task #13 (4 points):

    temp_celsius = 1
    temp_fahrenheit = (temp_celsius * 9.0 / 5.0) + 32
    print(str(temp_celsius) + " degrees Celsius is " +
          str(temp_fahrenheit) + " degrees Fahrenheit")

    # I basically did the previous equation in reverse. flipped the addition to subtraction and the division to multiplication of the inverse. it works but i am not sure that is the best way to do it.  It has been some time since I took algebra.

    # Task #14 (2 point):
    var = 3
    print(type(var))
    var = 3.0
    print(type(var))
    var = True
    print(type(var))
    var = 'Zombies!'
    print(type(var))
    var = None
    print(type(var))

    # What can you infer about the type of a variable at any given time with respect to the value it holds?

    #
    #

    # Task #15 (1 point):
    # Execute the following code:
    print(16 - 8 % 3)
    # Based on the order of operations, the equation will deal with the division and multiplication before it handles the addition and subtraction. In this equation, we are finding the result of 8 Mod 3 before we figure the result of the other part of the equation. Essentially we are doing 8 Mod 3 is 2 then 16 - 2 is 14.

    #

    # Task 16 (2 points):
    #  Execute the following code:
    print((16 - 8) % 3)
    print((8 - 16) % 3)

    # As you can see, modulus works differently with negative numbers... Explain why you observed that result from the second print statement.

    # Python modulo operator always returns the remainder having the same sign as the divisor. if the Modulo is a negative number, it will return a negative divisor. The inverse is also true as if the Modulo is a positive number, it will return a positive divisor.

    return error_code


if __name__ == '__main__':
    error_code = main(sys.argv[1:])
    print('[+] Terminated with code: ' + str(error_code))
    sys.exit(error_code)
