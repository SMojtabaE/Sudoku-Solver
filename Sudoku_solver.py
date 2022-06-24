
# TODO:
#     -printbored function
#     -find empty function

def printboard(board):

    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end=" ")
        print("")

def find_empty(board):

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return (i,j) # (row,col)


def number_Of_squers(number): # this function is just for checking that the squer is 2*2 or 3*3 
    if number == 9:
        return 3
    elif number == 4:
        return 2

def check_validation(pos,valu):
    #checking rows
    rows = board[pos[0]]
    if valu in rows:
        return False

    #checking col
    for i in range(len(board)):
        if board[i][pos[1]] == valu:
            return False
    
    #checking Squers
    starting_row = (pos[0] // squers) * squers
    starting_col = (pos[1] // squers) * squers

    for i in range(starting_row,starting_row + squers):
        for j in range(starting_col,starting_col + squers): 
            if board[i][j] == valu:
                return False
    return True


board = [[0,1,0,4],
         [3,0,1,0],
         [0,2,0,1],
         [0,3,0,0]]

size_Of_board =  int(input("enter the size of sudoku : "))
squers = number_Of_squers(size_Of_board)
# print(squers)

# printboard(board)

# for i in range(len(board)):
#     print(check_validation((0,0),i+1))