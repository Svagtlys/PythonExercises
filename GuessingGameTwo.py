# You, the user, will have in your head a number between 0 and 100. 
# The program will guess a number, and you, the user, will say whether 
# it is too high, too low, or your number.

def guess(lastguess, answer, minim = 0, maxim = 100): #binary "search" method
    if answer == "l": #lastguess is too low
        minim = lastguess+1
    else: #lastguess is too high
        maxim = lastguess-1
    guess = int((minim + maxim)/2)

    return [guess, minim, maxim]


def ask(guess):

    guess = str(guess)

    answer = input("Is your number " + guess + "? (C)orrect, Too (L)ow, Too (H)igh\n").lower()

    while answer != "c" and answer != "l" and answer != "h":
        answer = input("I guessed " + guess + ". Type C if correct, L if too low, and H if too high.\n").lower()

    return answer


if __name__ == "__main__":
    print("Write down a whole number between 0 and 100, and I will try to guess it.  Press enter when you're ready!")
    input("Prepare yourself, mortal!\n")

    numguesses = 1
    guesslist = [50, 0, 100]
    answer = ask(guesslist[0])
    cheated = False
    
    while answer != "c":
        if guesslist[0] == guesslist[1] and guesslist[0] == guesslist[2]:
            cheated = True
            break
        guesslist = guess(guesslist[0], answer, guesslist[1], guesslist[2])
        print(guesslist[0])
        print(guesslist[1])
        print(guesslist[2])
        numguesses += 1
        answer = ask(guesslist[0])
        
    if cheated is True:
        print("What a cheater!  You changed your number.")
    else:
        print("I guessed that your number is " + str(guesslist[0]) + " in only " + str(numguesses) + " guesses!")