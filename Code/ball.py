import pygame as pg
import math

class ballClass:
    def __init__(self):
        self.reset()
        self.rect = None
    def reset(self):
        self.x = 1920/2
        self.y = 1080/2
        self.timer = 0
        self.direction = math.pi / 2
        self.speed = 45
        self.offscreen = False
    def draw(self, window):
        self.rect = pg.draw.rect(window.screen, (255, 255, 255), (self.x - 30, self.y - 30, 60, 60))
    def render(self, window, gameState):
        if gameState == "pause":
            self.timer += window.tick
            if self.timer < 600:
                self.draw(window)
            elif self.timer > 1100:
                self.timer = 0
        elif gameState == "play":
            self.draw(window)
            self.timer += window.tick
            self.x += math.cos(self.direction) * self.speed / window.tick
            self.y += math.sin(self.direction) * self.speed / window.tick
            if self.x < 130 or self.x > 1790 and self.timer > 200:
                self.direction = math.pi - self.direction
                self.timer = 0
            if self.y < -30 or self.y > 1120:
                self.offscreen = True
        elif gameState == "score":
            self.timer = 0
