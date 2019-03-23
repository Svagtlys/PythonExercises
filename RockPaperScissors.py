import os
# Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), compare them,
# print out a message of congratulations to the winner,
# and ask if the players want to start a new game)

# Remember the rules:
#  Rock beats scissors
#  Scissors beats paper
#  Paper beats rock

print("Welcome to \"Rock, Paper, Scissors\"!\nYou know the rules:\nRock beats scissors\nScissors beats paper\nPaper beats rock.")

playing = 1

score1 = 0
score2 = 0

while(playing):
    
    play1 = input("Player 1, choose wisely! (R/P/S)\n").lower()
    while(play1 != "r" and play1 != "p" and play1 != "s"):
        play1 = input("Please choose one of these options: (R/P/S)\n").lower()
    os.system('CLS')
    play2 = input("Player 2, choose wisely! (R/P/S)\n").lower()
    while(play2 != "r" and play2 != "p" and play2 != "s"):
        play2 = input("Please choose one of these options: (R/P/S)\n").lower()
    os.system('CLS')

    if play1 == play2:
        print("You have tied! You both chose " + play1 + ".")

    elif play1 == "r":
        if play2 == "s":
            print("Player 1 has won! They chose rock, while P2 chose scissors.")
            score1 += 1
        else:
            print("Player 2 has won! They chose paper, while P1 chose rock.")
            score2 += 1
    elif play1 == "p":
        if play2 == "r":
            print("Player 1 has won! They chose paper, while P2 chose rock.")
            score1 += 1
        else:
            print("Player 2 has won! They chose scissors, while P1 chose paper.")
            score2 += 1
    elif play1 == "s":
        if play2 == "p":
            print("Player 1 has won! They chose scissors, while P2 chose paper.")
            score1 += 1
        else:
            print("Player 2 has won! They chose rock, while P1 chose scissors.")
            score2 += 1
    answer = input("Would you like to play again? (Y/N)\n").lower()
    if answer == "y":
        os.system('CLS')
        continue;
    else:
        break

os.system('CLS')
print("The final score was:\nP1: " + str(score1) + "\nP2: "+ str(score2) +"\n\nThank you for playing!")
