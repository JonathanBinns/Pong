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
        self.speed = 40
    def draw(self, window):
        self.rect = pg.draw.rect(window.screen, (255, 255, 255), (self.x - 30, self.y - 30, 60, 60))
    def render(self, window, gameState = "idle"):
        if gameState == "idle":
            self.timer += window.tick
            if self.timer < 600:
                self.draw(window)
            elif self.timer > 1100:
                self.timer = 0
        if gameState == "play":
            self.draw(window)
            self.x += math.cos(self.direction) * self.speed / window.tick
            self.y += math.sin(self.direction) * self.speed / window.tick
            if self.x < 130 or self.x > 1790:
                self.direction = math.pi - self.direction
