def evaluate(board):
    # horizontal
    for r in range(3):
        if board[r][0]==board[r][1]==board[r][2]:
            if board[r][0]=='X':
                return 10
            elif board[r][0]=='O':
                return -10
    # vertical
    for c in range(3):
        if board[0][c]==board[1][c]==board[2][c]:
            if board[0][c]=='X':
                return 10
            elif board[0][c]=='O':
                return -10
    # diagonal
    if (board[0][0]==board[1][1]==board[2][2]) or (board[0][2]==board[1][1]==board[2][0]):
        if board[1][1]=='X':
                return 10
        elif board[1][1]=='O':
            return -10
    # none
    return 0

def gameOver():
    for r in range(3):
        for c in range(3):
            if board[r][c]=='_':
                return False
    return True

def minimax(board,depth,maximisingPlayer):
    evaluation = evaluate(board)
    if gameOver():
        return 
    if maximisingPlayer:
        maxEval = - float('inf')
        for child in g[position]:
           evaluation = minimax(depth+1,False)
           maxEval = max(maxEval,evaluation)
        return maxEval
    else:
        minEval = float('inf')
        for child in g[position]:
            evaluation= minimax(depth+1,True)
            minEval = min(minEval,evaluation)
        return minEval

def findOptimalMove():
    optimalMove = None
    for move in board:
        score = minimax()
        if score>optimalMove:
            optimalMove = score
    return optimalMove

board = [['X','O','X'],['O','O','X'],['_','_','_']]
print(evaluate(board))