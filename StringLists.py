# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

string = input("Give me a word to test.\n")

if string[0:int(len(string)/2)].lower() == string[len(string):int((len(string)-1)/2):-1].lower():
    print(string + " is a palindrome.")
else:
    print(string + " is not a palindrome.")
