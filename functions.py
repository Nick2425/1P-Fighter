import pygame, sys, constants, os, manager, math

BG = pygame.transform.scale_by(
    pygame.image.load(os.path.join('graphics', 'bg.png')), constants.F)
pygame.font.init()


def getHS(score):
  file = open("data.txt", 'r')
  x = file.readline()
  if int(x) >= int(score):
    return "Game Over! Score " + str(score)
  elif int(x) < int(score):
    file.close()
    file = open("data.txt", "w")
    file.write(str(score))
    file.close()
    return "New High Score! " + str(score)


def loadBG():
  manager.win.blit(BG, (0, 0))
  pygame.transform.scale(manager.win, (480 * constants.F, 270 * constants.F))
  pass


def horizontal():  #Explained in documentation.
  keys = pygame.key.get_pressed()
  if keys[pygame.K_a] or keys[pygame.K_LEFT]:
    return -1
  elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
    return 1
  else:
    return 0


def vertical():  # Explained in documentation.
  keys = pygame.key.get_pressed()
  if keys[pygame.K_w] or keys[pygame.K_UP]:
    return -1
  elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
    return 1
  else:
    return 0


fnt = pygame.font.SysFont("comicsans", 40)

F = constants.F
def updateUI(obj):
  loadBG()
  for x in obj:
    if x != obj[0] and x.bullet != True:
      if x.health != x.max_health:
        loadBar(x, x.x, x.y)
  loadBarP(obj[0], 10*F, 10*F)


# Loads four rectangles displaying health information.
def loadBar(obj, x, y):
  pygame.draw.rect(pygame.display.get_surface(), (85, 27, 27),
                   (x - 10 * constants.F, y - 5 * constants.F, obj.health *
                    (50 / obj.max_health) * constants.F, 10 * constants.F / 2))
  pygame.draw.rect(
      pygame.display.get_surface(), (247, 58, 58),
      (x - 10 * constants.F, y - 5 * constants.F, obj.health *
       (50 / obj.max_health) * constants.F, 6.5 * constants.F / 2))
  pygame.draw.rect(pygame.display.get_surface(), (255, 255, 255),
                   (x - 10 * constants.F, y - 5 * constants.F, obj.health *
                    (50 / obj.max_health) * constants.F, 3 * constants.F / 2))
  pygame.draw.rect(pygame.display.get_surface(), (0, 0, 0, 0),
                   (x - 10 * constants.F, y - 5 * constants.F,
                    50 * constants.F, 10 * constants.F / 2), 3)


def loadBarP(obj, x, y):
  # Creates a rendered font and prints it.
  t = open("data.txt", "r")  # Get HS
  h = t.readline()
  text("High Score:" + str(h), x + 5 * constants.F, 40 * constants.F, 40)
  text("Score:" + str(manager.score), x + 5 * constants.F, 60 * constants.F, 40)
  t.close()
  s = 1.2
  pygame.draw.rect(pygame.display.get_surface(), (85, 27, 27), (5*constants.F, y, obj.life*(100 / obj.MAX_HP) * constants.F, 20 * constants.F / s))
  pygame.draw.rect(pygame.display.get_surface(), (247, 58, 58), (5*constants.F, y, obj.life*(100 / obj.MAX_HP) * constants.F, 13 * constants.F / s))
  pygame.draw.rect(pygame.display.get_surface(), (255, 255, 255), (5*constants.F, y, obj.life*(100 / obj.MAX_HP) * constants.F, 6 * constants.F / s))
  pygame.draw.rect(pygame.display.get_surface(), (0, 0, 0, 0), (5*constants.F, y, 100 * constants.F, 20 * constants.F / s), 3)


# Distance function
def dist(o1, o2):

  x = o1.x - o2.x
  y = o1.y - o2.y
  z = x**2 + y**2

  return math.sqrt(z)


# Direction function -- for enemies.
def rd(obj):
  # manager.gameObjects[0].y potential issue
  delta_x = obj.x - (manager.gameObjects[0].x - 7.5 * constants.F)
  if delta_x < 0:
    return 1
  elif delta_x > 0:
    return -1
  return 0


# Direction, for y-coordinates -- for enemies.
def rp(obj):
  delta_y = obj.y - (manager.gameObjects[0].y - 7.5 * constants.F)
  if delta_y < 0:
    return 1
  elif delta_y > 0:
    return -1
  return 0


# Sorts all objects
def sortObjects(list):
  list2 = list
  alt = sorted(list2, key=lambda x: x.y)
  for x in alt:
    x.move()


# adds velocity to objects.
def push(obj, obj2, v):
  delta_X = obj.x - obj2.x
  if delta_X < 0:
    obj.x -= v
  else:
    obj.x += v


# Displays text.
def text(string, x, y, fontsize):

  f0nt = pygame.font.SysFont('Calibri', int(fontsize / 3.2 * constants.F),
                             True, True)
  size = pygame.font.Font.size(f0nt, string)

  pygame.draw.rect(pygame.display.get_surface(), (153, 152, 95),
                   (x - 15 * constants.F, y - 15 * constants.F,
                    size[0] + 7.5 * constants.F, size[1] + 7.5 * constants.F))
  pygame.draw.rect(pygame.display.get_surface(), (48, 48, 0),
                   (x - 15 * constants.F, y - 15 * constants.F,
                    size[0] + 7.5 * constants.F, size[1] + 7.5 * constants.F),
                   5)
  txt = f0nt.render(string, False, (255, 255, 255))
  pygame.display.get_surface().blit(
      txt, (x - 10 * constants.F, y - 10 * constants.F))


def exit():
  manager.run = False
