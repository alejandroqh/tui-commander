import sys
import pygame
from pygame.constants import QUIT
from random import randrange

# Startup Display
pygame.init()
display_info = pygame.display.Info()
display = pygame.display.set_mode((display_info.current_w, display_info.current_h))
pygame.display.set_caption('TUI Commander 0.1a')

while True:  # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.draw.line(display, (255, 255, 255), (1 + randrange(800), 1 + randrange(800)), (1 + randrange(800), 1 + randrange(800)))
    pygame.display.update()
    display.fill((0, 0, 0))
