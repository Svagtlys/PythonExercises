# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that
# they will turn 100 years old.

name = input("What is your name?\n")
age = input("What is your age?\n")

if(age.isdigit()):
    age = int(age)
    year1 = 2019 - age + 99
    year2 = 2019 - age + 100
    print("Dear " + name + ", \nYou will turn 100 in either " + str(year1) + " or " + str(year2) + ".")
