# Guess the Number Game

# The import random statement imports the random module, which is used to generate a random number.
# The generate_random_number() function generates a random number between 1 and 100 using the random.randint()
# function, and returns the generated number. The get_user_input() function prompts the user to enter a number,
# and returns the user's input as an integer. If the user enters something that is not a number, the function will
# print an error message and prompt the user to enter a number again. The check_user_input() function takes two arguments:
# the user's input and the random number generated by the program. The function compares the user's input to the random
# number, and returns True if the user's input is equal to the random number, False if the user's input is too high, or
# False if the user's input is too low. The function also prints a message to give the user feedback on their guess.
# The validate_user_input() function takes the user's input as an argument, and checks if the input is within the range
# of 1 to 100. If the input is within the range, the function returns True. If the input is outside the range, the function
# prints an error message and returns False. The main() function is the main part of the program. It generates a random
# number using the generate_random_number() function, and prompts the user to guess the number. It then uses a while loop
# to repeatedly prompt the user to guess the number until the user guesses the correct number. The function calls the
# get_user_input() function to get the user's input, and then calls the validate_user_input() function to check if the input
# is valid. If the input is valid, the function calls the check_user_input() function to check if the user's guess is correct.
# If the user's guess is correct, the function breaks out of the while loop and the game ends.

# Example: Guess the Number Game
# This program generates a random number between 1 and 100, and prompts the user to guess the number. The program gives the user feedback on their guess, and prompts the user to guess again until the user guesses the correct number.
# Guess a number between 1 and 100!
# Guess the number: 50
# Your guess is too high!
# Guess the number: 25
# Your guess is too low!
# Guess the number: 37
# Your guess is too high!
# Guess the number: 31
# Your guess is too high!
# Guess the number: 28
# Your guess is too high!
# Guess the number: 26
# Your guess is too low!
# Guess the number: 27
# You guessed the number!

import random

# Generates a random number between 1 and 100
def generate_random_number():
    # The random.randint() function generates a random number between 1 and 100
    return random.randint(1, 100)

# Prompts the user to enter a valid number
def get_user_input():
    # try-except statement is used to catch errors, more specifically, non-integer inputs
    try:
        user_input = int(input("Guess the number: "))
    except:
        print("Your guess is not a number!")
        print("Please try again!")
        # Re-prompts the user to enter a valid number
        get_user_input()

# Checks if the user's input is within the range of 1 to 100
def validate_user_input(user_input):
    if user_input < 1 or user_input > 100:
        print("Your guess is out of range!")
        return False
    else:
        return True

# Checks if the user's guess is correct
def check_user_input(user_input, random_number):
    # Compares the user's input to the random number
    if user_input == random_number:
        print("You guessed the number!")
        return True
    elif user_input > random_number:
        print("Your guess is too high!")
        return False
    else:
        print("Your guess is too low!")
        return False

# The main function
def main():
    # Generates a random number
    random_number = generate_random_number()
    print("Guess a number between 1 and 100!")
    # Repeatedly prompts the user to guess the number until the user guesses the correct number
    while True:
        user_input = get_user_input()
        # Checks if the user's input is valid
        if validate_user_input(user_input) == True:
            # Checks if the user's guess is correct
            if check_user_input(user_input, random_number):
                break

# Calls the main function, to start the program
main()

# Here are some examples:

# Example 1:
# Guess a number between 1 and 100!
# Guess the number: 50
# Your guess is too high!
# Guess the number: 30
# Your guess is too low!
# Guess the number: 40
# Your guess is too low!
# Guess the number: 45
# Your guess is too low!
# Guess the number: 48
# Your guess is too high!
# Guess the number: 46
# You guessed the number!

# Example 2:
# Guess a number between 1 and 100!
# Guess the number: 76
# Your guess is too high!
# Guess the number: 43
# Your guess is too low!
# Guess the number: 60
# Your guess is too high!
# Guess the number: 52
# Your guess is too low!
# Guess the number: 56
# You guessed the number!

# Example 3:
# Guess a number between 1 and 100!
# Guess the number: 53
# Your guess is too low!
# Guess the number: 80
# Your guess is too low!
# Guess the number: 90
# Your guess is too low!
# Guess the number: 95
# Your guess is too low!
# Guess the number: 98
# Your guess is too high!
# Guess the number: 96
# You guessed the number!

# Example 4:
# Guess a number between 1 and 100!
# Guess the number: 39
# Your guess is too high!
# Guess the number: 20
# Your guess is too high!
# Guess the number: 10
# Your guess is too high!
# Guess the number: 5
# Your guess is too low!
# Guess the number: 7
# You guessed the number!
