from Game_Functions.Draw_Board import *
from Constants import *
pygame.init()

font = pygame.font.SysFont('Ariel', 20)


def draw(window, score, player):
    window.fill('dark grey')
    pygame.draw.circle(window, 'white', (player.player_x, player.player_y), WINDOW_HEIGHT // 10)
    draw_board(window)
    player.draw_player(window)
    score_text = font.render(f'SCORE: {score}', True, 'white')
    window.blit(score_text, (WINDOW_WIDTH // 75, (WINDOW_HEIGHT // 2) + (WINDOW_HEIGHT // 4) +
                             (WINDOW_HEIGHT // 8) + (WINDOW_HEIGHT // 16)))
    pygame.display.update()
