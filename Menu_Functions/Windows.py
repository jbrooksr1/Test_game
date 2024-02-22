import sys
from Menu_Functions.Draw_Functions import *
from Constants import *
from Game_Functions.Game_Run import *

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)


def difficulty_screen(window, button_text):
    running = True
    while running:

        mouse_x, mouse_y = pygame.mouse.get_pos()

        window.fill(BLACK)
        draw_text(window, f'{button_text}', text_font, RED, TEXT_X, TEXT_Y)

        exit_button = button(window, (BUTTON_X, BUTTON_Y + (WINDOW_HEIGHT // 9) * 7), 'Back', WHITE, RED)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if exit_button.collidepoint((mouse_x, mouse_y)) and click:
            running = False

        pygame.display.update()


def main_menu(window):
    running = True
    while running:

        mouse_x, mouse_y = pygame.mouse.get_pos()

        window.fill(BLACK)
        draw_text(window, 'Main Menu', text_font, WHITE, TEXT_X, TEXT_Y)

        button_1 = button(window, (BUTTON_X, BUTTON_Y), 'Option 1', WHITE, RED)
        button_2 = button(window, (BUTTON_X, BUTTON_Y * 2), 'Option 2', WHITE, RED)
        button_3 = button(window, (BUTTON_X, BUTTON_Y * 3), 'Option 3', WHITE, RED)
        button_4 = button(window, (BUTTON_X, BUTTON_Y * 4), 'Option 4', WHITE, RED)
        exit_button = button(window, (BUTTON_X, BUTTON_Y + (WINDOW_HEIGHT // 9) * 7), 'Back', WHITE, RED)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if button_1.collidepoint((mouse_x, mouse_y)) and click:
            # difficulty_screen(window, "option 1")
            game_run(window)
        if button_2.collidepoint((mouse_x, mouse_y)) and click:
            difficulty_screen(window, "option 2")
        if button_3.collidepoint((mouse_x, mouse_y)) and click:
            difficulty_screen(window, "option 3")
        if button_4.collidepoint((mouse_x, mouse_y)) and click:
            difficulty_screen(window, "option 4")
        if exit_button.collidepoint((mouse_x, mouse_y)) and click:
            running = False

        pygame.display.update()


def start_window(window):
    global WINDOW

    while True:

        mouse_x, mouse_y = pygame.mouse.get_pos()

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                WINDOW = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        window.fill(BLACK)
        menu_button = button(window, (BUTTON_X, BUTTON_Y + 500), "Difficulty", WHITE, RED)

        if menu_button.collidepoint((mouse_x, mouse_y)) and click:
            main_menu(window)

        draw_text(window, 'Start Window', text_font, WHITE, TEXT_X, TEXT_Y)

        pygame.display.update()
