import random
# Write a program (function!) that takes a list and returns 
# a new list that contains all the elements of the first list 
# minus all the duplicates.
# Extras:
#  Write two different functions to do this - one using
#   a loop and constructing a list, and another using sets.
#  Go back and do Exercise 5 using sets, and write the 
#   solution for that in a different function.

def remove_dupes_via_loop(mylist):
    result = []
    for i in range(len(mylist)):
        found = 0
        for j in range(i+1, len(mylist)):
            if mylist[i] == mylist[j]:
                found = 1
                break
        if not found:
            result.append(mylist[i])
    return result
        

def remove_dupes_via_set(mylist):
    return list(set(mylist))


def set_overlap(set1, set2):
    result = set()
    for elem in set1:
        if elem in set2:
            result.add(elem)

    return result

seta = set(random.sample(range(30), 15))
setb = set(random.sample(range(30), 15))
lista = random.sample(range(30), 15)

print(remove_dupes_via_loop(lista))
print(remove_dupes_via_set(lista))
print(set_overlap(seta, setb))