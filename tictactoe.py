def evaluate(board):
    # horizontal
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2]:
            if board[i][0]=='X':
                return 10
            elif board[i][0]=='O':
                return -10
    # vertical
    for j in range(3):
        if board[0][j]==board[1][j]==board[2][j]:
            if board[0][j]=='X':
                return 10
            elif board[0][j]=='O':
                return -10
    # diagonal
    if (board[0][0]==board[1][1]==board[2][2]) or (board[0][2]==board[1][1]==board[2][0]):
        if board[1][1]=='X':
                return 10
        elif board[1][1]=='O':
            return -10
    # none
    return 0

def minimax(position,depth,maximisingPlayer):
    if depth == 0 or game_over:
        return evaluate(position)
    if maximisingPlayer:
        maxEval = - float('inf')
        for child in g[position]:
           evaluation = minimax(depth-1,False)
           maxEval = max(maxEval,evaluation)
        return maxEval
    else:
        minEval = float('inf')
        for child in g[position]:
            evaluation= minimax(depth-1,True)
            minEval = min(minEval,evaluation)
        return minEval

board = [['X','X','O'],['O','_','_'],['X','O','O']]
print(evaluate(board))