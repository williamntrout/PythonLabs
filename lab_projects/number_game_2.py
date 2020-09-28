"""guess_the_number_template.py: Guess the Number game.
	Once the game starts, the computer will randomly generate
		an integer between 0 including and 100 including. The
		player will then have seven (7) attempts to guess the
		number. After each guess, the computer will print whether
		the actual number is higher or lower than the guessed
		number. If the player guesses correctly within the 7
		allowed attempts, the player wins the game. If the player
		fails to guess correctly with the 7 attempts, the computer
		wins the game.
"""

import sys
import random

__author__ = "William_Trout"
__license__ = "GPL"
__version__ = "1.0.1"
__date__ = "Sept_19_2020"


def parse_int(guess):
    """Parses user-entered string for an integer value between
            0 including and 100 including.
    Args:
            str (string): User input gathered from command line.
    Returns:
    int: The parsed integer if the input was valid; None
                    otherwise.
    """
    try:
        guess = int(guess)
    except:
        print("Not a valid entry.")

    if not guess > 0 or not guess < 101:
        print("Number is not between 1 and 100.")


def main(argv):
    """Main function of the script.
    Args:
            argv (list): Contains command-line arguments passed to the script.
    Returns:
    int: Error code after execution (0 if OK).
    """
    error_code = 0
    # Set the maximum number of attempts allowed.
    num_guesses = 7
    # Sample a random number between 0 and 100 for computer's choice.
    secret_number = random.randrange(0, 101)
    # print(type(secret_number))
    print('Computer has picked a number... Can you guess it??')
    # While the number of attempts remaining is greater than 0, allow
    keep_playing = "True"
    # 	the player to keep guessing.
    while keep_playing == "True":
        # Get user input from console.
        guess = int(input('Pick a number between 1 and 100.'))
        # Check if input was valid.
        parse_int(guess)
        num_guesses = num_guesses - 1
        guesses_left = num_guesses
        if guess < secret_number and num_guesses > 0:
            guesses_left = str(guesses_left)
            print('Higher! You have ' + guesses_left + ' guess left.')
        if guess > secret_number and num_guesses > 0:
            guesses_left = str(guesses_left)
            print('Lower! You have ' + guesses_left + ' guess left.')
        if guess == secret_number and num_guesses > 0:
            print('Correct!')
            keep_playing = "False"
        if num_guesses == 0:
            print('You did not guess the number, the number was ' +
                  str(secret_number))
    if guess == secret_number:
        print('Player WINS!')

    return error_code


if __name__ == '__main__':
    error_code = main(sys.argv[1:])
    print('[+] Terminated with code: ' + str(error_code))
    sys.exit(error_code)
