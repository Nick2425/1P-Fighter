import pygame, constants

win = pygame.display.set_mode(constants.SIZE)
pygame.display.set_caption('Colosseum Fighter')

INCREMENT = pygame.event.custom_type()
run = True
clock = pygame.time.Clock()

pygame.time.set_timer(INCREMENT, 250)

gameObjects = []
