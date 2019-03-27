# given a 3 by 3 list of lists that represents a Tic Tac Toe game board,
# tell me whether anyone has won, and tell me which player won, if any.
# A Tic Tac Toe win is 3 in a row - either in a row, a column, or a 
# diagonal. Don’t worry about the case where TWO people have won - 
# assume that in every board there will only be one winner.

def checkforwin(matrix): #returns 1 if p1 won, 2 if p2 won, and 0 if no win
    for line in range(3):
        if matrix[line][0] == matrix[line][1] == matrix[line][2]: #test rows
            return matrix[line][0]
        elif matrix[0][line] == matrix[1][line] == matrix[2][line]: #test columns
            return matrix[0][line]
    if matrix[0][0] == matrix[1][1] == matrix[2][2]:
        return matrix[0][0]
    elif matrix[0][2] == matrix[1][1] == matrix [2][0]:
        return matrix[0][2]
    else:
        return 0
        

if __name__ == "__main__":
    winner_is_2 = [[2, 2, 0],
        [2, 1, 0],
        [2, 1, 1]]

    winner_is_1 = [[1, 2, 0],
        [2, 1, 0],
        [2, 1, 1]]

    winner_is_also_1 = [[0, 1, 0],
        [2, 1, 0],
        [2, 1, 1]]

    no_winner = [[1, 2, 0],
        [2, 1, 0],
        [2, 1, 2]]

    also_no_winner = [[1, 2, 0],
        [2, 1, 0],
        [2, 1, 0]]

    winner = checkforwin(also_no_winner)

    if winner == 0:
        print("No winner!")
    else:
        print("Player " + str(winner) + " won!")