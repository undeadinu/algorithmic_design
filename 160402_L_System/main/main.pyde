from renderer import *

renderer = Renderer()

def setup():
    global renderer  
    size(SCREEN_WIDTH, SCREEN_HEIGHT)
    renderer.setup()

def draw():
    global renderer
    renderer.draw()