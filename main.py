import pygame, sys, functions, classes, constants
from pygame.locals import QUIT

pygame.init()
win = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Colosseum Fighter')
player = classes.Player(50, 50)

while constants.run:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    win.fill((0, 0, 0))
    player.move()
    player.draw(win)
