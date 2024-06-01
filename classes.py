import pygame, sys, functions, constants


class Player():

  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.lives = constants.LIVES
    self.attack = False
    self.aanim = 0  # Attack Animation
    self.v = constants.VELOCITY  # Velocity

  def move(self):
    self.x += functions.horizontal() * self.v
    self.y += functions.vertical() * self.v

  def draw(self, surf):
    pygame.draw.rect(surf, (0, 255, 0), (self.x, self.y, 50, 50))
