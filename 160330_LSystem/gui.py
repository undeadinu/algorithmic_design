add_library('controlP5')

from controlP5 import *

    
class Gui:
   __instance = None

   cp5 = None

   def __new__(cls, *args, **keys):
       if cls.__instance is None:
           cls.__instance = object.__new__(cls)
       return cls.__instance

   def __init__(self, restart, state, rules, unitLength, unitAngle):    
       self.cp5 = ControlP5(this)

       # Unit length
       self.cp5.addTextfield('length') \
       .setPosition(20, 20) \
       .setWidth(50) \
       .setValue(str(unitLength)) \
       .setColorLabel(200) \
       .getCaptionLabel() \
       .align(ControlP5.LEFT, ControlP5.TOP_OUTSIDE) \
       .setPaddingX(0)
    
       # Unit angle
       self.cp5.addTextfield('angle') \
       .setPosition(20, 60) \
       .setWidth(50) \
       .setValue(str(unitAngle)) \
       .setColorLabel(200) \
       .getCaptionLabel() \
       .align(ControlP5.LEFT, ControlP5.TOP_OUTSIDE) \
       .setPaddingX(0)
        
       # State
       self.cp5.addTextfield('state') \
       .setPosition(20, 100) \
       .setWidth(50) \
       .setValue(state) \
       .setColorLabel(200) \
       .getCaptionLabel() \
       .align(ControlP5.LEFT, ControlP5.TOP_OUTSIDE) \
       .setPaddingX(0)
        
       # Rules
       self.cp5.addTextfield('rules') \
       .setPosition(20, 140) \
       .setWidth(100) \
       .setValue(rules) \
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
       return self.cp5.get(Textfield, 'state').getText()

   @property
   def rules(self):
       return self.cp5.get(Textfield, 'rules').getText()
                                                                                                                                