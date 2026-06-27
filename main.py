


board = [['']* 8  for i in range(8)]
for i in range(8):
    print(f'{board[i]}')


class Piece:

    def __init__(self,color, type):
        self.__Color = color
        self.__Type = type


    def getColor(self):
        return self.__Color

    def getType(self):
        return self.__Type
    

class Knight(Piece):

    def __init__(self, color):
        super().__init__(color, 'Kn')
    
    knight_moves = [
        (-2, -1), 
        (-2, 1), 
        (-1, -2), 
        (-1, 2), 
        (1, -2), 
        (1, 2), 
        (2, -1), 
        (2, 1)
        ]

    def getLegalMoves(self, row, col):
        # current possible moves

        moves = []

        for dr, dc in self.knight_moves:
            new_row = row + dr
            new_col = col + dc

            # check if it's on the board
            if new_row >= 0 and new_row < 8:
                if new_col >= 0 and new_col < 8:
                    moves.append((new_row, new_col))
        
        return moves
    

class Pawn(Piece):

    def __init__(self, color):
        super().__init__(color, 'P')

        if color == 'White':
            self.direction = -1
        else:
            self.direction = 1

    # pawn_moves = [
    #     ()
    # ]

    def getLegalMoves(self, row, col):
        pass

    # will implement later since it's different


class Rook(Piece):

    def __init__(self, color):
        super().__init__(color, 'R')


    rook_moves = [
        (-1, 0), 
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    def getLegalMoves(self, row, col):
        pass


class Bishop(Piece):

    def __init__(self, color):
        super().__init__(color, 'B')

    bishop_moves = [
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1)
    ]

    def getLegalMoves(self, row, col):
        pass


class Queen(Piece):

    def __init__(self, color):
        super().__init__(color, 'Q')

    queen_moves = [
        (-1, 0),
        (-1, -1),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, 0),
        (1, -1),
        (1, 1)
    ]

    def getLegalMoves(self, row, col):
        pass


class King(Piece):

    def __init__(self, color):
        super().__init__(color, 'K')

    king_moves = [
        (-1, 0),
        (-1, -1),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, 0),
        (1, -1),
        (1, 1)
    ]

    def getLegalMoves(self, row, col):
        pass