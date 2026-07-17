


values = {
    'P': 1,
    'Kn': 3,
    'B': 3,
    'R': 5,
    'Q': 9,
    'K': 1000000
}

def evaluate(board):
    score = 0
    for row in range(8):
        for col in range(8):
            if not board.isEmpty(row, col):
                piece = board.getPiece(row, col)
                pieceType = piece.getType()
                color = piece.getColor()
                val = values[pieceType]
                if color == 'white':
                    score += val
                else:
                    score -= val
    
    return score