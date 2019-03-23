import random
# Take two lists, say for example these two:
#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains 
# only the elements that are common between the lists 
# (without duplicates). Make sure your program works on two 
# lists of different sizes. Write this using at least one list comprehension.
#Extra:
# Randomly generate two lists to test this

a = random.sample(range(30),random.randint(5,15))
b = random.sample(range(30),random.randint(5,15))

result = [item1 for item1 in a for item2 in b if item1 == item2]
result2 = []

for i in range(len(result)):
    isfound = 0
    for j in range(i+1, len(result)):
        if result[i] == result[j]:
            isfound = 1
            break
    if isfound == 0:
        result2.append(result[i])

print(result2)