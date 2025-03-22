import pygame
import sys
import math

pygame.init()

WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

pygame.font.init()
font = pygame.font.Font(None, 75)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BG_COLOR)

board = [[' ' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

def draw_lines():
    for row in range(1, BOARD_ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, row * SQUARE_SIZE), (WIDTH, row * SQUARE_SIZE), LINE_WIDTH)
    for col in range(1, BOARD_COLS):
        pygame.draw.line(screen, LINE_COLOR, (col * SQUARE_SIZE, 0), (col * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

draw_lines()

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'O':
                pygame.draw.circle(screen, CIRCLE_COLOR, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 'X':
                pygame.draw.line(screen, CROSS_COLOR, 
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), 
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, 
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), 
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)

def check_winner():
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != ' ':
            return board[row][0]
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    return None

def is_full():
    for row in board:
        if ' ' in row:
            return False
    return True  

def reset_board() :
    global board, player_turn 
    board = [[' ' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
    player_turn = True
    screen.fill(BG_COLOR)
    draw_lines()

# Minimax algorithm for AI
def minimax(board, is_maximizing):
    winner = check_winner()
    if winner == 'X':
        return 10
    if winner == 'O':
        return -10
    if is_full():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    score = minimax(board, False)
                    board[row][col] = ' '
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf # vô cực
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row][col] == ' ':
                    board[row][col] = 'O'
                    score = minimax(board, True)
                    board[row][col] = ' '
                    best_score = min(best_score, score)
        return best_score

def find_best_move():
    best_score = -math.inf
    best_move = None
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == ' ':
                board[row][col] = 'X'
                score = minimax(board, False)
                board[row][col] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    return best_move

# Main game loop
player_turn = True  # Player starts as 'O'
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and player_turn:
            x_pos = event.pos[0] // SQUARE_SIZE
            y_pos = event.pos[1] // SQUARE_SIZE

            if board[y_pos][x_pos] == ' ':
                board[y_pos][x_pos] = 'O'
                player_turn = False

        if not player_turn and not check_winner() and not is_full():
            ai_move = find_best_move()
            if ai_move:
                board[ai_move[0]][ai_move[1]] = 'X'
                player_turn = True

    screen.fill(BG_COLOR)
    draw_lines()
    draw_figures()

    winner = check_winner()
    if winner or is_full():
        text = font.render(f"{winner if winner else 'Draw!'} wins!", True, (255, 255, 255))
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
        pygame.display.update()
        pygame.time.wait(3000)
        running = False

    pygame.display.update()

pygame.quit()