"""buggy_calculator.py: Simple calculator program that contains several bugs."""

import sys

__author__ = "Mikhail Sudakov"
__license__ = "GPL"
__version__ = "1.0.1"
__date__ = "November 6, 2019"


def add(x, y):
    """Computes the sum of two operands.
    Args:
        x (int): The first operand.
        y (int): The second operand.
    Returns:
        int: The result of the addition.
    """
    return x + y


def subtract(x, y):
    """Computes the difference of two operands.
    Args:
        x (int): The first operand.
        y (int): The second operand.
    Returns:
        int: The result of the subtraction.
    """
    return x - y


def multiply(x, y):
    """Computes the product of two operands.
    Args:
        x (int): The first operand.
        y (int): The second operand.
    Returns:
        int: The result of the multiplication.
    """
    return x * y


def divide(x, y):
    """Computes the division of two operands.
    Args:
        x (int): The dividend.
        y (int): The divisor.
    Returns:
        float: The result of the division.
    """
    try:
        return x / y
    except Exception as e:
        return None


def main(argv):
    """Main function of the script.
    Args:
        argv (list): Contains command-line arguments passed to the script.
    Returns:
        int: Error code after execution (0 if OK).
    """
    error_code = 0
    invalid_input_error = 'ERROR: Invalid input!\nUsage: <INT_1> <OPERATOR> <INT_2>\nValid operators: + - * /'
    if len(argv) != 3:
        print(invalid_input_error)
        error_code = 1
        return error_code
    operand_1 = operand_2 = operator = result = None
    try:
        operand_1 = int(argv[0])
        operator = argv[1]
        operand_2 = int(argv[2])
    except Exception as e:
        print('Invalid_input_error')
        error_code = 2
        return error_code

    if operator == '+':
        result = add(operand_1, operand_2)
    elif operator == '-':
        result = subtract(operand_1, operand_2)
    elif operator == '*':
        result = multiply(operand_1, operand_2)
    elif operator == '/':
        result = divide(operand_1, operand_2)
    else:
        print(invalid_input_error)
        error_code = 3
    print(str(operand_1) + ' ' + operator + ' ' +
          str(operand_2) + ' ' + ' = ' + str(result))
    return error_code


if __name__ == '__main__':
    error_code = main(sys.argv[1:])
    print('[+] Terminated with code: ' + str(error_code))
    sys.exit(error_code)
