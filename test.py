# testing the game logic


from MAIN.main import *

board = Board()

board.displayBoard()

print('---------------')

# piece = board.getPiece(6, 4)
# firstmove = piece.firstMove
# print(f'firstMove: {firstmove}')

# moves = piece.getLegalMoves(6, 4, board)
# print(f'moves: {moves}')
# print(f'turn: {board.currentTurn}')
# board.movePiece(6, 4, 5, 4)
# print('Moved --------------------')
# firstmove = piece.firstMove
# print(f'firstMove: {firstmove}')
# board.displayBoard()

# moves = piece.getLegalMoves(5, 4, board)
# print(f'moves: {moves}')
# print(f'turn: {board.currentTurn}')
# board.movePiece(1, 3, 3, 3)
# print('-----------------------')
# board.displayBoard()

# piece = board.getPiece(7, 1)
# print(piece.getLegalMoves(7, 1, board))
# print(board.getLegalMoves(7, 1))

# wK = board.getPiece(7, 4)
# wR = board.getPiece(7, 0)
# bR = board.getPiece(0, 0)
# board.setPiece(3, 3, wK)
# board.setPiece(4, 3, wR)
# board.setPiece(5, 3, bR)
# board.displayBoard()

# piece = board.getPiece(4, 3)

# print(piece.getLegalMoves(4, 3, board))
# print(board.getLegalMoves(4, 3))

board.clearBoard()
board.displayBoard()

# board.setPiece(7, 4, King('white'))
# board.setPiece(0, 4, King('black'))
# board.setPiece(3, 4, Rook('black'))

# board.setPiece(7, 4, King('white'))
# board.setPiece(5, 4, Bishop('white'))
# board.setPiece(0, 4, King('black'))
# board.setPiece(3, 4, Rook('black'))

# board.setPiece(7, 0, King('white'))
# board.setPiece(5, 2, King('black'))
# board.setPiece(6, 1, Queen('black'))

# board.setPiece(7, 0, King('white'))
# board.setPiece(5, 1, King('black'))
# board.setPiece(6, 2, Queen('black'))

# board.setPiece(7, 4, King('white'))
# board.setPiece(0, 4, King('black'))
# board.setPiece(5, 4, Rook('black'))
# 
board.displayBoard()
print(board.isChecked('white'))
print(board.isChecked('black'))

print('---------------')
print(board.isCheckMate('white'))
print(board.isCheckMate('black'))

print('-------------')
print(board.isStaleMate('white'))
print(board.isStaleMate('black'))