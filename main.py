# these are all the imports i need for the game to work
# window handles the window for the program
# the paddle and ball files are code for those objects respectively
from Code.window import windowClass
from Code.paddle import paddleClass
from Code.ball import ballClass

# these are all the local variables and objects
window = windowClass()
window.rename("Pong")
player = paddleClass()
enemy = paddleClass("NPC")
ball = ballClass()
gameState = "pause"
scoreDelay = 0

# the while loop is simple, differentiating between each of the gamestates through elif blocks
while window.isRunning():
    window.processing()
    window.screen.fill((50, 70, 140))
    if gameState == "pause":
        if window.input["spaceT"]:
            gameState = "play"
    elif gameState == "play":
        if ball.offscreen:
            gameState = "score"
            scoreDelay = 0
    elif gameState == "score":
        scoreDelay += window.tick
        if scoreDelay > 1000:
            gameState = "pause"
            ball.reset()
            enemy.reset()
            player.reset()
    ball.render(window, gameState)
    player.render(window, ball, gameState)
    enemy.render(window, ball, gameState)
