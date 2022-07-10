import pygame as pg

class ballClass:
    def __init__(self):
        self.x = 1920/2
        self.y = 1080/2
    def render(self, window):
        self.x -= 10
