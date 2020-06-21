def evaluate(board):
    # horizontal
    for r in range(3):
        if board[r][0]==board[r][1]==board[r][2]:
            if board[r][0]==PLAYER:
                return SCORE
            elif board[r][0]==OPPONENT:
                return -SCORE
    # vertical
    for c in range(3):
        if board[0][c]==board[1][c]==board[2][c]:
            if board[0][c]==PLAYER:
                return SCORE
            elif board[0][c]==OPPONENT:
                return -SCORE
    # diagonal
    if (board[0][0]==board[1][1]==board[2][2]) or (board[0][2]==board[1][1]==board[2][0]):
        if board[1][1]==PLAYER:
                return SCORE
        elif board[1][1]==OPPONENT:
            return -SCORE
    # none
    return 0

def movesRemaining(board): 
    for r in range(3):
        for c in range(3):
            if board[r][c]=='_':
                return True
    return False

def minimax(board,depth,maximisingPlayer):
    if movesRemaining(board) == False: # empty space left
        return 0
    evaluation = evaluate(board)
    if evaluation==SCORE or evaluation==-SCORE: # already in winning/losing position
        return evaluation
    if maximisingPlayer:
        evaluation -= depth # early winning
        maxEval = - float('inf') 
        for r in range(3):
            for c in range(3):
                if board[r][c]=='_':
                    board[r][c] = PLAYER
                    evaluation = minimax(board,depth+1,False) 
                    maxEval = max(maxEval,evaluation)
                    board[r][c]='_'
        return maxEval
    else:
        evaluation += depth # late losing
        minEval = float('inf')
        for r in range(3):
            for c in range(3):
                if board[r][c]=='_':
                    board[r][c] = PLAYER
                    evaluation = minimax(board,depth+1,True) 
                    minEval = min(minEval,evaluation)
                    board[r][c]='_'
        return minEval

def findOptimalMove(board):
    optimalScore = - float('inf')
    optimalPosition = (-1,-1)
    for r in range(3):
        for c in range(3):
            if board[r][c] == '_':
                board[r][c] = PLAYER
                moveScore = minimax(board,0,False)
                board[r][c] = '_'
                if moveScore > optimalScore:
                    optimalScore = moveScore
                    optimalPosition = (r,c)
    return optimalScore,optimalPosition


global PLAYER
global OPPONENT
global score
PLAYER = 'X'
OPPONENT = 'O'
SCORE = 1
boards = [
    [['X','O','X'],['O','O','X'],['_','_','_']],
    [['X','X','X'],['O','O','X'],['_','_','_']],
    [['O','_','X'],['X','_','_'],['X','O','O']]
]
for board in boards:
    for row in board:
        print(*row)
    optimalScore,optimalPosition = findOptimalMove(board)
    print('\n\tScore:',optimalScore,'Position:',optimalPosition,'\n\n')