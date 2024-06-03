import pygame, sys, constants, os, manager, math

BG = pygame.transform.scale_by(pygame.image.load(os.path.join('graphics', 'bg.png')), constants.F)
pygame.font.init()

def loadBG():
  manager.win.blit(BG, (0, 0))
  pygame.transform.scale(manager.win, (480*constants.F, 270*constants.F))
  pass

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
  
fnt = pygame.font.SysFont("comicsans", 40)

def updateUI(obj):
  loadBG()
  loadBar(obj[0], 60, 40)

def loadBar(obj, x, y):
  pygame.draw.rect(pygame.display.get_surface(), (85, 27, 27), (x, y-10*constants.F, obj.life * (10 / obj.MAX_HP)*constants.F, 5*constants.F/2))
  pygame.draw.rect(pygame.display.get_surface(), (247, 58, 58), (x, y-10*constants.F, obj.life * (10 / obj.MAX_HP)*constants.F, 13/4*constants.F/2))
  pygame.draw.rect(pygame.display.get_surface(), (255, 255, 255), (x, y-10*constants.F, obj.life * (10 / obj.MAX_HP)*constants.F, 6/4*constants.F/2))
  pygame.draw.rect(pygame.display.get_surface(), (0, 0, 0, 0), (x, y-10*constants.F, 10*constants.F, 20*constants.F/2), 3)

def loadBarP(obj, x, y):
  pygame.draw.circle(pygame.display.get_surface(), (247, 58, 58), (x-30, y+5*constants.F), 10*constants.F)
  pygame.draw.circle(pygame.display.get_surface(), (0, 0, 0), (x-30, y+5*constants.F), 10*constants.F, 5)
  txt = fnt.render(str(obj.lives), False, (255, 255, 255))
  pygame.display.get_surface().blit(txt, (x-25-5*constants.F, y-5*constants.F))

  pygame.draw.rect(pygame.display.get_surface(), (85, 27, 27), (x+10*constants.F, y, obj.life * (100 / obj.MAX_HP)*constants.F, 20*constants.F/2))
  pygame.draw.rect(pygame.display.get_surface(), (247, 58, 58), (x+10*constants.F, y, obj.life * (100 / obj.MAX_HP)*constants.F, 13*constants.F/2))
  pygame.draw.rect(pygame.display.get_surface(), (255, 255, 255), (x+10*constants.F, y, obj.life * (100 / obj.MAX_HP)*constants.F, 6*constants.F/2))
  pygame.draw.rect(pygame.display.get_surface(), (0, 0, 0, 0), (x+10*constants.F, y, 100*constants.F, 20*constants.F/2), 3)

def dist(o1, o2):

  x = o1.x - o2.x
  y = o1.y - o2.y
  z = x**2 + y**2

  return math.sqrt(z)

def rd(obj):
    delta_x = obj.x - manager.gameObjects[0].x
    if delta_x < 0:
      return 1
    elif delta_x > 0:
      return -1
    return 0
def rp(obj):
  delta_y = obj.y - manager.gameObjects[0].y
  if delta_y < 0:
    return 1
  elif delta_y > 0:
    return -1
  return 0
  