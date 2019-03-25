import random
import string
import os
# Create a program that will play the “cows and bulls” game with the user.
# The game works like this:
#/1. Randomly generate a 4-digit number *where each digit is unique.
#/2. Ask the user to guess a 4-digit number. 
#/3. For every digit that the user guessed correctly in the correct place,
#    they have a “cow”. 
#/4. For every digit the user guessed correctly in the wrong place,
#    they have a “bull.” 
#/5. Every time the user makes a guess, tell them how many “cows” and
#    “bulls” they have. 
#/6. Once the user guesses the correct number, the game is over. 
#/7. Keep track of the number of guesses the user makes throughout the 
#    game and tell the user at the end.
# I actually watched Etho make a version of this game in his Minecraft
# world recently.  Dunno if he ever finished it....

def isgoodnum(num):
    '''
    Takes in a number and determines if it is four in length and only contains digits
    Returns 1 if yes and 0 if no
    '''
    if len(num) == 4 and not 0 in [1 if each.isdigit() else 0 for each in num]:
        return 1
    else:
        return 0

def askforguess():
    guess = input("Please guess a four digit number.\n")
    while(not isgoodnum(guess)):
        guess = input("You must guess a four digit number.\n")
    return guess


def cowsandbulls(mynum, guess):
    #calc number of digits that overlap in mynum and guess              = overlap
    #calc number of digits that are in the same spot in mynum and guess = cows
    #calc overlap - cows                                                = bulls
    overlap = 0
    cows = 0
    bulls = 0
    for index in range(4):
        if guess[index] in mynum:
            overlap += 1
        if guess[index] == mynum[index]:
            cows += 1
    bulls = overlap - cows
    return "You have "+ "".join(["1 cow" if cows == 1 else str(cows) + "  cows"]) + " and " + "".join(["1 bull." if bulls == 1 else str(bulls) + " bulls."])


if __name__ == "__main__":
    mynum = set()
    while(len(mynum) < 4):
        mynum.add(str(random.choice(string.digits)))
    mynum = "".join(each for each in mynum)                         # mynum is saved as a string
    numguesses = 0                                                  # numguesses saved as int

    # print("My number is " + mynum) <- Tells you the number

    print("Welcome to the game of Cows and Bulls!  I have written down a number containing four unique digits, and you must guess it!")
    input("Hit enter when you're ready to start.")

    os.system('CLS')

    while(True): #Will break once player guesses correctly
        guess = askforguess()                                       # guess is saved as a string
        numguesses += 1
        if guess == mynum:
            break
        else:
            print(cowsandbulls(mynum, guess))

    if numguesses == 1:
        print("You guessed my number in only 1 guess. Sheer luck!")
    else:
        print("You guessed my number in " + str(numguesses) + " guesses.")
