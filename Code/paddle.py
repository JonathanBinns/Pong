import pygame as pg

class paddleClass:
    def __init__(self, type = "player"):
        self.x = 1920/2
        self.y = 1080/8
        if type == "player":
            self.y += 6 * 1080/8
        self.type = type
        self.clock = pg.time.Clock()
    def render(self, window, ball = None):
        tick = self.clock.tick(60)
        pg.draw.rect(window.screen, (255, 255, 255), (self.x - 200, self.y - 30, 400, 60))
        if self.type == "player":
            if window.input["a"] and self.x > 300:
                self.x -= 400 / tick
            if window.input["d"] and self.x < 1620:
                self.x += 400 / tick
        else:
            if ball.x > self.x and self.x > 300:
                self.x += 400 / tick
            if ball.x < self.x and self.x < 1620:
                self.x -= 400 / tick
