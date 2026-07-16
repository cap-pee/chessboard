# for testing timing of the algorithms

from main import *
from ai import *

board = Board()
board.clearBoard()

board.setPiece(7, 4, King('white'))
board.setPiece(0, 4, King('black'))
board.setPiece(4, 4, Queen('white'))
board.setPiece(4, 5, Queen('black'))

board.currentTurn = 'black'

import time
start = time.time()
move = findBestMove(board, 2)
print("Best move:", move)
print("Time taken:", time.time() - start, 'sec')