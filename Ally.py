import time
import pygame
from random import uniform as rand


from Bullet import Bullet
from Identity import Identity
from Playable import Playable
import random


class Ally(Playable):
    def __init__(self,  x: int, y: int):
        super().__init__(x, y, 1)
        self.color = (0,255,0)
        self.lastId = 0

    def shoot(self):
        if time.time() < self.nextShoot:
            return
        self.nextShoot = time.time()+rand(0, 2.5)
        self.lastId = self.x+self.y
        return Bullet(self.x+self.width/2+self.xDeslocation,self.y+self.height+self.yDeslocation, self.ammoDirection, self.x+self.y)

    def watchEnvironment(self, allies: Playable, enemys: Playable, bullets: Identity):
        for bullet in bullets:
            x = bullet.x
            y = bullet.y
            width = bullet.width
            xDeslocation = bullet.xDeslocation
            yDeslocation = bullet.yDeslocation
            if bullet.x+bullet.xDeslocation >= self.x+self.xDeslocation-self.width and bullet.x+bullet.xDeslocation+width <= self.x+self.xDeslocation+self.width+self.width:
                if y+yDeslocation >= self.y-self.height and y+yDeslocation <= self.y+self.height*2 and bullet.id != self.lastId:
                    self.xDeslocation*=-1
                    break

