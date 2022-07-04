from Code.window import windowClass
#from Code.paddle import paddleClass

window = windowClass()
window.rename("Pong")

while window.isRunning():
    window.processing()
    window.screen.fill((0, 90, 0))
