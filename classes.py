import pygame, sys, functions, constants, manager, os

playerRight = [pygame.transform.scale_by(pygame.image.load(os.path.join('graphics/cb/cb-splice', 'row-2-column-' + str(i) + '.png')), 1.5*constants.F) for i in range(1,5)]
playerLeft = [pygame.transform.scale_by(pygame.image.load(os.path.join('graphics/cb/cb-splice', 'row-4-column-' + str(i) + '.png')), 1.5*constants.F) for i in range(1,5)]
playerARight = [pygame.transform.scale_by(pygame.image.load(os.path.join('graphics/cb/cb-attack-splice', 'row-3-column-' + str(i) + '.png')), 1.5*constants.F) for i in range(1,5)]
playerALeft = [pygame.transform.scale_by(pygame.image.load(os.path.join('graphics/cb/cb-attack-splice', 'row-4-column-' + str(i) + '.png')), 1.5*constants.F) for i in range(1,5)]

class Player():

  def __init__(self, x, y):
    self.x = constants.specs.current_w/2
    self.y = constants.specs.current_h/2
    self.lives = constants.LIVES
    self.MAX_HP = 10
    self.life = self.MAX_HP
    self.attack = False
    self.aanim = 0  # Attack Animation
    self.v = constants.VELOCITY  # Velocity
    self.surf = pygame.display.get_surface()
    self.dir = 'r'
    self.HSTILL = True

  def Attack(self):
    
    self.attack = True
    self.attackAnimation()

    self.detect()

  def move(self):
    if (pygame.key.get_pressed()[pygame.K_SPACE]) or self.attack == True:
      self.Attack()
    if self.attack != True:
      self.HSTILL = False

      if self.x + functions.horizontal() * self.v > constants.H_B[0] and self.x + functions.horizontal() * self.v < constants.H_B[1]:
        self.x += functions.horizontal() * self.v
      if self.y + functions.vertical() * self.v > constants.V_B[0] and self.y + functions.vertical() * self.v < constants.V_B[1]:
        self.y += functions.vertical() * self.v

      if functions.horizontal() < 0:
        self.dir = 'l'
      elif functions.horizontal() > 0:
        self.dir = 'r'
      elif functions.vertical() == 0:
        self.HSTILL = True

      self.draw()

  def draw(self):
    #pygame.draw.rect(surf, (0, 255, 0), (self.x, self.y, 50, 50))
    if self.dir == 'r' and self.HSTILL == False:
      self.surf.blit(playerRight[constants.animationNum%4], (self.x, self.y))
    elif self.dir == 'l' and self.HSTILL == False:
      self.surf.blit(playerLeft[constants.animationNum%4], (self.x, self.y)) 
    if self.dir == 'r' and self.HSTILL == True:
      self.surf.blit(playerRight[0], (self.x, self.y))
    elif self.dir == 'l' and self.HSTILL == True:
      self.surf.blit(playerLeft[0], (self.x, self.y))

  def attackAnimation(self):
    if self.dir == 'r':
      self.surf.blit(playerARight[self.aanim], (self.x-17, self.y))
    elif self.dir == 'l':
      self.surf.blit(playerALeft[self.aanim], (self.x-17, self.y))

  def detect(self):
    pass

class Enemy():
  pass