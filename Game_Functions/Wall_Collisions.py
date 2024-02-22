from Constants import *
from Game_Functions.Boards import *


def wall_collision(direction, x, y):
    # 0-r, 1-l, 2-u, 3-d
    turns = [False, False, False, False]
    num1 = (BLOCK_SIZE // 2) + (BLOCK_SIZE // 12)
    num2 = BLOCK_SIZE // 2
    low = num2 - (num2 // 4)
    high = num2 + (num2 // 4)
    if x // BLOCK_SIZE < 31:
        if direction == 0:
            if board[y // BLOCK_SIZE][(x - num1) // BLOCK_SIZE] < 2:
                turns[1] = True
        if direction == 1:
            if board[y // BLOCK_SIZE][(x + num1) // BLOCK_SIZE] < 2:
                turns[0] = True
        if direction == 2:
            if board[(y + num1) // BLOCK_SIZE][x // BLOCK_SIZE] < 2:
                turns[3] = True
        if direction == 3:
            if board[(y - num1) // BLOCK_SIZE][x // BLOCK_SIZE] < 2:
                turns[2] = True

        if direction == 2 or direction == 3:
            if low <= x % BLOCK_SIZE <= high:
                if board[(y + num1) // BLOCK_SIZE][x // BLOCK_SIZE] < 2:
                    turns[3] = True
                if board[(y - num1) // BLOCK_SIZE][x // BLOCK_SIZE] < 2:
                    turns[2] = True
            if low <= y % BLOCK_SIZE <= high:
                if board[y // BLOCK_SIZE][(x + BLOCK_SIZE) // BLOCK_SIZE] < 2:
                    turns[0] = True
                if board[y // BLOCK_SIZE][(x - BLOCK_SIZE) // BLOCK_SIZE] < 2:
                    turns[1] = True

        if direction == 0 or direction == 1:
            if low <= x % BLOCK_SIZE <= high:
                if board[(y + BLOCK_SIZE) // BLOCK_SIZE][x // BLOCK_SIZE] < 2:
                    turns[3] = True
                if board[(y - BLOCK_SIZE) // BLOCK_SIZE][x // BLOCK_SIZE] < 2:
                    turns[2] = True
            if low <= y % BLOCK_SIZE <= high:
                if board[y // BLOCK_SIZE][(x + num1) // BLOCK_SIZE] < 2:
                    turns[0] = True
                if board[y // BLOCK_SIZE][(x - num1) // BLOCK_SIZE] < 2:
                    turns[1] = True
    else:
        turns[0] = True
        turns[1] = True

    return turns
