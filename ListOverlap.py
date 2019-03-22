# Take two lists, say for example these two:
#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only
# the elements that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

result = []

for i in a:     #take num from a
    for j in b: #take num from b
        if i == j:          #see if a and b nums are the same
            taken = 0
            for k in result: #see if num is on the results already
                if i == k:
                    taken = 1
                    break
            if not taken: #if that number isn't already
                result.append(i)
        continue

print(result)
        
