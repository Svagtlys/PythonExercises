# Ask the user for a number and 
# determine whether the number is prime or not.

def get_num():
    number = input("What number would you like to determine the primality of?\n")
    while(not number.isdigit()):
        number = input("Please provide a number to determine the primality of?\n")
    return int(number)

def check_divisible(num):
    for x in range(2, num-1):
        if num % x == 0:
            return x
    return 0

number = get_num()
isdivisible = check_divisible(number)

if(not isdivisible):
    print(str(number) + " is prime.")
if(isdivisible):
    print(str(number) + " is not prime. The first divisor for it (other than 1) is " + str(isdivisible) + ".")