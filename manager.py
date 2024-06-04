import pygame, constants


win = pygame.display.set_mode(constants.SIZE)
pygame.display.set_caption('Colosseum Fighter')

# Custom pygame events.
ENEMY_RATE = pygame.event.custom_type()
INCREMENT = pygame.event.custom_type()
INCREMENTa = pygame.event.custom_type()

randTick = 0 # This is a random chance # generated every tick, used to generate enemy attacks.
run = True
clock = pygame.time.Clock()

# Setting the infinite timers.
pygame.time.set_timer(INCREMENT, 250)
pygame.time.set_timer(INCREMENTa, 100)
pygame.time.set_timer(ENEMY_RATE, 8000)

score = 0
gameObjectCount = 0
gameObjects = []
bulletList = []
