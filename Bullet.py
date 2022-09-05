import pygame
import time
from threading import Thread



class Bullet:
    def __init__(self):
        self.height = 5
        self.width = 5
        self.color = (255,255,0)
        self.nextMove = time.time()+0.5
        self.exists = True

    def runFunction(self):
        while self.exists:
            self.move()
            self.draw()

    def run(self):
        Thread(target=self.runFunction).start()
