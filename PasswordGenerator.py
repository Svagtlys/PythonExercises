import random
import string

# Write a password generator in Python. Be creative with how you 
# generate passwords - strong passwords have a mix of lowercase 
# letters, uppercase letters, numbers, and symbols. The passwords 
# should be random, generating a new password every time the user
# asks for a new password. Include your run-time code in a main method.
# Extra:
#  Ask the user how strong they want their password to be. 
#  For weak passwords, pick a word or two from a list.

def weak(): #pick from word list
    return random.choice(['strange','disgusting','chivalrous','decide','loud','vivacious','love','toothpaste','steal','defeated','wood','claim'])

def passgen(strength): #generator
    '''
    Takes in strength as an int defining how many characters to generate for the password.
    Returns a result containing the defined number of psuedo-randomly generated characters.
    '''
    password = ''
    max = 2
    for i in range(strength):
        chartype = random.randint(0,max) #0 = num, 1 = letter, 2 = specialchar
        if chartype == 0:
            password += random.choice(string.digits) #this was randint(0,9), but when I was looking for the letters and punctuation, I found this, so
        elif chartype == 1:
            password += random.choice(string.ascii_letters)
        else:
            password += random.choice(string.punctuation)
            max = 1 #I got tired of all special chars
    return password

# apparently this is a python main function
if __name__ == '__main__': 
    # I looked it up, apparently __name__ is a variable
    # the file has set to its name, until it's executed,
    # then its name is '__main__', so this here is asking
    # if the file is being executed, essentially. Smart

    stronglength = 16
    mediumlength = 8

    #first, ask for strength
    #Two methods, weak and other: 
    # weak will pick from word list
    # other has random gen, which picks length depending on med or strong
    strength = input("What strength do you want your password to be? (S)trong, (M)edium, (W)eak\n").lower()
    while(strength != "s" and strength != "m" and strength != "w"):
        strength = input("Please type s for strong, m for medium, or w for weak.\n").lower()

    if(strength == "w"):
        print("Your weak password is: " + weak())
    elif(strength == "m"):
        print("Your medium password is: " + passgen(mediumlength))
    else:
        print("Your strong password is: " + passgen(stronglength))