from Constants import *
from Game_Functions.Boards import *


def collect_coins(score, x, y):
    if 0 < x // BLOCK_SIZE < 31:
        if board[y // BLOCK_SIZE][x // BLOCK_SIZE] == 1:
            board[y // BLOCK_SIZE][x // BLOCK_SIZE] = 0
            score += 1
    return score
