import pygame as pg
import math

# ballClass is the structure for the ball object
# it handles physics and rendering of the ball
# being an object makes it more easy to work with and passing windowClass allows for simple rendering
class ballClass:
    # in initialization, the rect attribute is created and all other values are set to default
    def __init__(self):
        self.reset()
        self.rect = None
    # resetting the attributes is important and it makes sense to put that in a function
    def reset(self):
        self.x = 1920/2
        self.y = 1080/2
        self.timer = 0
        self.direction = math.pi / 2
        self.speed = 45
        self.offscreen = False
    # keeping the actual nuts and bolts of rendering in one function allows it to be universally changed without any conflict
    def draw(self, window):
        self.rect = pg.draw.rect(window.screen, (255, 255, 255), (self.x - 30, self.y - 30, 60, 60))
    # render is the main function of the class
    # the three gamestates are seperated by if else blocks
    # physics are taken care of with simple trigonometry and some coordinate checking for the edges of the game
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
            if self.x < 130 or self.x > 1790 and self.timer > 50:
                self.direction = math.pi - self.direction
                self.timer = 0
            if self.y < -30 or self.y > 1120:
                self.offscreen = True
        elif gameState == "score":
            self.timer = 0
