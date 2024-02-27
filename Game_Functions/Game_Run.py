import sys

from Game_Functions.Player import *
from Game_Functions.Wall_Collisions import *
from Game_Functions.Collect_Coins import *
from Game_Functions.Draw_Function import *
from Menu_Functions.Draw_Functions import *

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)


def pause_window(window, text, player):
    running = True
    while running:

        # mouse_x, mouse_y = pygame.mouse.get_pos()

        pygame.draw.rect(window, BLACK, (WINDOW_WIDTH // 2 - WINDOW_HEIGHT // 6,
                                         WINDOW_HEIGHT // 2 - WINDOW_HEIGHT // 6, 300, 300))
        draw_pause_text(window, f'{text}', text_font, WHITE, PAUSE_TEXT_LOCATION, PAUSE_TEXT_LOCATION)

        # resume_button = button(window, (BUTTON_X, BUTTON_Y + (WINDOW_HEIGHT // 9) * 7), 'Back', WHITE, RED)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    player.player_speed = 3
            # if event.type == pygame.MOUSEBUTTONDOWN:
                # if event.button == 1:
                # click = True

        # if resume_button.collidepoint((mouse_x, mouse_y)) and click:
            # running = False
            # player.player_speed = 3

        pygame.display.update()


def game_run(window):

    global WINDOW

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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    direction_command = 0
                if event.key == pygame.K_LEFT:
                    direction_command = 1
                if event.key == pygame.K_UP:
                    direction_command = 2
                if event.key == pygame.K_DOWN:
                    direction_command = 3
                if event.key == pygame.K_ESCAPE:
                    player.player_speed = 0
                    pause_window(window, 'Game Paused', player)

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
