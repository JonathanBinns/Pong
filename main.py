from Code.window import windowClass
from Code.paddle import paddleClass
from Code.ball import ballClass

window = windowClass()
window.rename("Pong")
player = paddleClass()
enemy = paddleClass("NPC")
ball = ballClass()

while window.isRunning():
    window.processing()
    window.screen.fill((70, 60, 150))
    ball.render(window)
    player.render(window)
    enemy.render(window, ball)
