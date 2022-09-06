import time
import pygame
from random import uniform as rand
from Bullet import Bullet
from Identity import Identity


class Playable(Identity):
    def __init__(self, x, y, ammoDir: int):
        super().__init__(x, y)
        self.nextShoot = time.time() + 0.5
        self.ammoDirection = ammoDir
        self.lastId = 0

    def shoot(self):
        if time.time() < self.nextShoot:
            return
        self.nextShoot = time.time()+rand(1, 2.5)
        return Bullet(self.x+self.width/2,self.y, self.ammoDirection, 0)


    def runFunction(self, screen, enemys):
        if self.health > 0:
            self.draw(screen)
            if len(enemys) != 0:
                self.move()
                return self.shoot()

    def run(self, screen, enemys):
        return self.runFunction(screen, enemys)

