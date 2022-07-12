import sys
import pygame
from pygame.constants import QUIT

# Startup Display
pygame.init()
display_info = pygame.display.Info()
display = pygame.display.set_mode((display_info.current_w, display_info.current_h), pygame.FULLSCREEN)
display_size = display.get_size()
window = pygame.Surface((1024, 576))
pygame.display.set_caption('TUI Commander 0.1a')


def pixel(window, x, y, color):
    pygame.draw.rect(window, color, (x, y, 4, 4))


while True:  # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pixel(window=window, x=10, y=10, color=(255, 0, 0))
    scaled_win = pygame.transform.smoothscale(window, display_size)
    display.blit(scaled_win, (0, 0))
    pygame.display.update()
    display.fill((0, 0, 0))
