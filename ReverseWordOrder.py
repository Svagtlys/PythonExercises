# Write a program (using functions!) that asks the user for
# a long string containing multiple words. Print back to the 
# user the same string, except with the words in backwards order. 

def string_mess(words):
    #split string
    wordlist = words.split(" ")
    #reverse order
    for i in range(int(len(wordlist)/2)):
        word1 = wordlist[i]
        wordlist[i] = wordlist[len(wordlist)-1-i]
        wordlist[len(wordlist)-1-i] = word1
    #rejoin string
    return " ".join(wordlist)

print(string_mess(input("What would you like to tell me?\n")))