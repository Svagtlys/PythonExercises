# Ask the user what size game board they want to draw, and draw
# it for them to the screen using Python’s print statement.

def build_board(width, height):
    '''
    Takes in the width and height of the game board
    Returns a string containing a faux-graphical board
    '''

    outputrows = ["" for each in range(height*2+1)]

    for row in range(len(outputrows)): #2 parts to each board row: mid and bottom, except first row has top
        for column in range(width*4+1):# 4 parts to each board column, midleft, mid, midright, right, except first colomn has left
            if column%4 != 0 and row%2 == 0:#if column# is not 0,4,8, etc && row# is even, add "-" (ZERO INDEX)
                outputrows[row] += "-"
            elif column%4 == 0 and row%2 == 1: # if column# is 0,4,8, etc && row is odd, add a "|"
                outputrows[row] += "|"
            else:
                outputrows[row] += " "

    return "\n".join(outputrows)


if __name__ == "__main__":
    print(build_board(3,3))