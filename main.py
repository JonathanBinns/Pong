from Code.window import windowClass
from Code.paddle import paddleClass
from Code.ball import ballClass

window = windowClass()
window.rename("Pong")
player = paddleClass()
enemy = paddleClass("NPC")
ball = ballClass()
gameState = "idle"

while window.isRunning():
    window.processing()
    window.screen.fill((50, 70, 140))
    if window.input["spaceT"]:
        if gameState == "idle":
            gameState = "play"
        elif gameState == "play":
            gameState = "idle"
            ball.reset()
            player.reset()
            enemy.reset()
    ball.render(window, gameState)
    player.render(window, ball, gameState)
    enemy.render(window, ball, gameState)
