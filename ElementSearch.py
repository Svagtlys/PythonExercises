# Write a function that takes an ordered list of numbers (a list where
# the elements are in order from smallest to largest) and another number.
# The function decides whether or not the given number is inside the list
# and returns (then prints) an appropriate boolean.
# Extras:
#  Use binary search.

def search(myset, num):
    '''
    Takes in an ordered list or set, and a number to search for
    Uses binary search to see if the number is in the list
    Return True if it is or False if it isn't
    '''
    foundnum = None
    while len(myset) >= 1: #if the halved list is over 1 and we haven't found the number we're searching for, keep searching
        foundnum = myset[int((len(myset)-1)/2)]
        if foundnum == num:
            return True
        elif(foundnum < num):
            myset = myset[int((len(myset)-1)/2)+1:len(myset)]
        else: #foundnum > num
            myset = myset[0:int((len(myset)-1)/2)]
    return False


if __name__ == "__main__":
    myseta = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    mysetb = [1, 3, 5, 30, 42, 43, 500, 700]
    num = 13
    print(search(mysetb, num))