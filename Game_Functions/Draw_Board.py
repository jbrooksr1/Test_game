from Constants import *
from Game_Functions.Boards import *


def draw_board(window):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                pygame.draw.circle(window, 'gold', (j * BLOCK_SIZE + (0.5 * BLOCK_SIZE),
                                                    i * BLOCK_SIZE + (0.5 * BLOCK_SIZE)), COIN_SIZE)
            if board[i][j] == 2:
                pygame.draw.line(window, WALL_COLOUR, (j * BLOCK_SIZE, i * BLOCK_SIZE + (0.5 * BLOCK_SIZE)),
                                 (j * BLOCK_SIZE + BLOCK_SIZE, i * BLOCK_SIZE + (0.5 * BLOCK_SIZE)), 4)
            if board[i][j] == 3:
                pygame.draw.line(window, WALL_COLOUR, (j * BLOCK_SIZE + (0.5 * BLOCK_SIZE), i * BLOCK_SIZE),
                                 (j * BLOCK_SIZE + (0.5 * BLOCK_SIZE), i * BLOCK_SIZE + BLOCK_SIZE), 4)
            if board[i][j] == 4:
                pygame.draw.line(window, WALL_COLOUR, (j * BLOCK_SIZE + (0.5 * BLOCK_SIZE),
                                                       i * BLOCK_SIZE + (0.5 * BLOCK_SIZE)),
                                 (j * BLOCK_SIZE + BLOCK_SIZE, i * BLOCK_SIZE + (0.5 * BLOCK_SIZE)), 4)
                pygame.draw.line(window, WALL_COLOUR, (j * BLOCK_SIZE + (0.5 * BLOCK_SIZE),
                                                       i * BLOCK_SIZE + (0.5 * BLOCK_SIZE)),
                                 (j * BLOCK_SIZE + (0.5 * BLOCK_SIZE), i * BLOCK_SIZE + BLOCK_SIZE), 4)
            if board[i][j] == 5:
                pygame.draw.line(window, WALL_COLOUR, (j * BLOCK_SIZE + (0.5 * BLOCK_SIZE),
                                                       i * BLOCK_SIZE + (0.5 * BLOCK_SIZE)),
                                 (j * BLOCK_SIZE + BLOCK_SIZE, i * BLOCK_SIZE + (0.5 * BLOCK_SIZE)), 4)
                pygame.draw.line(window, WALL_COLOUR, (j * BLOCK_SIZE + (0.5 * BLOCK_SIZE), i * BLOCK_SIZE),
                                 (j * BLOCK_SIZE + (0.5 * BLOCK_SIZE), i * BLOCK_SIZE + (0.5 * BLOCK_SIZE)), 4)
            if board[i][j] == 6:
                pygame.draw.line(window, WALL_COLOUR, (j * BLOCK_SIZE, i * BLOCK_SIZE + (0.5 * BLOCK_SIZE)),
                                 (j * BLOCK_SIZE + (0.5 * BLOCK_SIZE), i * BLOCK_SIZE + (0.5 * BLOCK_SIZE)), 4)
                pygame.draw.line(window, WALL_COLOUR, (j * BLOCK_SIZE + (0.5 * BLOCK_SIZE),
                                                       i * BLOCK_SIZE + (0.5 * BLOCK_SIZE)),
                                 (j * BLOCK_SIZE + (0.5 * BLOCK_SIZE), i * BLOCK_SIZE), 4)
            if board[i][j] == 7:
                pygame.draw.line(window, WALL_COLOUR, (j * BLOCK_SIZE, i * BLOCK_SIZE + (0.5 * BLOCK_SIZE)),
                                 (j * BLOCK_SIZE + (0.5 * BLOCK_SIZE), i * BLOCK_SIZE + (0.5 * BLOCK_SIZE)), 4)
                pygame.draw.line(window, WALL_COLOUR, (j * BLOCK_SIZE + (0.5 * BLOCK_SIZE),
                                                       i * BLOCK_SIZE + (0.5 * BLOCK_SIZE)),
                                 (j * BLOCK_SIZE + (0.5 * BLOCK_SIZE), i * BLOCK_SIZE + BLOCK_SIZE), 4)
            if board[i][j] == 8:
                pygame.draw.line(window, WALL_COLOUR, (j * BLOCK_SIZE, i * BLOCK_SIZE + (0.5 * BLOCK_SIZE)),
                                 (j * BLOCK_SIZE + (0.5 * BLOCK_SIZE), i * BLOCK_SIZE + (0.5 * BLOCK_SIZE)), 4)
                pygame.draw.line(window, WALL_COLOUR, (j * BLOCK_SIZE + (0.5 * BLOCK_SIZE), i * BLOCK_SIZE),
                                 (j * BLOCK_SIZE + (0.5 * BLOCK_SIZE), i * BLOCK_SIZE + BLOCK_SIZE), 4)
            if board[i][j] == 9:
                pygame.draw.line(window, WALL_COLOUR, (j * BLOCK_SIZE + (0.5 * BLOCK_SIZE),
                                                       i * BLOCK_SIZE + (0.5 * BLOCK_SIZE)),
                                 (j * BLOCK_SIZE + BLOCK_SIZE, i * BLOCK_SIZE + (0.5 * BLOCK_SIZE)), 4)
                pygame.draw.line(window, WALL_COLOUR, (j * BLOCK_SIZE + (0.5 * BLOCK_SIZE), i * BLOCK_SIZE),
                                 (j * BLOCK_SIZE + (0.5 * BLOCK_SIZE), i * BLOCK_SIZE + BLOCK_SIZE), 4)
            if board[i][j] == 10:
                pygame.draw.line(window, WALL_COLOUR, (j * BLOCK_SIZE, i * BLOCK_SIZE + (0.5 * BLOCK_SIZE)),
                                 (j * BLOCK_SIZE + BLOCK_SIZE, i * BLOCK_SIZE + (0.5 * BLOCK_SIZE)), 4)
                pygame.draw.line(window, WALL_COLOUR, (j * BLOCK_SIZE + (0.5 * BLOCK_SIZE), i * BLOCK_SIZE),
                                 (j * BLOCK_SIZE + (0.5 * BLOCK_SIZE), i * BLOCK_SIZE + (0.5 * BLOCK_SIZE)), 4)
            if board[i][j] == 11:
                pygame.draw.line(window, WALL_COLOUR, (j * BLOCK_SIZE, i * BLOCK_SIZE + (0.5 * BLOCK_SIZE)),
                                 (j * BLOCK_SIZE + BLOCK_SIZE, i * BLOCK_SIZE + (0.5 * BLOCK_SIZE)), 4)
                pygame.draw.line(window, WALL_COLOUR, (j * BLOCK_SIZE + (0.5 * BLOCK_SIZE),
                                                       i * BLOCK_SIZE + (0.5 * BLOCK_SIZE)),
                                 (j * BLOCK_SIZE + (0.5 * BLOCK_SIZE), i * BLOCK_SIZE + BLOCK_SIZE), 4)
