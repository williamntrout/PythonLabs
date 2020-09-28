"""rpsls_template.py: Rock-Paper-Scissors-Lizard-Spock game.
	"Oh, it's very simple. Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard,
		Lizard poisons Spock, Spock smashes Scissors, Scissors decapitates Lizard,
		Lizard eats Paper, Paper disproves Spock, Spock vaporizes Rock,
		and, as it always has, Rock crushes Scissors" - Dr. Sheldon Cooper.
	The approach you will use is to equate the choice strings of "Rock",
		"Paper", "Scissors", "Lizard", and "Spock" to numbers as follows:
		0: Rock
		1: Spock
		2: Paper
		3: Lizard
		4: Scissors
	Then, you will be able to determine who wins a round by the difference of choices
		and modular arithmetic.
"""

import sys
import random

__author__ = "William_Trout"
__license__ = "GPL"
__version__ = "1.0.1"
__date__ = "TODAY'S DATE"


def choice_to_number(choice):
    """Converts choice into number.
    Args:
            choice (str): Given game choice.
    Returns:
            int: Associated number for the given choice.
    """
    if choice == "rock":
        return 0
    elif choice == "spock":
        return 1
    elif choice == "paper":
        return 2
    elif choice == "lizard":
        return 3
    elif choice == "scissors":
        return 4
    else:
        return None


def number_to_choice(number):
    """Converts number into choice.
    Args:
            number (int): Given game number.
    Returns:
            str: Associated choice for the given number.
    """
    if number == 0:
        return "rock"
    elif number == 1:
        return "spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return None


def rpsls(player_number, comp_number):
    """Plays Rock-Paper-Scissors-Lizard-Spock game between player and computer.
    Args:
            player_number (int): Player's choice converted into number.
            comp_number (int): Computer's choice converted into number.
    Returns:
            bool: True if player wins the round; False if computer wins the round;
                    None otherwise.
    """
    number_diff = (player_number - comp_number) % 5

    if number_diff >= 1 and number_diff <= 2:
        return True
    elif number_diff > 2:
        return False
    else:
        return None


def main(argv):
    """Main function of the script.
    Args:
            argv (list): Contains command-line argumentsed to the script.
    Returns:
            int: Error code after execution (0 if OK).
    """
    error_code = 0
    # Get player's choice from command line.
    player_choice = input(
        'Choose between "Rock", "Paper", "Scissors", "Lizard", or "Spock": >>> ')
    # Normalize player's input.
    player_choice = player_choice.lower().replace('"', '')
    # If player's choice is not valid, display error message and set error code.
    if player_choice not in ['rock', 'paper', 'scissors', 'lizard', 'spock']:
        print('ERROR: Invalid choice!')
        print('Valid choices are "Rock", "Paper", "Scissors", "Lizard", or "Spock"')
        print('Try again...')
        error_code = 1
    # If error code has not been set, play the game.
    if error_code == 0:
        # Sample a random number between 0 and 4 for computer's choice.
        comp_number = random.randrange(0, 5)

        # Convert player's choice into number.
        player_number = choice_to_number(player_choice)

        # Convert computer's number into choice.
        comp_choice = number_to_choice(comp_number)

        # Play Rock-Paper-Scissors-Lizard-Spock
        round_result = rpsls(player_number, comp_number)

        # Print out the choices of the player and the computer.
        print("Player Choses: " + player_choice.upper())
        print("Computer Choses: " + comp_choice.upper())

        # Print out the result of the game round.
        if round_result is None:
            print("Player and computer Tie!")
        elif round_result is True:
            print("Player WINS!")
        else:
            print("Computer WINS, You LOSE!")
    return error_code


if __name__ == '__main__':
    error_code = main(sys.argv[1:])
    print('[+] Terminated with code: ' + str(error_code))
    sys.exit(error_code)
