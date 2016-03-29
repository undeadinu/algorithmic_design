add_library('controlP5')
import re
# from classes import Point

initialState = "A" #"F-F-F-F"
state    = initialState + ""
edge     = PVector(240, 240)
rules    = "A:B-A-B,B:A+B+A" #"F:F+FF-FF-F-F+F+FF-F-F+F+FF+FF-F"
degree   = 0
iterates = 5

unitLength = 1
unitAngle  = 60 #90
isDrawing  = True

gui = None
    
def setup():
    global unitLength, unitAngle, gui
    
    size(480, 480)
    background(254)
    stroke(210)
    frameRate(2)

    gui = Gui() 

def draw():
    global state, edge, degree, isDrawing

    if not isDrawing:
        return

    for i in range(iterates):
        state  = DrawRule.update(state, rules)

    for c in state:
        if c in ["A", "B", "F"]:
            edge = DrawRule.forward(edge, degree)
        elif c == "+":
            degree = DrawRule.plus(degree, unitAngle)
        elif c == "-":
            degree = DrawRule.minus(degree, unitAngle)

    isDrawing = False

def restart(e):
    global edge, degree, isDrawing, initialState, state, gui, unitLength, unitAngle, rules

    rect(0, 0, 480, 480)
    state  = initialState + ""
    edge   = PVector(240, 240)
    degree = 0    
    unitLength = gui.unitLength
    unitAngle = gui.unitAngle
    state = gui.state
    rules = gui.rules
    isDrawing  = True
    
class Gui:
    __instance = None

    cp5 = None

    def __new__(cls, *args, **keys):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self):    
        self.cp5 = ControlP5(this)

        # Unit length
        self.cp5.addTextfield('length') \
        .setPosition(20, 20) \
        .setWidth(50) \
        .setValue(str(2)) \
        .setColorLabel(200) \
        .getCaptionLabel() \
        .align(ControlP5.LEFT, ControlP5.TOP_OUTSIDE) \
        .setPaddingX(0)
    
        # Unit angle
        self.cp5.addTextfield('angle') \
        .setPosition(20, 60) \
        .setWidth(50) \
        .setValue(str(60)) \
        .setColorLabel(200) \
        .getCaptionLabel() \
        .align(ControlP5.LEFT, ControlP5.TOP_OUTSIDE) \
        .setPaddingX(0)
        
        # State
        self.cp5.addTextfield('state') \
        .setPosition(20, 100) \
        .setWidth(50) \
        .setValue(str(60)) \
        .setColorLabel(200) \
        .getCaptionLabel() \
        .align(ControlP5.LEFT, ControlP5.TOP_OUTSIDE) \
        .setPaddingX(0)
        
        # Rules
        self.cp5.addTextfield('rules') \
        .setPosition(20, 140) \
        .setWidth(100) \
        .setValue(str(60)) \
        .setColorLabel(200) \
        .getCaptionLabel() \
        .align(ControlP5.LEFT, ControlP5.TOP_OUTSIDE) \
        .setPaddingX(0)
        
        self.cp5.addButton('restart') \
        .setLabel('draw') \
        .setPosition(20,180) \
        .setSize(51,20) \
        .addListener(restart)
    
    @property
    def unitLength(self):
        return int(self.cp5.get(Textfield, 'length').getText())

    @property
    def unitAngle(self):
        return int(self.cp5.get(Textfield, 'angle').getText())

    @property
    def state(self):
        return int(self.cp5.get(Textfield, 'state').getText())

    @property
    def rules(self):
        return int(self.cp5.get(Textfield, 'rules').getText())
                                                                                                                                
class DrawRule:
    
    @classmethod
    def forward(cls, edge, degree):
        diff = PVector(unitLength, 0).rotate(degree * PI / 180.0)
        dest = PVector(edge.x, edge.y)
        dest.add(diff)
        line(edge.x, edge.y, dest.x, dest.y)
        return dest

    @classmethod
    def plus(cls, currentDegree, diff):
        return currentDegree + diff

    @classmethod
    def minus(cls, currentDegree, diff):
        return currentDegree - diff
    
    @classmethod
    def update(cls, state, rules):
        rep = {}
        for rule in rules.replace(' ', '').split(','):
           item = rule.split(':')
           if len(item) > 1:
               rep[item[0]] = item[1]
                          
        rep = dict((re.escape(k), v) for k, v in rep.iteritems())
        pattern = re.compile("|".join(rep.keys()))
        return pattern.sub(lambda m: rep[re.escape(m.group(0))], state)