# Create a program that asks the user for a number
# and then prints out a list of all the divisors of that number.

number = input("What number would you like to find the divisors of?\n")

if(number.isdigit()):
    number = int(number)
    divisors = []
    for x in range(1, number):
        if number % x == 0:
            divisors.append(x)

    print(divisors)
