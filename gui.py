import pygame
from main import *

pygame.init()

screen = pygame.display.set_mode((820, 820))
pygame.display.set_caption('Chess')

board = Board()
board.boardSetup()

def drawBoard(surface):
    for row in range(8):
        for col in range(8):
            x = (col * 100) + 10
            y = (row * 100) + 10

            if (row + col) % 2 == 0:
                # white
                pygame.draw.rect(surface, 'white', (x, y, 100, 100))
            else:
                # black
                    pygame.draw.rect(surface, 'brown', (x, y, 100, 100))


def drawPieces(surface):
    
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

            x = (col * 100) + 15
            y = (row * 100) + 15
            
            screen.blit(image, (x, y))
            
def legalMoves(surface, x, y):
    col = (x - 15) // 100
    row = (y-15) // 100
    
    if board.isEmpty(row, col):
        return

    moves = board.getLegalMoves(row, col)
    rects = []
    for move in moves:
        x = (move[1] * 100) + 10
        y = (move[0] * 100) + 10

        rects.append(pygame.Rect(x, y, 100, 100))
    for rect in rects:
        pygame.draw.rect(surface, 'blue', rect, 5)


def dragPiece(surface, x, y, mouseX, mouseY):
    col = (x-15) // 100
    row = (y-15) // 100
    finalCol = (mouseX-15) // 100
    finalRow = (mouseY-15) // 100
    

    if board.isEmpty(row, col):
        return

    piece = board.getPiece(row, col)
    board.movePiece(row, col, finalRow, finalCol)   


click = 0

running = True
while running:

    
    screen.fill('green')


    # board
    drawBoard(screen)
    drawPieces(screen)
    
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = event.pos
    # clearing the screen
    print(click)
    if click != 0:
        legalMoves(screen, click[0], click[1])

    mouse = pygame.mouse.get_pos()
    if click != 0:
        dragPiece(screen, click[0], click[1], mouse[0], mouse[1])


    pygame.display.flip()
    clock = pygame.time.Clock()
    clock.tick(60)


pygame.quit()