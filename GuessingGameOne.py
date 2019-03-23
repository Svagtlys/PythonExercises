import random
import os
# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they
# guessed too low, too high, or exactly right.
# (Hint: remember to use the user input lessons from the very first exercise)

# Extras:
#  Keep the game going until the user types “exit”
#  Keep track of how many guesses the user has taken,
#  and when the game ends, print this out.

mynumber = random.randint(1, 9)
numguesses = 0

numguesses += 1
guess = input("Guess a number between 1 and 9 (including 1 and 9)\n")

while(not guess.isdigit()):
    guess = input("Please guess a number!\n")

guess = int(guess)

while(guess != mynumber):
    
    if(guess < mynumber):
        guess = input("Your guess is too low!  Guess again.\n")
        while(not guess.isdigit()):
            guess = input("Please guess a number!\n")
    else:
        guess = input("Your guess is too high!  Guess again.\n")
        while(not guess.isdigit()):
            guess = input("Please guess a number!\n")
    numguesses += 1
    guess = int(guess)

    print("You guessed my number in only " + str(numguesses) + " tries! Thanks for playing.")
