import pygame
import sys
import math

BOARD_SIZE = 5
CELL_SIZE = 80
SCREEN_SIZE = BOARD_SIZE * CELL_SIZE
RADIUS = CELL_SIZE // 3
LINE_COLOR = (0, 0, 0)
BG_COLOR = (240, 220, 180)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
EMPTY = ' '

board = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

def draw_board(screen):
    screen.fill(BG_COLOR)

    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            x = col * CELL_SIZE + CELL_SIZE // 2
            y = row * CELL_SIZE + CELL_SIZE // 2
            pygame.draw.line(screen, LINE_COLOR, (CELL_SIZE // 2, y), (SCREEN_SIZE - CELL_SIZE // 2, y), 2)
            pygame.draw.line(screen, LINE_COLOR, (x, CELL_SIZE // 2), (x, SCREEN_SIZE - CELL_SIZE // 2), 2)

    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            x = col * CELL_SIZE + CELL_SIZE // 2
            y = row * CELL_SIZE + CELL_SIZE // 2
            if board[row][col] == 'B':
                pygame.draw.circle(screen, BLACK, (x, y), RADIUS)
            elif board[row][col] == 'W':
                pygame.draw.circle(screen, WHITE, (x, y), RADIUS)
                pygame.draw.circle(screen, LINE_COLOR, (x, y), RADIUS, 2)

def is_valid_move(row, col):
    return 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE and board[row][col] == EMPTY

def calculate_score():
    black_score = sum(row.count('B') for row in board)
    white_score = sum(row.count('W') for row in board)
    visited = [[False] * BOARD_SIZE for _ in range(BOARD_SIZE)]

    def flood_fill(r, c):
        stack = [(r, c)]
        territory = []
        borders = set()
        while stack:
            x, y = stack.pop()
            if not (0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE) or visited[x][y]:
                continue
            visited[x][y] = True

            if board[x][y] == EMPTY:
                territory.append((x, y))
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE:
                        if board[nx][ny] == EMPTY:
                            stack.append((nx, ny))
                        else:
                            borders.add(board[nx][ny])

        return territory, borders

    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            if board[r][c] == EMPTY and not visited[r][c]:
                territory, borders = flood_fill(r, c)
                if borders == {'B'}:
                    black_score += len(territory)
                elif borders == {'W'}:
                    white_score += len(territory)

    return black_score, white_score

def is_game_over():
    return all(cell != EMPTY for row in board for cell in row)

def show_winner(screen):
    black_score, white_score = calculate_score()
    font = pygame.font.Font(None, 50)

    if black_score > white_score:
        text = font.render("Black is winner!", True, BLACK)
    elif white_score > black_score:
        text = font.render("White is winner!", True, BLACK)
    else:
        text = font.render("Draw!", True, BLACK)

    screen.blit(text, (SCREEN_SIZE // 2 - text.get_width() // 2, SCREEN_SIZE // 2 - text.get_height() // 2))
    pygame.display.flip()
    pygame.time.delay(3000)

def minimax(depth, is_maximizing, alpha, beta):
    black_score, white_score = calculate_score()
    
    if depth == 0 or is_game_over():
        return black_score - white_score

    if is_maximizing:
        max_eval = -math.inf
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if is_valid_move(row, col):
                    board[row][col] = 'B'
                    eval = minimax(depth - 1, False, alpha, beta)
                    board[row][col] = EMPTY
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if is_valid_move(row, col):
                    board[row][col] = 'W'
                    eval = minimax(depth - 1, True, alpha, beta)
                    board[row][col] = EMPTY
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def find_best_move():
    best_score = -math.inf
    best_move = None
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if is_valid_move(row, col):
                board[row][col] = 'B'
                score = minimax(3, False, -math.inf, math.inf)
                board[row][col] = EMPTY
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    return best_move

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
    pygame.display.set_caption("Cờ Vây với Minimax AI (5x5)")

    clock = pygame.time.Clock()
    running = True
    turn = 'W'

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and turn == 'W':
                row, col = get_cell_from_mouse(event.pos)
                if is_valid_move(row, col):
                    board[row][col] = 'W'
                    turn = 'B'
                    
        if turn == 'B' and not is_game_over():
            ai_move = find_best_move()
            if ai_move:
                board[ai_move[0]][ai_move[1]] = 'B'
            turn = 'W'

        if is_game_over():
            draw_board(screen)
            show_winner(screen)
            running = False

        draw_board(screen)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

def get_cell_from_mouse(pos):
    x, y = pos
    col = x // CELL_SIZE
    row = y // CELL_SIZE
    return row, col

if __name__ == "__main__":
    main()