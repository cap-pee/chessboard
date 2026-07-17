from evaluation import evaluate
from main import Board


def minimax(board, depth):
    
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
        returnedScore = minimax(board, depth-1)
        board.undoMove(moveInfo)


        if maximize:

            if returnedScore > bestScore:
                bestScore = returnedScore

        else:

            if returnedScore < bestScore:
                bestScore = returnedScore
    
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
    
    bestMove = None

    for move in allmoves:
        moveInfo = board.makeMove(move[0], move[1], move[2], move[3])
        returnedScore = minimax(board, depth-1)
        board.undoMove(moveInfo)

        if maximize:
            if returnedScore > bestScore:
                bestScore = returnedScore
                bestMove = move
        else:
            if returnedScore < bestScore:
                bestScore = returnedScore
                bestMove = move


    return bestMove