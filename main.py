


board = [[None]* 8  for i in range(8)]
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

    def getLegalMoves(self, row, col, board):
        # current possible moves

        moves = []
        capturable_pieces = []

        for dr, dc in self.knight_moves:
            new_row = row + dr
            new_col = col + dc

            # check if it's on the board
            if new_row >= 0 and new_row < 8:
                if new_col >= 0 and new_col < 8:
                    destination = board[new_row][new_col]

                    # check if it's your own piece or not
                    if isinstance(destination, Piece):
                        if destination.getColor() == self.getColor():
                            print('same team')
                            continue
                        else:
                            moves.append((new_row, new_col))
         
                            # add to another list if there's a piece you can capture
                            capturable_pieces.append((new_row, new_col))
         
                    # empty square
                    else:
                        moves.append((new_row, new_col))


        return moves, capturable_pieces
    

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


    rook_directions = [
        (-1, 0), 
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    def getLegalMoves(self, row, col, board):
        # current possible moves

        moves = []
        capturable_pieces = []


        for dr, dc in self.rook_directions:
            sqs_moved = 1
            
            # loop to keep checking further squares
            while True:
                new_row = row + (dr * sqs_moved)
                new_col = col + (dc * sqs_moved)
            
                if new_row >= 0 and new_row < 8:
                    if new_col >= 0 and new_col < 8:
                        destination = board[new_row][new_col]
                        if isinstance(destination, Piece):
                            if destination.getColor() == self.getColor():
                                print('same team')
                            else:
                                moves.append((new_row, new_col))
                                capturable_pieces.append((new_row, new_col))
                            # break loop if there's any piece in the way
                            break 
                        else:
                            moves.append((new_row, new_col))
                            sqs_moved += 1
                            # keep checking if square is empty
                            continue
                # break loop if destination not on the board
                break

        return moves, capturable_pieces
                            


class Bishop(Piece):

    def __init__(self, color):
        super().__init__(color, 'B')

    bishop_directions = [
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1)
    ]

    def getLegalMoves(self, row, col, board):

        moves = []
        capturable_pieces = []


        for dr, dc in self.bishop_directions:
            sqs_moved = 1

            while True:
                new_row = row + (dr * sqs_moved)
                new_col = col + (dc * sqs_moved)

                if new_row >= 0 and new_row < 8:
                    if new_col >= 0 and new_col < 8:
                        destination = board[new_row][new_col]
                        if isinstance(destination, Piece):
                            if destination.getColor() == self.getColor():
                                print('same team')
                            else:
                                moves.append((new_row, new_col))
                                capturable_pieces.append((new_row, new_col))
                            break
                        else:
                            moves.append((new_row, new_col))
                            sqs_moved += 1
                            continue
                break

        return moves, capturable_pieces


class Queen(Piece):

    def __init__(self, color):
        super().__init__(color, 'Q')

    queen_directions = [
        (-1, 0),
        (-1, -1),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, 0),
        (1, -1),
        (1, 1)
    ]

    def getLegalMoves(self, row, col, board):
        

        moves = []
        capturable_pieces = []


        for dr, dc in self.queen_directions:
            sqs_moved = 1

            while True:
                new_row = row + (dr * sqs_moved)
                new_col = col + (dc * sqs_moved)

                if new_row >= 0 and new_row < 8:
                    if new_col >= 0 and new_col < 8:
                        destination = board[new_row][new_col]
                        if isinstance(destination, Piece):
                            if destination.getColor() == self.getColor():
                                print('same team')
                            else:
                                moves.append((new_row, new_col))
                                capturable_pieces.append((new_row, new_col))
                            break
                        else:
                            moves.append((new_row, new_col))
                            sqs_moved += 1
                            continue
                break

        return moves, capturable_pieces


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