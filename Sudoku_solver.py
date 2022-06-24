
# TODO:
#     -printbored function      DONE
#     -find empty function      DONE
#     -check validation         DONE
#     -Backtracking             DONE
#     -forward checking
#     -mrv
#     -degreee


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
    return None


def number_Of_squers(number): # this function is just for checking that the squer is 2*2 or 3*3 
    if number == 9:
        return 3
    elif number == 4:
        return 2

def check_validation(board,pos,valu):
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

    #checking the squer
    for i in range(starting_row,starting_row + squers):
        for j in range(starting_col,starting_col + squers): 
            if board[i][j] == valu:
                return False
    return True

def solve(board):
    pos = find_empty(board)
    if not pos:
        return True
    
    for i in range(1,size_Of_board+1):
        if check_validation(board,pos,i):
            board[pos[0]][pos[1]] = i

            if solve(board):
                return True

            board[pos[0]][pos[1]] = 0

    return False  # this sudoku cant be solved


board = [                   #this board cant be solved
            [0, 1,  0, 4],         
            [3, 0,  1, 0],

            [0, 2,  0, 1],
            [0, 3,  0, 0]
        ]

board1 = [                   #this board cant be solved
            [3, 4,  1, 0],         
            [0, 2,  0, 0],
            
            [0, 0,  2, 0],
            [0, 1,  4, 3]
        ]

board2 = [
            [3, 9, 0,   0, 5, 0,   0, 0, 0],
            [0, 0, 0,   2, 0, 0,   0, 0, 5],
            [0, 0, 0,   7, 1, 9,   0, 8, 0],

            [0, 5, 0,   0, 6, 8,   0, 0, 0],
            [2, 0, 6,   0, 0, 3,   0, 0, 0],
            [0, 0, 0,   0, 0, 0,   0, 0, 4],

            [5, 0, 0,   0, 0, 0,   0, 0, 0],
            [6, 7, 0,   0, 0, 5,   0, 4, 0],
            [0, 0, 9,   0, 0, 0,   2, 0, 0]
        ]

size_Of_board =  int(input("enter the size of sudoku : "))
squers = number_Of_squers(size_Of_board)


printboard(board1)

if solve(board1):
    print("-----Solved-Sudoku-----")
    printboard(board1)
else:
    print("board cant be solved")

