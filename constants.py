import pygame, math
pygame.display.init()

specs = pygame.display.Info()

LIVES = 5
SIZE = (specs.current_w, specs.current_h)
F = (specs.current_w/480)
VELOCITY = 5/480*specs.current_w

H_B = [0, 480*F*0.94] #Horizontal Bound
V_B = [270*F*0.28, 270*F*0.92] #Vertical Bound

animationNum = 0