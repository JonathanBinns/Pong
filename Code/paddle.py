import pygame as pg
import math
from random import randint

# paddleClass provides the physics and the rendering for both paddles
# they are differentiated by a string value passed in initialization, which is then saved to a class attribute
# passing windowClass as an argument makes drawing to the window as well as interacting with the other objects very simple
class paddleClass:
    # initialization involves defining the rect attribute, saving the paddle type, and resetting all the values to default
    def __init__(self, type = "player"):
        self.type = type
        self.rect = None
        self.reset()
    # resetting the paddle puts it back in the center of the screen with all the collision information set for the game
    def reset(self):
        self.x = 1920/2
        self.y = 1080/8
        if self.type == "player":
            self.y += 6 * 1080/8
        self.speed = 0
        self.collisionTimer = 1000
    # putting the drawing of the paddle into its own function makes it consistent and easy to change
    # this is important because of how complex the pygame.draw function is
    def draw(self, window):
        self.rect = pg.draw.rect(window.screen, (255, 255, 255), (self.x - 200, self.y - 30, 400, 60))
    # render is the main function of the object
    # it neatly organizes the other functions and packages them to be easily called together
    def render(self, window, ball, gameState):
        if gameState == "play":
            self.physics(window, ball, gameState)
            self.collisionHandler(window, ball)
        self.draw(window)
    # physics is obviously a really important part of the object
    # both the player and NPC paddles have movement speeds based on the window clock through tick
    # they differ in their control, one being controlled by keypressses and one by chasing the ball
    def physics(self, window, ball, gameState):
        tick = window.tick
        accConst = 5
        acc = 0
        if self.type == "player":
            if window.input["a"]:
                acc -= accConst / tick
            if window.input["d"]:
                acc += accConst / tick
        else:
            if gameState == "play":
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
    # collisionHandler uses the pygame colliderect function to handle collisions with the ball
    # it directly changes the ball object attributes, keeping collisions simple
    def collisionHandler(self, window, ball):
        self.collisionTimer += window.tick
        if ball.rect.colliderect(self.rect) and self.collisionTimer > 800:
            difference = self.x - ball.x
            random_skew = randint(-40, 40)
            if self.type == "player":
                difference *= -1
            if ball.direction > 0 and ball.direction < math.pi:
                ball.direction = math.pi * 1.5 + (difference + random_skew) / 230
            else:
                ball.direction = math.pi / 2 + (difference + random_skew) / 230
            if ball.speed < 200:
                ball.speed *= 1.035
            self.collisionTimer = 0
