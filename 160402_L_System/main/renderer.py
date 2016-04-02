from gui import Gui
from rules import DrawRule

SCREEN_WIDTH  = 600
SCREEN_HEIGHT = 600

class Renderer:
    initiator  = "A"
    vertex     = PVector(SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.5)
    rules      = "A:B-A-B,B:A+B+A"
    angle      = 0
    iterates   = 9
    offset     = PVector(-255, -200)
    unitLength = 1
    unitAngle  = 60
    isDrawing  = True
    
    gui = None
        
    def setup(self):
        background(254)
        stroke(210)
        frameRate(60)
        self.gui = Gui(self.restart, self.initiator, self.rules, self.unitLength, self.unitAngle, self.iterates, self.offset)
            
    def draw(self):
        if not self.isDrawing:
            return

        self.vertex.add(PVector(self.offset.x, -self.offset.y))

        for i in range(self.iterates):
            self.initiator = DrawRule.update(self.initiator, self.rules)
        for c in self.initiator:
            if c in ["A", "B", "F"]:
                self.vertex = DrawRule.forward(self.unitLength, self.vertex, self.angle)
            elif c == "+":
                self.angle = DrawRule.plus(self.angle, self.unitAngle)
            elif c == "-":
                self.angle = DrawRule.minus(self.angle, self.unitAngle)
        self.isDrawing = False
                                
    def restart(self, e):
        rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.vertex     = PVector(SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.5)
        self.angle      = 0
        self.unitLength = self.gui.unitLength
        self.unitAngle  = self.gui.unitAngle
        self.initiator  = self.gui.initiator
        self.iterates   = self.gui.iterates
        self.offset     = self.gui.offset
        self.rules      = self.gui.rules
        self.isDrawing  = True