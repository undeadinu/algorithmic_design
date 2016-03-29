from gui import Gui
from rules import DrawRule

SCREEN_WIDTH  = 600
SCREEN_HEIGHT = 600

class Renderer:
    initialState = "A" #"F-F-F-F"
    state    = initialState + ""
    edge     = PVector(SCREEN_WIDTH, SCREEN_HEIGHT)
    rules    = "A:B-A-B,B:A+B+A" #"F:F+FF-FF-F-F+F+FF-F-F+F+FF+FF-F"
    degree   = 0
    iterates = 5
    
    unitLength = 4
    unitAngle  = 60 #90
    isDrawing  = True
    
    gui = None
    
    def __init__(self):
        print('init')
        
    def setup(self):
        background(254)
        stroke(210)
        frameRate(2)
        self.gui = Gui(self.restart, self.state, self.rules, self.unitLength, self.unitAngle)
            
    def draw(self):
        if not self.isDrawing:
            return
            
        for i in range(self.iterates):
            self.state  = DrawRule.update(self.state, self.rules)
                        
        for c in self.state:
            if c in ["A", "B", "F"]:
                self.edge = DrawRule.forward(self.unitLength, self.edge, self.degree)
            elif c == "+":
                self.degree = DrawRule.plus(self.degree, self.unitAngle)
            elif c == "-":
                self.degree = DrawRule.minus(self.degree, self.unitAngle)
   
        self.isDrawing = False
                                
    def restart(self, e):
        rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.state      = self.initialState + ""
        self.edge       = PVector(SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.5)
        self.degree     = 0
        self.unitLength = self.gui.unitLength
        self.unitAngle  = self.gui.unitAngle
        self.state      = self.gui.state
        self.rules      = self.gui.rules
        self.isDrawing  = True