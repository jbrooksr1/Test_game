import sys

from Game_Functions.Player import *
from Game_Functions.Wall_Collisions import *
from Game_Functions.Collect_Coins import *
from Game_Functions.Draw_Function import *

WINDOW_WIDTH = 850
WINDOW_HEIGHT = 900
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)


def game_run(window):

    global WINDOW, WINDOW_HEIGHT, WINDOW_WIDTH

    score = 0
    direction = 0
    direction_command = 0

    player = Player(PLAYER_START_X, PLAYER_START_Y, PLAYER_SIZE, 3)

    while True:

        TIMER.tick(FPS)
        turns_allowed = wall_collision(direction, player.player_x, player.player_y)
        score = collect_coins(score, player.player_x, player.player_y)

        player.move_player(direction, turns_allowed)

        draw(window, score, player)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                WINDOW = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                WINDOW_HEIGHT = event.h
                WINDOW_WIDTH = event.w

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    direction_command = 0
                if event.key == pygame.K_LEFT:
                    direction_command = 1
                if event.key == pygame.K_UP:
                    direction_command = 2
                if event.key == pygame.K_DOWN:
                    direction_command = 3

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT and direction_command == 0:
                    direction_command = direction
                if event.key == pygame.K_LEFT and direction_command == 1:
                    direction_command = direction
                if event.key == pygame.K_UP and direction_command == 2:
                    direction_command = direction
                if event.key == pygame.K_DOWN and direction_command == 3:
                    direction_command = direction

        for i in range(4):
            if direction_command == i and turns_allowed[i]:
                direction = i
