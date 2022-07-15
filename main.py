from Code.window import windowClass
from Code.paddle import paddleClass
from Code.ball import ballClass

window = windowClass()
window.rename("Pong")
player = paddleClass()
enemy = paddleClass("NPC")
ball = ballClass()
gameState = "pause"
scoreDelay = 0

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
