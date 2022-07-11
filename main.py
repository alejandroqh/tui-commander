import pygame, sys, os
from pygame.locals import *

pygame.init()
display_info = pygame.display.Info()
display = pygame.display.set_mode((display_info.current_w, display_info.current_h))
pygame.display.set_caption('TUI Commander 0.1a')

while True:  # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
