#Name: Nicholas Kuijpers
#Date: Monday, June 10, 2024
#Purpose: Create an interactive GUI, or game.

import pygame, sys, functions, classes, constants, manager, random
from pygame.locals import QUIT

pygame.init()
player = classes.Player(50, 50) # Player Object.

#20 Ticks/Second
while manager.run:
    #Timer
    functions.text(functions.getHS(manager.score), 0.25*constants.SIZE[0], 0.5 * constants.SIZE[1], 50)
    pygame.time.delay(50)
    manager.clock.tick()

    # Random number per tick.
    manager.randTick = random.randint(1, 100)
    for event in pygame.event.get():

        # Enemy Spawn Event
        # !! Issue with spawning ememies and crashing game.
        if event.type == manager.ENEMY_RATE: # Spawns the amount of enemies based on score. Higher score -> Higher amount and difficulty of enemies.
            score = manager.score
            factor = score//12+1
            F = constants.F
            i5 = 0
            u = random.randint(1,3)
            while i5 <= factor: # Factor is the amount of enemies.
                i5 += 1
                j = random.randint(1,3)
                v = random.randint(1,4)
                d = classes.Enemy(240*F+50*j, 110*F+50*v, 11 + 5*factor, 5+2*factor, v*constants.F, j)
                manager.gameObjects.append(d)

        # Standard Quit
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Animation Increment
        if event.type == manager.INCREMENT: # Animation Increment.
            constants.animationNum += 1

        # Attack Animation Increment (Faster)
        if event.type == manager.INCREMENTa: # Attack Animation Increment.
            if player.attack == True and player.aanim <= 3: # If the player is attacking.
                print(player.aanim)
                player.aanim += 1
                if player.aanim > 3: # Reset attack properties.
                    player.attack = False
                    player.aanim = 0
                    player.count = 0

    # Update UI
    pygame.display.update()
    functions.updateUI(manager.gameObjects)

    # Calls the move function for all entities.
    # !! Print objects with the closest y to 0 first.
    functions.sortObjects(manager.gameObjects)
    
# End Game information, displays score and such, then quits.
functions.text(functions.getHS(manager.score), 0.25*constants.SIZE[0], 0.5 * constants.SIZE[1], 50)
pygame.display.update()

pygame.time.delay(3000)
pygame.quit()