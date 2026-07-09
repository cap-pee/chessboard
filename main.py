




class Board:
    def __init__(self):
        self.__grid = [[None] * 8 for i in range(8)]
        self.boardSetup()
        self.currentTurn = 'white'

    def showBoard(self):
        return self.__grid
    
    def boardSetup(self):
        # pawns
        for i in range(8):
            # black
            self.__grid[1][i] = Pawn('black')
            # white
            self.__grid[6][i] = Pawn('white')

        # other pieces
        
        # black
        self.__grid[0][0], self.__grid[0][7] = Rook('black'), Rook('black')
        self.__grid[0][1], self.__grid[0][6] = Knight('black'), Knight('black')
        self.__grid[0][2], self.__grid[0][5] = Bishop('black'), Bishop('black')
        self.__grid[0][3] = Queen('black')
        self.__grid[0][4] = King('black')

        # white
        self.__grid[7][0], self.__grid[7][7] = Rook('white'), Rook('white')
        self.__grid[7][1], self.__grid[7][6] = Knight('white'), Knight('white')
        self.__grid[7][2], self.__grid[7][5] = Bishop('white'), Bishop('white')
        self.__grid[7][3] = Queen('white')
        self.__grid[7][4] = King('white')

        print('Board setup complete!')

    def isOnBoard(self, row, col):
        if row >= 0 and row < 8:
            if col >= 0 and col < 8:
                return True
        return False

    def isEmpty(self, row, col):
        if self.__grid[row][col] == None:
            return True
        return False
    
    def isEnemy(self, row, col, color):
        if self.isEmpty(row, col):
            return False
        if self.__grid[row][col].getColor() != color:
            return True
        return False
    
    def getPiece(self, row, col):
        return self.__grid[row][col]
    
    def setPiece(self, row, col, piece):
        self.__grid[row][col] = piece
    
    def movePiece(self, start_row, start_col, end_row, end_col):
        if self.isEmpty(start_row, start_col):
            return
        piece = self.getPiece(start_row, start_col)
        if piece.getColor() == self.currentTurn:
            if self.isLegal(start_row, start_col, end_row, end_col):
                self.__grid[start_row][start_col], self.__grid[end_row][end_col] = None, piece
                
                # pawn
                if piece.getType() == 'P':
                    if piece.firstMove:
                        piece.firstMove = False

                # turns
                if self.currentTurn == 'white':
                    self.currentTurn = 'black'
                else:
                    self.currentTurn = 'white' 
    
    def findKing(self, color):
        for i in range(8):
            for j in range(8):
                if not self.isEmpty(i, j):
                    piece = self.getPiece(i, j)
                    if piece.getType() == 'K':
                        if piece.getColor() == color:
                            return (i, j)
                        
    def getAllMoves(self, color):
        allmoves = []

        for i in range(8):
            for j in range(8):
                if not self.isEmpty(i, j):
                    piece = self.getPiece(i, j)
                    if piece.getColor() == color:
                        allmoves.extend(piece.getLegalMoves(i, j, self)[0])
        
        return allmoves

    def isChecked(self, color):
        king = self.findKing(color)
        
        enemycolor = 'white'
        
        if color == 'white':
            enemycolor = 'black'
        
        moves = self.getAllMoves(enemycolor)

        for move in moves:
            if move == king:
                return True
        return False

    def getLegalMoves(self, row, col):
        if not self.isEmpty(row, col):
            piece = self.getPiece(row, col)
            moves = piece.getLegalMoves(row, col, self)[0]
            legalMoves = []
            for move in moves:
                dest = self.getPiece(move[0], move[1])
                self.setPiece(move[0], move[1], piece)
                self.setPiece(row, col, None)
                if self.isChecked(piece.getColor()):
                    self.setPiece(move[0], move[1], dest)
                    self.setPiece(row, col, piece)
                    continue
                legalMoves.append(move)
                self.setPiece(move[0], move[1], dest)
                self.setPiece(row, col, piece)
            
            return legalMoves
        
    def getAllLegalMoves(self, color):
        allLegalMoves = []

        for i in range(8):
            for j in range(8):
                if not self.isEmpty(i, j):
                    piece = self.getPiece(i, j)
                    if piece.getColor() == color:
                        allLegalMoves.extend(self.getLegalMoves(i, j))

        return allLegalMoves
    
    def isCheckMate(self, color):
        if self.isChecked(color):
            if len(self.getAllLegalMoves(color)) == 0:
                return True
        return False
    
    def isStaleMate(self, color):
        if not self.isChecked(color):
            if len(self.getAllLegalMoves(color)) == 0:
                return True
        return False
    
    def isLegal(self, start_row, start_col, end_row, end_col):
        allLegalMoves = self.getLegalMoves(start_row, start_col)
        for move in allLegalMoves:
            if move == (end_row, end_col):
                return True
        return False

    def displayBoard(self):
        print('      0   1    2   3   4    5   6   7')
        for i in range(8):
            pieces = ''
            for j in range(8):
                if self.isEmpty(i, j):
                    piece = '.'
                    pieces = pieces + '   ' + piece
                    continue
                piece = self.getPiece(i, j)
                pType = piece.getType()
                pColor = piece.getColor()
                if pColor == 'white':
                    pColor = 'W'
                else:
                    pColor = 'B'
                piece = pType + '|' + pColor
                pieces = pieces + ' ' + piece
            print(f'{i} | {pieces}')

    def clearBoard(self):
        for i in range(8):
            for j in range(8):
                self.setPiece(i, j, None)

# board = [[None]* 8  for i in range(8)]
# for i in range(8):
#     print(f'{board[i]}')


class Piece:

    def __init__(self, color, type):
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
            if board.isOnBoard(new_row, new_col):
                
                # check if it's your own piece or not
                
                if board.isEmpty(new_row, new_col):
                    moves.append((new_row, new_col))
                    continue
                elif board.isEnemy(new_row, new_col, self.getColor()):
                    moves.append((new_row, new_col))
                    capturable_pieces.append((new_row, new_col))


        return moves, capturable_pieces
    

class Pawn(Piece):

    def __init__(self, color):
        super().__init__(color, 'P')

        if color == 'white':
            self.direction = -1
        else:
            self.direction = 1
        
        self.firstMove = True

    pawn_direction = [(1, 0)]
    pawn_captures = [
        (1, -1),
        (1, 1)
    ]

    def getLegalMoves(self, row, col, board):
        
        moves = []
        capturable_pieces = []

        if self.firstMove:
            for dr, dc in self.pawn_direction:
                sqs_moved = 1

                while sqs_moved < 3:
                    new_row = row + (dr * self.direction * sqs_moved)
                    new_col = col + (dc * sqs_moved)


                    # can't move out of the board on 1st move
                    if board.isEmpty(new_row, new_col):
                        moves.append((new_row, new_col))
                        sqs_moved += 1
                        continue
                    break
        else:
            for dr, dc in self.pawn_direction:
                new_row = row + (dr * self.direction)
                new_col = col + dc


                if board.isOnBoard(new_row, new_col):
                    
                    if board.isEmpty(new_row, new_col):
                        moves.append((new_row, new_col))

        for ar, ac in self.pawn_captures:
            new_row = row + (ar * self.direction)
            new_col = col + ac

            
            if board.isOnBoard(new_row, new_col):
                if board.isEnemy(new_row, new_col, self.getColor()):
                    moves.append((new_row, new_col))
                    capturable_pieces.append((new_row, new_col))


        return moves, capturable_pieces


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
            
                if board.isOnBoard(new_row, new_col):
                    
                    if board.isEmpty(new_row, new_col):
                        moves.append((new_row, new_col))
                        sqs_moved += 1
                        continue
                    elif board.isEnemy(new_row, new_col, self.getColor()):
                        moves.append((new_row, new_col))
                        capturable_pieces.append((new_row, new_col))
                
                # break if there's a piece in the way or not on board
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

                if board.isOnBoard(new_row, new_col):

                    if board.isEmpty(new_row, new_col):
                        moves.append((new_row, new_col))
                        sqs_moved += 1
                        continue
                    elif board.isEnemy(new_row, new_col, self.getColor()):
                        moves.append((new_row, new_col))
                        capturable_pieces.append((new_row, new_col))
        

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

                if board.isOnBoard(new_row, new_col):
                    
                    if board.isEmpty(new_row, new_col):
                        moves.append((new_row, new_col))
                        sqs_moved += 1
                        continue
                    elif board.isEnemy(new_row, new_col, self.getColor()):
                        moves.append((new_row, new_col))
                        capturable_pieces.append((new_row, new_col))

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

    def getLegalMoves(self, row, col, board):
        

        moves = []
        capturable_pieces = []

        for dr, dc in self.king_moves:
            new_row = row + dr
            new_col = col + dc


            if board.isOnBoard(new_row, new_col):
                
                if board.isEmpty(new_row, new_col):
                    moves.append((new_row, new_col))
                    continue
                elif board.isEnemy(new_row, new_col, self.getColor()):
                    moves.append((new_row, new_col))
                    capturable_pieces.append((new_row, new_col))

        return moves, capturable_pieces
    



# board = Board()