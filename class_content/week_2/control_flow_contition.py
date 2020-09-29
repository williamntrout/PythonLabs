"""control_flow_condition.py: Demonstrates conditional flow of control.
"""

import sys

__author__ = "Mikhail Sudakov"
__license__ = "GPL"
__version__ = "1.0.1"
__date__ = "October 3, 2019"


def atm(pin, amount):
    """Simulates an automated teller machine (ATM).
    Args:
            pin (str): User's PIN code.
            amount (float): Requested withdrawal amount.
    Returns:
    float: Amount withdrawn from account.
    """
    correct_pin = '1234'
    withdrawal_limit = 100
    withdrawn_money = 0.0
    if pin != correct_pin:
        print('Incorrect pin...')
    elif amount > withdrawal_limit:
        print('Withdrawal limit exceeded...')
    else:
        print('Withdrawal successful!')
        withdrawn_money = amount
    return withdrawn_money


def main(argv):
    """Main function of the script.
    Args:
            argv (list): Contains command-line arguments passed to the script.
    Returns:
    int: Error code after execution (0 if OK).
    """
    error_code = 0
    money = atm('1337', 150.0)
    print('Money withdrawn: $' + str(money))
    money = atm('1337', 50.0)
    print('Money withdrawn: $' + str(money))
    money = atm('1234', 150.0)
    print('Money withdrawn: $' + str(money))
    money = atm('1234', 50.0)
    print('Money withdrawn: $' + str(money))
    return error_code


if __name__ == '__main__':
    error_code = main(sys.argv[1:])
    print('[+] Terminated with code: ' + str(error_code))
    sys.exit(error_code)
