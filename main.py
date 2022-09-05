import random

import pygame
from Ally import Ally


BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
ORANGE = (255,255,0)

width = 1920
height = 1080

allies = []
bullets = []
enemies = []

for x in range(5):
    allies.append(Ally(10,20))

pygame.init()
screen = pygame.display.set_mode((width, height))


while 1:
    screen.fill(BLACK)
    for x in allies:
        x.run(screen)
    pygame.display.update()
