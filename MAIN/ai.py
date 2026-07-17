from evaluation import evaluate


def minimax(board, depth, alpha, beta):
    
    maximize = True
    color = board.currentTurn
    if color == 'black':
        maximize = False

    allmoves = board.getAllLegalMoves(color)

    # checking for checkmate/stalemate
    if len(allmoves) == 0:
        if board.isChecked(color):
            if maximize:
                return -1000000000000000000000
            return 1000000000000000000000
        return 0

    if maximize:
        bestScore = -10000000000
    else:
        bestScore = 10000000000
    

    if depth == 0:
        score = evaluate(board)
        return score
    

    for move in allmoves:
        moveInfo = board.makeMove(move[0], move[1], move[2], move[3])
        returnedScore = minimax(board, depth-1, alpha, beta)
        board.undoMove(moveInfo)


        if maximize:

            if returnedScore > bestScore:
                bestScore = returnedScore
                alpha = max(alpha, bestScore)

        else:

            if returnedScore < bestScore:
                bestScore = returnedScore
                beta = min(beta, bestScore)
    
        if alpha >= beta:
            break
    return bestScore


def findBestMove(board, depth):
    maximize = True
    color = board.currentTurn
    if color == 'black':
        maximize = False
    
    allmoves = board.getAllLegalMoves(color)

    if maximize:
        bestScore = -10000000000
    else:
        bestScore = 10000000000

    alpha = -10000000000
    beta = 10000000000
    
    bestMove = None

    for move in allmoves:
        moveInfo = board.makeMove(move[0], move[1], move[2], move[3])
        returnedScore = minimax(board, depth-1, alpha, beta)
        board.undoMove(moveInfo)

        if maximize:
            if returnedScore > bestScore:
                bestScore = returnedScore
                bestMove = move
                alpha = max(alpha, bestScore)
        else:
            if returnedScore < bestScore:
                bestScore = returnedScore
                bestMove = move
                beta = min(beta, bestScore)
    
        if alpha >= beta:
            break

    return bestMove