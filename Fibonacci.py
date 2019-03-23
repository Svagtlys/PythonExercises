# Write a program that asks the user how many Fibonnaci 
# numbers to generate and then generates them. Take this 
# opportunity to think about how you can use functions. 
# Make sure to ask the user to enter the number of numbers 
# in the sequence to generate

def gen_fib(length, mylist = []):
    if(len(mylist) < 2):
        mylist.append(1)
    else:
        mylist.append(mylist[len(mylist)-1] + mylist[len(mylist)-2])

    if(len(mylist) == length):
        return mylist
    else:
        return gen_fib(length, mylist)

print(gen_fib(int(input("How many numbers of the Fibonacci sequence would you like to generate?\n"))))