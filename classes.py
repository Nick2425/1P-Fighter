import pygame, sys, functions, constants, manager, os, math

# Import the player textures.
playerRight = [pygame.transform.scale_by(pygame.image.load(os.path.join('graphics/cb/cb-splice', 'row-2-column-' + str(i) + '.png')), 1.5*constants.F) for i in range(1,5)]
playerLeft = [pygame.transform.scale_by(pygame.image.load(os.path.join('graphics/cb/cb-splice', 'row-4-column-' + str(i) + '.png')), 1.5*constants.F) for i in range(1,5)]
playerARight = [pygame.transform.scale_by(pygame.image.load(os.path.join('graphics/cb/cb-attack-splice', 'row-3-column-' + str(i) + '.png')), 1.5*constants.F) for i in range(1,5)]
playerALeft = [pygame.transform.scale_by(pygame.image.load(os.path.join('graphics/cb/cb-attack-splice', 'row-4-column-' + str(i) + '.png')), 1.5*constants.F) for i in range(1,5)]

class Player():

  def __init__(self, x, y):
    manager.gameObjectCount += 1
    manager.gameObjects.append(self)
    self.num = manager.gameObjectCount
    self.x = constants.specs.current_w/2
    self.y = constants.specs.current_h/2
    self.lives = constants.LIVES
    self.MAX_HP = 100
    self.life = self.MAX_HP
    self.attack = False
    self.aanim = 0  # Attack Animation
    self.v = constants.VELOCITY  # Velocity
    self.surf = pygame.display.get_surface()
    self.dir = 'r'
    self.HSTILL = True
    self.damage = 10
    self.count = 0

  def Attack(self):
    self.attack = True
    self.attackAnimation()
    if self.count < 2: # Maximum of two objects hit at once.
      self.count += 1
      try:
        self.detect() # Incase it returned an error.
      except:
        print("L35")

  # Moves character.
  def move(self):
    if self.life <= 0: # Checks if the player is dead or not.
      functions.exit()
    if (pygame.key.get_pressed()[pygame.K_SPACE]) or self.attack == True:
      self.Attack()
    if self.attack != True:
      self.HSTILL = False

      # Moves the player in respective direction.
      if self.x + functions.horizontal() * self.v > constants.H_B[0] and self.x + functions.horizontal() * self.v < constants.H_B[1]:
        self.x += functions.horizontal() * self.v
      if self.y + functions.vertical() * self.v > constants.V_B[0] and self.y + functions.vertical() * self.v < constants.V_B[1]:
        self.y += functions.vertical() * self.v

      if functions.horizontal() < 0: # !! Determines the direction of the player.
        self.dir = 'l'
      elif functions.horizontal() > 0:
        self.dir = 'r'
      elif functions.vertical() == 0:
        self.HSTILL = True

      self.draw()

  def draw(self):
    #pygame.draw.rect(surf, (0, 255, 0), (self.x, self.y, 50, 50))
    if self.dir == 'r' and self.HSTILL == False: # Displays the player walking animation in respective directions.
      self.surf.blit(playerRight[constants.animationNum%4], (self.x, self.y))
    elif self.dir == 'l' and self.HSTILL == False:
      self.surf.blit(playerLeft[constants.animationNum%4], (self.x, self.y)) 
    if self.dir == 'r' and self.HSTILL == True:
      self.surf.blit(playerRight[0], (self.x, self.y))
    elif self.dir == 'l' and self.HSTILL == True:
      self.surf.blit(playerLeft[0], (self.x, self.y))

  # Prints attack anim.
  def attackAnimation(self): # Displays attack animation in respective directions.
    if self.dir == 'r':
      self.surf.blit(playerARight[self.aanim], (self.x-17, self.y))
    elif self.dir == 'l':
      self.surf.blit(playerALeft[self.aanim], (self.x-17, self.y))
  def detect(self):
    try:
      for obj in manager.gameObjects:
        if obj != self:
          d = functions.dist(obj, self) # Error here?
          if d < 30*constants.F: # If there is an object less than 30*F pixels away.
            print("Found")
            obj.health -= self.damage # Remove the damage etc.
            functions.push(obj, self, 15*constants.F) # Push the enemy away.
            if obj.health <= 0: # Check if it is less than zero health.
              if obj.bullet != True:
                manager.score += 1 # Add 1 to score if not a bullet.
                if self.life + 2 <= 100: 
                  self.life += 2
              delBullet(obj) # Delete the enemy from bullet list just in case.

    except:
      print("L76-93 Group")

    pass

# !! This is the enemy pictures.
Enemy1R = [pygame.transform.scale_by(pygame.image.load(os.path.join('graphics/other/e1', 'row-3-column-' + str(i) + '.png')), 1*constants.F) for i in range(1,5)]
Enemy1L = [pygame.transform.scale_by(pygame.image.load(os.path.join('graphics/other/e1', 'row-2-column-' + str(i) + '.png')), 1*constants.F) for i in range(1,5)]
Enemy2R = [pygame.transform.scale_by(pygame.image.load(os.path.join('graphics/other/e2', 'row-3-column-' + str(i) + '.png')), 1*constants.F) for i in range(1,5)]
Enemy2L = [pygame.transform.scale_by(pygame.image.load(os.path.join('graphics/other/e2', 'row-2-column-' + str(i) + '.png')), 1*constants.F) for i in range(1,5)]
Enemy3R = [pygame.transform.scale_by(pygame.image.load(os.path.join('graphics/other/e3', 'row-3-column-' + str(i) + '.png')), 1*constants.F) for i in range(1,5)]
Enemy3L = [pygame.transform.scale_by(pygame.image.load(os.path.join('graphics/other/e3', 'row-2-column-' + str(i) + '.png')), 1*constants.F)  for i in range(1,5)]

class Enemy():

  def __init__(self, x, y, health, damage, speed, type): # Enemy constructor.
    manager.gameObjectCount += 1
    self.num = manager.gameObjectCount
    self.bullet = False
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
    if self.health < 0: # Deletes the enemy if it is less than zero health.
      delObject(self)
    self.attack()
    if self.attackB == False: # Only moves the enemy if it is not attacking.
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

  def draw(self): #LEFT = 4 # RIGHT = 3  # Series of conditions for displaying the enemy in the correct direction. Uses % function for lists.
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
  def attack(self): # Attack function
    if manager.randTick == 1:
      if len(manager.bulletList) <= 3 and self.attackB == False: # If there are less than 4 bullets, and the enemy is not already attacking.
        self.attackB = True # Condition to only attack once.
        x = Bullet(self, self.x+15, self.y+15, 7*constants.F, self.dir, self.damage)
    if manager.randTick < 35: # Chance of around 20%.
      if functions.dist(self, manager.gameObjects[0]) < 20*constants.F: # All below is for collision detection.
        manager.gameObjects[0].life -= self.damage*0.5
        functions.push(manager.gameObjects[0], self, constants.F)

# Bullet Row 1 25-29
BulletR = [pygame.transform.scale_by(pygame.image.load(os.path.join('graphics/other/wata', 'row-1-column-' + str(24+i) + '.png')), 1.5*constants.F) for i in range(1,6)]
BulletL = [pygame.transform.scale_by(pygame.transform.flip(pygame.image.load(os.path.join('graphics/other/wata', 'row-1-column-' + str(24+i) + '.png')), True, False), 1.5*constants.F) for i in range(1,6)]

class Bullet():
  def __init__(self, parent, x, y, speed, dir, damage):

    manager.gameObjectCount += 1
    self.num = manager.gameObjectCount
    self.x = x
    self.y = y
    self.iX = x
    self.speed = speed
    self.dir = dir
    self.health = 5
    self.surface = pygame.display.get_surface()
    self.damage = damage
    self.v = pygame.math.Vector2(0,0)
    self.parent = parent
    self.bullet = True

    manager.bulletList.append(self)
    manager.gameObjects.append(self)

  def move(self):
    if self.dir == 'r':
      self.v.x = self.speed
    elif self.dir == 'l':
      self.v.x = -self.speed
    self.x += self.v.x
    self.detect()
    self.draw()
    
    # Destroys the object after a certain distance. 300*F pixels.
    if abs(self.x - self.iX) > 150*constants.F:
      delBullet(self)

  def draw(self):
    if self.dir == 'r':
      self.surface.blit(BulletR[constants.animationNum % 4], (self.x, self.y))
    elif self.dir == 'l':
      self.surface.blit(BulletL[constants.animationNum % 4], (self.x, self.y))

  def detect(self):
    d = functions.dist(manager.gameObjects[0], self)
    if d < 20 * constants.F:
      manager.gameObjects[0].life -= self.damage
      delBullet(self)

# Because code is repetitive
def delObject(obj):
  if len(manager.gameObjects) != 0:
    for x in manager.gameObjects:
      try:
        if x == obj: 
          manager.gameObjects.remove(x)
          del x
        else:
          print("Object not found")
      except:
        print("Object not found")
      finally:
        print(":0")
def delBullet(obj):
  if len(manager.bulletList) != 0:
    for x in manager.bulletList:
      try:
        if x == obj: 
          print(x.parent)
          x.parent.attackB = False
          manager.bulletList.remove(x)
          manager.gameObjects.remove(x)
          del x
        else:
          print("Object not found")
      except:
        print("Object not found")
      finally:
        print(":0")