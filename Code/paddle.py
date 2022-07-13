import pygame as pg
import math

class paddleClass:
    def __init__(self, type = "player"):
        self.type = type
        self.rect = None
        self.reset()
    def reset(self):
        self.x = 1920/2
        self.y = 1080/8
        if self.type == "player":
            self.y += 6 * 1080/8
        self.speed = 0
        self.collisionTimer = 1000
    def draw(self, window):
        self.rect = pg.draw.rect(window.screen, (255, 255, 255), (self.x - 200, self.y - 30, 400, 60))
    def render(self, window, ball, gameState):
        if gameState == "play":
            self.physics(window, ball)
            self.collisionHandler(window, ball)
        self.draw(window)
    def physics(self, window, ball):
        tick = window.tick
        accConst = 5
        acc = 0
        if self.type == "player":
            if window.input["a"]:
                acc -= accConst / tick
            if window.input["d"]:
                acc += accConst / tick
        else:
            if ball.x - 100 > self.x:
                acc += accConst / tick
            if ball.x + 100 < self.x:
                acc -= accConst / tick
        if self.x < 300:
            self.x = 300
        elif self.x > 1620:
            self.x = 1620
        self.speed += acc
        self.x += self.speed
        self.speed *= 0.9
    def collisionHandler(self, window, ball):
        self.collisionTimer += window.tick
        if ball.rect.colliderect(self.rect) and self.collisionTimer > 800:
            difference = self.x - ball.x
            if self.type == "player":
                difference *= -1
            ball.direction += math.pi + (difference / 240)
            if ball.speed < 120:
                ball.speed *= 1.07
            self.collisionTimer = 0
