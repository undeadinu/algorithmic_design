import re

class DrawRule:
    @classmethod
    def forward(cls, unitLength, vertex, angle):
        origin = vertex
        diff = PVector(unitLength, 0).rotate(angle * PI / 180.0)
        dest = PVector(origin.x, origin.y)
        dest.add(diff)
        line(origin.x, origin.y, dest.x, dest.y)
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
        
        if len(rep) == 0:
            return state
                
        rep = dict((re.escape(k), v) for k, v in rep.iteritems())
        pattern = re.compile("|".join(rep.keys()))
        return pattern.sub(lambda m: rep[re.escape(m.group(0))], state)