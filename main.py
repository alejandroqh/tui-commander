import pygame, sys, os
from pygame.locals import *

pygame.display.init()
pygame.display.list_modes()
display = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Hello World!')
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
