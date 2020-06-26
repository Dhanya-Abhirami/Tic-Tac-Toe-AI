from copy import deepcopy

def movesRemaining(board): 
    for r in range(3):
        for c in range(3):
            if board[r][c]=='_':
                return True
    return False

def checkWinner(board):
    # horizontal
    for r in range(3):
        if board[r][0]!='_' and board[r][0]==board[r][1]==board[r][2]:
            return board[r][0]
    # vertical
    for c in range(3):
        if board[0][c]!='_' and board[0][c]==board[1][c]==board[2][c]:
            return board[0][c]
    # diagonal
    if board[1][1]!='_' and ((board[0][0]==board[1][1]==board[2][2]) or (board[0][2]==board[1][1]==board[2][0])):
        return board[1][1]
    return None

def terminal(board):
    if checkWinner(board) is not None:
        return True
    else:
        return movesRemaining(board) == False

def evaluate(board):
    winner = checkWinner(board)
    if winner == AI:
        return 1
    elif winner == HUMAN:
        return -1 
    else:
        return 0   

def minimax(board,depth,maximisingPlayer):
    if terminal(board):
        return evaluate(board)
    if maximisingPlayer:
        evaluation = evaluate(board)
        # evaluation -= depth # early winning
        maxEval = - float('inf') 
        for r in range(3):
            for c in range(3):
                if board[r][c]=='_':
                    board_copy = deepcopy(board)
                    board_copy[r][c] = AI
                    evaluation = minimax(board_copy,depth+1,False) 
                    maxEval = max(maxEval,evaluation)
        return maxEval
    else:
        evaluation = evaluate(board)
        # evaluation += depth # late losing
        minEval = float('inf')
        for r in range(3):
            for c in range(3):
                if board[r][c]=='_':
                    board_copy = deepcopy(board)
                    board_copy[r][c] = HUMAN
                    evaluation = minimax(board_copy,depth+1,True) 
                    minEval = min(minEval,evaluation)
        return minEval

def findOptimalMove(board):
    optimalPosition = (None,None)
    if terminal(board):
        return optimalPosition
    optimalScore = - float('inf')
    for r in range(3):
        for c in range(3):
            if board[r][c] == '_':
                board_copy = deepcopy(board)
                board_copy[r][c] = AI
                moveScore = minimax(board_copy,0,False)
                if moveScore > optimalScore:
                    optimalScore = moveScore
                    optimalPosition = (r,c)
    return optimalPosition

def init(choice):
    global AI
    global HUMAN
    if choice == 'y' or choice == 'Y':
        HUMAN = 'X'
        AI = 'O'
    else:
        HUMAN = 'O'
        AI = 'X'
        

if __name__ == '__main__':
    AI = 'X'
    HUMAN = 'O'
    boards = [
        [['X','O','X'],['O','O','X'],['_','_','_']],
        [['X','_','_'],['O','O','_'],['_','_','X']],
        [['O','_','X'],['X','_','_'],['X','O','O']]
    ]
    for board in boards:
        for row in board:
            print(*row)
        optimalPosition = findOptimalMove(board)
        print('\n\tPosition:',optimalPosition,'\n\n')