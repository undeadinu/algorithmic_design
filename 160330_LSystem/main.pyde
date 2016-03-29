add_library('controlP5')

from renderer import Renderer

renderer = Renderer()

def setup():
    global renderer    
    size(600, 600)
    renderer.setup()

def draw():
    global renderer
    renderer.draw()