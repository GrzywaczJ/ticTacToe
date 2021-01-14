import numpy
import pygame
import sys

pygame.init()

WIDTH = 600
HEIGHT = WIDTH
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 13
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4
# COLOURS
BACKGROUND_COLOR = (75, 179, 189)
LINE_COLOR = (72, 88, 89)
DRAWING_COLOR = (66, 66, 66)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BACKGROUND_COLOR)

# board
board = numpy.zeros((BOARD_ROWS, BOARD_COLS))


def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen,
                                   DRAWING_COLOR,
                                   (int(col * SQUARE_SIZE + SQUARE_SIZE // 2),
                                    int(row * SQUARE_SIZE + SQUARE_SIZE // 2)),
                                   CIRCLE_RADIUS,
                                   CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen,
                                 DRAWING_COLOR,
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 (col * SQUARE_SIZE - SPACE + SQUARE_SIZE, row * SQUARE_SIZE + SPACE),
                                 CROSS_WIDTH)
                pygame.draw.line(screen,
                                 DRAWING_COLOR,
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 CROSS_WIDTH)


def draw_lines():
    # 1 horizontal
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (HEIGHT, SQUARE_SIZE), LINE_WIDTH)
    # 2 horizontal
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (HEIGHT, 2 * SQUARE_SIZE), LINE_WIDTH)

    # 1 vertical
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    # 2 vertical
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)


def mark_square(row, col, player):
    board[row][col] = player


def available_square(row, col):
    return board[row][col] == 0


def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False

    return True


def check_win(player):
    # vertical win check
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True
    # horizontal win check
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True

    # left win check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_left_diagonal_line(player)
        return True

    # right win check
    if board[2][2] == player and board[1][1] == player and board[0][0] == player:
        draw_right_diagonal_line(player)
        return True

    return False


def draw_vertical_winning_line(col, player):
    pos_x = col * SQUARE_SIZE + SQUARE_SIZE // 2

    pygame.draw.line(screen,
                     DRAWING_COLOR,
                     (pos_x, 15),
                     (pos_x, HEIGHT - 15),
                     15)


def draw_horizontal_winning_line(row, player):
    pos_y = row * SQUARE_SIZE + SQUARE_SIZE // 2

    pygame.draw.line(screen,
                     DRAWING_COLOR,
                     (15, pos_y),
                     (WIDTH - 15, pos_y),
                     15)


def draw_left_diagonal_line(player):
    pygame.draw.line(screen,
                     DRAWING_COLOR,
                     (15, HEIGHT - 15),
                     (WIDTH - 15, 15),
                     15)


def draw_right_diagonal_line(player):
    pygame.draw.line(screen,
                     DRAWING_COLOR,
                     (15, 15),
                     (WIDTH - 15, HEIGHT - 15),
                     15)


def restart():
    screen.fill(BACKGROUND_COLOR)
    draw_lines()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0


draw_lines()

player = 1
game_over = False

# MAIN
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            mouseX = event.pos[0]  # x
            mouseY = event.pos[1]  # y

            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE

            print(clicked_row, clicked_col)

            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                if check_win(player):
                    game_over = True
                player = player % 2 + 1

                draw_figures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                game_over = False

    pygame.display.update()
