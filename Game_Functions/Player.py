import pygame


class Player:

    player_colour = 'red'

    def __init__(self, player_x, player_y, player_size, player_speed):
        self.player_x = player_x
        self.player_y = player_y
        self.player_size = player_size
        self.player_speed = player_speed

    def draw_player(self, window):
        pygame.draw.circle(window, self.player_colour, (self.player_x, self.player_y), self.player_size)

    def move_player(self, direction, turns_allowed):
        if direction == 0 and turns_allowed[0]:
            self.player_x += self.player_speed
        elif direction == 1 and turns_allowed[1]:
            self.player_x -= self.player_speed
        elif direction == 2 and turns_allowed[2]:
            self.player_y -= self.player_speed
        elif direction == 3 and turns_allowed[3]:
            self.player_y += self.player_speed
