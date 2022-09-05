import time
import pygame

from Playable import Playable


class Enemy(Playable):
    def __init__(self,  x, y):
        super(x, y)
        self.color = (255,0,0)
