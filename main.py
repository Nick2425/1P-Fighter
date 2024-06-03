import pygame, sys, functions, classes, constants, manager, random
from pygame.locals import QUIT

pygame.init()
player = classes.Player(50, 50)
manager.gameObjects.append(player)

while manager.run:
    pygame.time.delay(50)
    manager.clock.tick()
    for event in pygame.event.get():
        if event.type == manager.ENEMY_RATE:
            F = constants.F
            u = random.randint(1,3)
            for g in range(1, u+1):
                j = random.randint(1,3)
                d = classes.Enemy(150*F, 150*F, 50, 50, 5, j)
            manager.gameObjects.append(d)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == manager.INCREMENT:
            constants.animationNum += 1
        if event.type == manager.INCREMENTa:
            if player.attack == True and player.aanim <= 3:
                print(player.aanim)
                player.aanim += 1
                if player.aanim > 3:
                    player.attack = False
                    player.aanim = 0

    pygame.display.update()
    functions.updateUI(manager.gameObjects)
    for obj in manager.gameObjects:
        obj.move()
