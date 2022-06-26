
# TODO:
#     -printbored function      DONE
#     -find empty function      DONE
#     -check validation         DONE
#     -Backtracking             DONE
#     -forward checking         DONE
#     -mrv                      DONE
#     -degreee                  DONE

def number_Of_squers(number): # this function is just for checking that the squer is 2*2 or 3*3 
    if number == 9:
        return 3
    elif number == 4:
        return 2




def printboard(board):          # print board like sudoku

    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end=" ")
        print("")

def find_empty(board):          # find the empty positions in board(the positions that are 0),and return an arry of positions
    empty_valus = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                empty_valus.append((i,j)) # (row,col)
    return empty_valus


def check_validation(board,pos,valu):           # checks if a number is valid in position
    #checking rows
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

    for i in range(starting_row,starting_row + squers):
        for j in range(starting_col,starting_col + squers): 
            if board[i][j] == valu:
                return False
    return True

def forward_checking(board):                    # find the domins of a position
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

def degree(poses,board):  # [(2,1),(3,0)]           # gets an array of positions and return the position that has most rilation
    sum = {}
    count = 0
    #checking row
    for pos in poses:
        for a in range(len(board)):
            if board[pos[0]][a] == 0:
                count += 1
        sum[pos] = count
        count = 0

    #checking col
    for pos in poses:
        for j in range(len(board)):
            if board[j][pos[1]] == 0:
                sum[pos] += 1
    
    #checking Squers
    for pos in poses:
        starting_row = (pos[0] // squers) * squers
        starting_col = (pos[1] // squers) * squers

        for i in range(starting_row,starting_row + squers):
            for j in range(starting_col,starting_col + squers): 
                if board[i][j] == 0:
                    sum[pos] += 1

    result = ()
    for pos in sum:             # sum = {(0,0) : 5, (1,2) : 8}
        if sum[pos] > count:
            count = sum[pos]
            result = pos
    
    return result


def mrv(domins,board):              # finds the position that has less domin
    poses = []
    tmp = size_Of_board + 1   # for 9*9 tmp is 9 and in this case evrithing is less than this number 
    for domin in domins:
        if len(domins[domin]) == tmp:
            poses.append(domin)
        elif len(domins[domin]) < tmp:
            poses.clear()
            poses.append(domin)
            tmp = len(domins[domin])
    
    if len(poses) > 1 :
        return degree(poses,board)
    
    return poses.pop()


def solve(board):               # solve the problem by backtracking

    domins = forward_checking(board)
    if not domins:
        return True
    start = mrv(domins,board)
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
            if solve(board):
                return True
            board[start[0]][start[1]] = 0
         

    return False  # this sudoku cant be solved


board0 = [                   #this board cant be solved
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


board3 = [                                          # TEST CASE 
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


board4 = [
            [0, 0, 0,   0, 0, 0,   0, 0, 0],
            [0, 0, 0,   0, 0, 0,   0, 0, 0],
            [0, 0, 0,   0, 0, 0,   0, 0, 0],

            [0, 0, 0,   0, 0, 0,   0, 0, 0],
            [0, 0, 0,   0, 0, 0,   0, 0, 0],
            [0, 0, 0,   0, 0, 0,   0, 0, 0],

            [0, 0, 0,   0, 0, 0,   0, 0, 0],
            [0, 0, 0,   0, 0, 0,   0, 0, 0],
            [1, 0, 2,   0, 0, 0,   0, 0, 0]
        ]


boardtest = board3
size_Of_board =  len(boardtest)
squers = number_Of_squers(size_Of_board)

printboard(boardtest)

if solve(boardtest):
    print("-----Solved-Sudoku-----")
    printboard(boardtest)
else:
    print("board cant be solved")

