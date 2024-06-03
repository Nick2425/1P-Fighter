from _typeshed import Self
import pygame, sys, functions, constants, manager, os, math

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
    self.damage = 4

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

Enemy1R = [pygame.transform.scale_by(pygame.image.load(os.path.join('graphics/other/e1', 'row-3-column-' + str(i) + '.png')), 1*constants.F) for i in range(1,5)]
Enemy1L = [pygame.transform.scale_by(pygame.image.load(os.path.join('graphics/other/e1', 'row-2-column-' + str(i) + '.png')), 1*constants.F) for i in range(1,5)]
Enemy2R = [pygame.transform.scale_by(pygame.image.load(os.path.join('graphics/other/e2', 'row-3-column-' + str(i) + '.png')), 1*constants.F) for i in range(1,5)]
Enemy2L = [pygame.transform.scale_by(pygame.image.load(os.path.join('graphics/other/e2', 'row-2-column-' + str(i) + '.png')), 1*constants.F) for i in range(1,5)]
Enemy3R = [pygame.transform.scale_by(pygame.image.load(os.path.join('graphics/other/e3', 'row-3-column-' + str(i) + '.png')), 1*constants.F) for i in range(1,5)]
Enemy3L = [pygame.transform.scale_by(pygame.image.load(os.path.join('graphics/other/e3', 'row-2-column-' + str(i) + '.png')), 1*constants.F)  for i in range(1,5)]

class Enemy():

  def __init__(self, x, y, health, damage, speed, type):
    self.x = x
    self.y = y
    self.health = health
    self.max_health = health
    self.v = pygame.math.Vector2(0,0)
    self.speed = speed
    self.damage = damage
    self.surface = pygame.display.get_surface()
    self.attackB = False
    self.dir = 'r'
    self.type = type
  def move(self):
    self.v.x = self.speed * functions.rd(self)
    self.v.y = self.speed * functions.rp(self)
    if self.v.x < 0:
      self.dir = 'l'
    elif self.v.x > 0:
      self.dir = 'r'
    if self.attackB != True:
      self.x += self.v.x
      self.y += self.v.y
    self.draw()
  def draw(self): #LEFT = 4 # RIGHT = 3
    if self.type == 1:
      if self.dir == 'r':
        self.surface.blit(Enemy1R[constants.animationNum % 4], (self.x, self.y))
      elif self.dir == 'l':
          self.surface.blit(Enemy1L[constants.animationNum % 4], (self.x, self.y))
    elif self.type == 2:
      if self.dir == 'r':
        self.surface.blit(Enemy2R[constants.animationNum % 4], (self.x, self.y))
      elif self.dir == 'l':
          self.surface.blit(Enemy2L[constants.animationNum % 4], (self.x, self.y))
    elif self.type == 3:
      if self.dir == 'r':
        self.surface.blit(Enemy3R[constants.animationNum % 4], (self.x, self.y))
      elif self.dir == 'l':
          self.surface.blit(Enemy3L[constants.animationNum % 4], (self.x, self.y))
    pass




# Bullet Row 1 25-29
BulletR = [pygame.transform.scale_by(pygame.image.load(os.path.join('graphics/other/wata', 'row-1-column-' + str(24+i) + '.png'))) for i in range(1,5)]
BulletL = [pygame.transform.scale_by(pygame.transform.flip(pygame.image.load(os.path.join('graphics/other/wata', 'row-1-column-' + str(24+i) + '.png')), True, False), constants.F) for i in range(1,5)]

class Bullet():
  def __init__(self, parent, x, y, speed, dir, damage):
    self.x = x
    self.y = y
    self.speed = speed
    self.dir = dir
    self.surface = pygame.display.get_surface()
    self.damage = 5
    self.v = pygame.math.Vector2(0,0)
    self.parent = parent

  def move(self):
    if self.dir == 'r':
      self.v.x = self.speed
    elif self.dir == 'l':
      self.v.x = -self.speed
    self.x += self.v.x
    self.detect()
    self.draw()

  def draw(self):
    if self.dir == 'r':
      self.surface.blit(BulletR[constants.animationNum % 4], (self.x, self.y))
    elif self.dir == 'l':
      self.surface.blit(BulletL[constants.animationNum % 4], (self.x, self.y))

  def detect():
    d = functions.dist(manager.gameObjects[0], self)
    if d < 40 * constants.F:
      manager.gameObjects.remove(self)
      manager.gameObjects[0].health -= self.damage
      self.parent.aTimer = False
      #!! ## = pygame.event.custom_type()
      pygame.time.set_timer(aTimer, )
      
      del self

      
      