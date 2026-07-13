import pygame
from main import *

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Chess')

clock = pygame.time.Clock()

board = Board()
board.boardSetup()

SQUARESIZE = 100


bishopImgW = pygame.image.load('./assets/images/white_bishop.png')
kingImgW = pygame.image.load('./assets/images/white_king.png')
knightImgW = pygame.image.load('./assets/images/white_knight.png')
pawnImgW = pygame.image.load('./assets/images/white_pawn.png')
queenImgW =pygame.image.load('./assets/images/white_queen.png') 
rookImgW = pygame.image.load('./assets/images/white_rook.png')
bishopImgB = pygame.image.load('./assets/images/black_bishop.png')
kingImgB = pygame.image.load('./assets/images/black_king.png')
knightImgB = pygame.image.load('./assets/images/black_knight.png')
pawnImgB = pygame.image.load('./assets/images/black_pawn.png')
queenImgB =pygame.image.load('./assets/images/black_queen.png') 
rookImgB = pygame.image.load('./assets/images/black_rook.png')

images = {
    'bW': bishopImgW,
    'kW': kingImgW,
    'knW': knightImgW,
    'pW': pawnImgW,
    'qW': queenImgW,
    'rW': rookImgW,
    'bB': bishopImgB,
    'kB': kingImgB,
    'knB': knightImgB,
    'pB': pawnImgB,
    'qB': queenImgB,
    'rB': rookImgB,
}




def drawBoard(surface):
    for row in range(8):
        for col in range(8):
            x = col * SQUARESIZE
            y = row * SQUARESIZE

            if (row + col) % 2 == 0:
                # white
                pygame.draw.rect(surface, 'white', (x, y, SQUARESIZE, SQUARESIZE))
            else:
                # black
                    pygame.draw.rect(surface, 'brown', (x, y, SQUARESIZE, SQUARESIZE))


def drawPieces(surface):

    for row in range(8):
        for col in range(8):
            if board.isEmpty(row, col):
                continue
            piece = board.getPiece(row, col)
            
            color = 'W'
            if piece.getColor() == 'black':
                color = 'B'
            symbol = piece.getType().lower()
            key = symbol + color
            image = images[key]

            x, y = convertToPygame(row, col)
            
            surface.blit(image, (x, y))
            

def drawPiece(surface, piece, x, y):
    color = 'W'
    if piece.getColor() == 'black':
        color = 'B'
    symbol = piece.getType().lower()
    key = symbol + color
    image = images[key]
    scaled_image = pygame.transform.scale(image, (100, 100))
    surface.blit(scaled_image, (x, y))


def legalMoves(surface, x, y):
    row, col = convertToPy(x, y)
    
    if board.isEmpty(row, col):
        return

    moves = board.getLegalMoves(row, col)
    rects = []
    for move in moves:
        x, y = convertToPygame(move[0], move[1])

        rects.append(pygame.Rect(x, y, SQUARESIZE, SQUARESIZE))
    for rect in rects:
        pygame.draw.rect(surface, 'blue', rect, 5)


def dragPiece(surface, x, y, mouseX, mouseY):
    row, col = convertToPy(x, y)
    

    if board.isEmpty(row, col):
        return

    piece = board.getPiece(row, col)
    pygame.mouse.set_visible(False)
    drawPiece(surface, piece, mouseX - 50, mouseY - 50)
    # board.movePiece(row, col, finalRow, finalCol)


def movePiece(x, y, mouseX, mouseY):
    row, col = convertToPy(x, y)
    finalRow, finalCol = convertToPy(mouseX, mouseY)

    
    board.movePiece(row, col, finalRow, finalCol)
    pygame.mouse.set_visible(True)


def gameOver(surface, winner):
    text = 'Checkmate!'
    text2 = f'{winner} wins!!'


def convertToPygame(row, col):
    x = col * SQUARESIZE
    y = row * SQUARESIZE
    return x, y

def convertToPy(x, y):
    row = y // SQUARESIZE
    col = x // SQUARESIZE
    return row, col


clicks = []


running = True
while running:

    # clearing the screen
    screen.fill('green')


    # board
    drawBoard(screen)
    drawPieces(screen)
    
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if len(clicks) == 2:
                clicks.clear()
            clicks.append(event.pos)
    
    # print(click)
    mouse = pygame.mouse.get_pos()
    if clicks:
        print(clicks)
        legalMoves(screen, clicks[0][0], clicks[0][1])
        dragPiece(screen, clicks[0][0], clicks[0][1], mouse[0], mouse[1])
        if len(clicks) == 2:
            movePiece(clicks[0][0], clicks[0][1], clicks[1][0], clicks[1][1])
            if board.isCheckMate('white'):
                gameOver(screen, 'Black')
            elif board.isCheckMate('black'):
                gameOver(screen, 'White')
            clicks.clear()


    pygame.display.flip()
    clock.tick(60)


pygame.quit()