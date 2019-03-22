# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user.

number = input("Give me a whole number, any whole number!\n")

if(number.isdigit()):
    number = int(number)
    if(number % 2 is 0): #had to look up mod in python, turns out it's same as in Java
        print(str(number) + " is an even number.")
    else:
        print(str(number) + " is an even number.")
