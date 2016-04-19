import math

honicombs = []
radius    = 26
number    = 16

def setup():
    size(600, 600, P3D)
    stroke(220)
    frameRate(2)
    
    p = PVector(-radius, -radius)
    delta = 0
    while True:
        newX = p.x + radius * 3
        newY = p.y + radius * math.sqrt(3) * 0.5

        if newX <= width + radius:
            p = PVector(newX, p.y)
        elif newY <= height + radius:
            delta = 1 if delta == 0 else 0
            p = PVector(delta * radius * 1.5, newY)
        else:
            break
        
        honicombs.append(Honicomb(p, radius))


def draw():
    background(254)

    for h in honicombs:
        h.draw()


class Honicomb:
    def __init__(self, point, radius):
        self.point  = point
        self.radius = radius
        
    def draw(self):
        for r in xrange(1, number + 1):
            self.drawHonicomb(self.radius * r / number)
   
    def drawHonicomb(self, radius):
        beginShape()
        for i in xrange(7):
            p = PVector(self.point.x + radius * cos(TWO_PI / 6 * i), \
                         self.point.y + radius * sin(TWO_PI / 6 * i))
            
            z  = sin(p.x / (width * 2.0) * TWO_PI) * \
                 sin(p.y / (height * 2.0) * TWO_PI) * cos(frameCount * 10 / TWO_PI) * 450
                        
            vertex(p.x, p.y, z)
        endShape()  