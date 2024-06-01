import pygame, sys, functions, classes, constants, manager
from pygame.locals import QUIT

pygame.init()
player = classes.Player(50, 50)
manager.gameObjects.append(player)

while manager.run:
    pygame.time.delay(50)
    manager.clock.tick()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == manager.INCREMENT:
            constants.animationNum += 1
            if player.attack == True and player.aanim <= 3:
                print(player.aanim)
                player.aanim += 1
                if player.aanim > 3:
                    player.attack = False
                    player.aanim = 0

    pygame.display.update()
    functions.updateUI(manager.gameObjects)
    player.move()
