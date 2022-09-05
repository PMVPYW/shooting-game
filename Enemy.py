import time
import pygame

from Playable import Playable


class Enemy(Playable):
    def __init__(self,  x, y):
        super().__init__(x, y)
        self.color = (255,0,0)
