
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
    empty_valus = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                empty_valus.append((i,j)) # (row,col)
    return empty_valus


def number_Of_squers(number): # this function is just for checking that the squer is 2*2 or 3*3 
    if number == 9:
        return 3
    elif number == 4:
        return 2

def check_validation(board,pos,valu):
    #checking rows

    # rows = board[pos[0]]
    # if valu in rows:
    #     return False

    for i in range(len(board)):
        if board[pos[0]][i] == valu:
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


## uptomize the forward checking function
def forward_checking(board):
    empty_valus = find_empty(board) ##
    domins = {}  ##
    for pos in empty_valus:
        domins[pos] = []
        # empty_valus.remove(pos)
        for i in range(1, len(board) + 1):
            if check_validation(board, pos, i):
                domins[pos].append(i)

        if domins[pos] == []:
            domins[pos].pop
    return domins

def mrv(domins):
    pos = ()
    tmp = size_Of_board + 1   # 
    for domin in domins:
        if len(domins[domin]) < tmp:
            pos = domin
            tmp = len(domins[domin])
    return pos

def solve(board):
    # pos = find_empty(board)

    domins = forward_checking(board)
    start = mrv(domins)
    if not domins:
        return True

    # for pos in domins:                  ### without MRV
    #     for i in domins[pos]:
    #         board[pos[0]][pos[1]] = i
    #         # printboard(board)
    #         # print("--------")
    #         if solve(board):
    #             return True
    #         board[pos[0]][pos[1]] = 0

    for i in domins[start]:
            board[start[0]][start[1]] = i
            # printboard(board)
            # print("--------")
            if solve(board):
                return True
            board[start[0]][start[1]] = 0
         

    return False  # this sudoku cant be solved


board = [                   #this board cant be solved
            [0, 1,  0, 4],         
            [3, 0,  1, 0],

            [0, 2,  0, 1],
            [0, 3,  0, 0]
        ]

board1 = [                  
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


board3 = [
            [3, 0, 6,   5, 0, 8,   4, 0, 0],
            [5, 2, 0,   0, 0, 0,   0, 0, 0],
            [0, 8, 7,   0, 0, 0,   0, 3, 1],

            [0, 0, 3,   0, 1, 0,   0, 8, 0],
            [9, 0, 0,   8, 6, 3,   0, 0, 5],
            [0, 5, 0,   0, 9, 0,   6, 0, 0],

            [1, 3, 0,   0, 0, 0,   2, 5, 0],
            [0, 0, 0,   0, 0, 0,   0, 7, 4],
            [0, 0, 5,   2, 0, 6,   3, 0, 0]
        ]

size_Of_board =  int(input("enter the size of sudoku : "))
squers = number_Of_squers(size_Of_board)
# domins = {} # { Pos : Domin}
# empty_valus = find_empty(board1)


printboard(board3)
#forward_checking(board2)

if solve(board3):
    print("-----Solved-Sudoku-----")
    printboard(board3)
else:
    print("board cant be solved")

