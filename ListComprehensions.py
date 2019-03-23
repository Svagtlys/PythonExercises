# Let’s say I give you a list saved in a variable:
#  a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Write one line of Python that takes this list a and
# makes a new list that has only the even elements of this list in it.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Here's my line
result = a[1:len(a):2]
# End my line, singular, only one

#I was actually very confused by this prompt, as one could interpret it three ways.
# 1. Even items in list (by testing)
# 2. Even items in this list (odd indeces)
# 3. Items at the even indeces (odd items in this list)

# Okay, so I'm gonna test it with this bit down here, but it doesn't change anything.
# I still only used one line
print(a)
print(result)
