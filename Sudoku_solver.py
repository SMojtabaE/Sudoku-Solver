
# TODO:
#     -printbored function
#     -find empty function


def printboard(board):

    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end=" ")
        print("")
        # print("-" * len(board))

def find_empty(board):

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return (i,j) # (row,col)


board = [[0,1,0,4],
         [3,0,1,0],
         [0,2,0,1],
         [0,3,0,0]]
        
