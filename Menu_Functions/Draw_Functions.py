import pygame

from Constants import TEXT_SIZE, BUTTON_TEXT_SIZE
pygame.init()

text_font = pygame.font.SysFont('Arial', TEXT_SIZE)


def draw_text(window, text, font, colour, x, y):
    text_object = font.render(text, 1, colour)
    text_box = text_object.get_rect()
    text_box.topleft = (x, y)
    window.blit(text_object, text_box)


def button(window, position, text, text_colour, box_colour):
    font = pygame.font.SysFont('arial', BUTTON_TEXT_SIZE)
    text_render = font.render(text, True, text_colour)
    x, y, width, height = text_render.get_rect()
    x, y = position
    pygame.draw.rect(window, box_colour, (x, y, width, height))
    return window.blit(text_render, (x, y))
