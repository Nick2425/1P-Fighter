import pygame, sys, constants


def horizontal():
  keys = pygame.key.get_pressed()
  if keys[pygame.K_a] or keys[pygame.K_LEFT]:
    return -1
  elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
    return 1
  else:
    return 0

def vertical():
  keys = pygame.key.get_pressed()
  if keys[pygame.K_w] or keys[pygame.K_UP]:
    return -1
  elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
    return 1
  else:
    return 0
