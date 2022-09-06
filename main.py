import random
import pyautogui
import pygame
import time
from Ally import Ally
from Enemy import Enemy

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
ORANGE = (255,255,0)

width, height = pyautogui.size()

allies = []
bullets = []
enemies = []

for x in range(5):
    allies.append(Ally(x*width/5,x*100))
#allies.append(Ally(500, 200))
for x in range(5):
    enemies.append(Enemy(100*x,height-x*100+25))

screen = pygame.display.set_mode((width, height))


while 1:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill(BLACK)
    for x in allies:
        bullet = x.run(screen, enemies)
        x.watchEnvironment(allies, enemies, bullets)
        if bullet != None:
            bullets.append(bullet)
    for x in enemies:
        bullet = x.run(screen, enemies)
        if bullet != None:
            bullets.append(bullet)


    for x in bullets:
        x.run(screen)

    if time.time() % 5 == 0:
        enemies.append(Enemy(random.randin(0, width), random.randint(height/2, height)))
    pygame.display.update()