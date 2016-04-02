add_library('controlP5')

from controlP5 import *
    
class Gui:
   __instance = None

   cp5 = None
   labelColor = 180

   def __new__(cls, *args, **keys):
       if cls.__instance is None:
           cls.__instance = object.__new__(cls)
       return cls.__instance

   def __init__(self, restart, initiator, rules, unitLength, unitAngle, iterates, offset):    
       self.cp5 = ControlP5(this)
       
       # Unit length
       self.cp5.addTextfield('length') \
       .setPosition(20, 20) \
       .setWidth(50) \
       .setValue(str(unitLength)) \
       .setColorLabel(self.labelColor) \
       .getCaptionLabel() \
       .align(ControlP5.LEFT, ControlP5.TOP_OUTSIDE) \
       .setPaddingX(0)
    
       # Unit angle
       self.cp5.addTextfield('angle') \
       .setPosition(80, 20) \
       .setWidth(50) \
       .setValue(str(unitAngle)) \
       .setColorLabel(self.labelColor) \
       .getCaptionLabel() \
       .align(ControlP5.LEFT, ControlP5.TOP_OUTSIDE) \
       .setPaddingX(0)

       # Iterates
       self.cp5.addTextfield('iterates') \
       .setPosition(140, 20) \
       .setWidth(50) \
       .setValue(str(iterates)) \
       .setColorLabel(self.labelColor) \
       .getCaptionLabel() \
       .align(ControlP5.LEFT, ControlP5.TOP_OUTSIDE) \
       .setPaddingX(0)

       # Offset X
       self.cp5.addTextfield('offsetX') \
       .setPosition(20, 60) \
       .setWidth(50) \
       .setValue(str(offset.x)) \
       .setColorLabel(self.labelColor) \
       .getCaptionLabel() \
       .align(ControlP5.LEFT, ControlP5.TOP_OUTSIDE) \
       .setPaddingX(0)

       # Offset Y
       self.cp5.addTextfield('offsetY') \
       .setPosition(80, 60) \
       .setWidth(50) \
       .setValue(str(offset.y)) \
       .setColorLabel(self.labelColor) \
       .getCaptionLabel() \
       .align(ControlP5.LEFT, ControlP5.TOP_OUTSIDE) \
       .setPaddingX(0)
                                
       # initiator
       self.cp5.addTextfield('initiator') \
       .setPosition(20, 100) \
       .setWidth(50) \
       .setValue(initiator) \
       .setColorLabel(self.labelColor) \
       .getCaptionLabel() \
       .align(ControlP5.LEFT, ControlP5.TOP_OUTSIDE) \
       .setPaddingX(0)
       
       # Rules
       self.cp5.addTextfield('rules') \
       .setPosition(20, 140) \
       .setWidth(100) \
       .setValue(rules) \
       .setColorLabel(self.labelColor) \
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
   def initiator(self):
       return self.cp5.get(Textfield, 'initiator').getText()

   @property
   def offset(self):
       return PVector(float(self.cp5.get(Textfield, 'offsetX').getText()), \
       float(self.cp5.get(Textfield, 'offsetY').getText()))
      
   @property
   def iterates(self):
       return int(self.cp5.get(Textfield, 'iterates').getText())

   @property
   def rules(self):
       return self.cp5.get(Textfield, 'rules').getText()
                                                                                                                                