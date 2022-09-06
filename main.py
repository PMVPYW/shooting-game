import random
import pyautogui
import pygame
import time

from Player import Player
from general import colision
from Ally import Ally
from Enemy import Enemy

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
ORANGE = (255,255,0)

width, height = pyautogui.size()
screen = pygame.display.set_mode((width, height))

def game():

    allies = []
    bullets = []
    enemies = []

    for x in range(5):
        allies.append(Ally(x*width/5,x*100))
    #allies.append(Ally(500, 200))
    '''for x in range(5):
        enemies.append(Enemy(100*x,height-x*100+25))'''



    spawned = False
    begin = time.time()
    t_health = 100*len(allies)
    kills = 0
    player = Player(width/2, height/4)
    while t_health != 0:
        #events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_LEFT:
                    player.xDeslocation = -5
                if event.key == pygame.K_RIGHT:
                    player.xDeslocation = 5
                if event.key == pygame.K_UP:
                    player.yDeslocation = -5
                if event.key == pygame.K_DOWN:
                    player.yDeslocation = 5
                if event.key == pygame.K_SPACE:
                    bullet = player.shoot()
                    if bullet != None:
                         bullets.append(bullet)

        screen.fill(BLACK)

        #identities running
        t_health = player.health
        for x in allies:
            t_health += x.health
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

        player.run(screen, enemies)

        #colision detection
        for y in bullets:
            for x in enemies:
                if colision(x, y):
                    x.die()
                    enemies.remove(x)
                    bullets.remove(y)
                    kills+=1

            for x in allies:
                if colision(x, y):
                    x.die()
                    bullets.remove(y)

            if colision(player, y):
                player.die()




        current = time.time()-begin
        if int(current) % 5 == 0:
            if not spawned:
                enemies.append(Enemy(random.randint(0, width), random.randint(height/2, height)))
            spawned = True
        else:
            spawned = False
        pygame.display.update()

if __name__ == "__main__":
    game()