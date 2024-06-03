import pygame, constants


win = pygame.display.set_mode(constants.SIZE)
pygame.display.set_caption('Colosseum Fighter')

ENEMY_RATE = pygame.event.custom_type()
INCREMENT = pygame.event.custom_type()
INCREMENTa = pygame.event.custom_type()
run = True
clock = pygame.time.Clock()

pygame.time.set_timer(INCREMENT, 250)
pygame.time.set_timer(INCREMENTa, 100)
pygame.time.set_timer(ENEMY_RATE, 10000)

score = 0
gameObjectCount = 0
gameObjects = []
