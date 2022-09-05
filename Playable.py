import time
import pygame
from random import uniform as rand
from Bullet import Bullet
from Identity import Identity
from threading import Thread


class Playable(Identity):
    def __init__(self, x, y):
        super(x, y)
        self.nextShoot = time.time() + 1.5

    def shoot(self):
        if time.time() >= self.nextShoot:
            return
        self.nextShoot = rand(0, 2.5)
        return Bullet()


    def runFunction(self):
        while self.health > 0:
            self.move()
            self.shoot()
            self.draw()

    def run(self):
        Thread(target=self.runFunction).start()