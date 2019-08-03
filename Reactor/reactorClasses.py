from random import *
from graphics import *
from math import *
from time import *


#The reactor itself
class Reactor:

    def __init__(self):
        self.fuel_level = 100
        self.heat = 0
        self.coolant_level = 100
        self.rod_insertion = 100
        
    #Emergency shutdown
    def scram(self):
        self.rod_insertion = 100
        return True
    
    #Move the control rods by some increment
    def moveControlRods(self, increment):
        if self.rod_insertion + increment > 100:
            self.rod_insertion = 100
        elif self.rod_insertion + increment < 0:
            self.rod_insertion = 0
        else:
            self.rod_insertion += increment
        
#These are the numbers which get displayed; for example: 0100 MW of power, 1300 deg. C heat, etc.
class DisplayNumber: #NYI
    
    def __init__(self):
        None

        
class StatusBar:

    def __init__(self, level, top_left, bottom_right,):
        self.level = level #Number between 0 and 100
        self.top_left = top_left
        self.bottom_right = bottom_right
        
        #This was the hardest part, it needed so much geometry
        #Draws 4 rectangles stacked on top of each other to show the status of reactor levels. I'll  color the top one black once the level drops below 75%, the third one black when level drops below 50%, etc.
        self.height = ( top_left.getY() - bottom_right.getY() )
        self.bottom_quad = Rectangle( Point( top_left.getX(), top_left.getY() - 3*(self.height/4)), bottom_right)
        self.second_quad = Rectangle( Point( top_left.getX(), top_left.getY() - 2*(self.height/4)), Point( bottom_right.getX(), top_left.getY() - 3*(self.height/4)) )
        self.third_quad = Rectangle( Point( top_left.getX(), top_left.getY() - (self.height/4)), Point( bottom_right.getX(), top_left.getY() - 2*(self.height/4)) )
        self.top_quad = Rectangle( top_left, Point(bottom_right.getX(), top_left.getY() - (self.height/4)))
        
    #Take in your window and 4 different color choices and draw your status bar
    def draw(self, win, color1, color2, color3, color4):
        self.bottom_quad.setFill( color1 )
        self.second_quad.setFill( color2 )
        self.third_quad.setFill( color3 )
        self.top_quad.setFill( color4 )
        self.bottom_quad.draw(win)
        self.second_quad.draw(win)
        self.third_quad.draw(win)
        self.top_quad.draw(win)
        
    def getLevel(self):
        return self.level
    
#Buttons!        
class Button:
    
    #Buttons know whether they've been pressed, their color, their center, what they look like
    def __init__(self, center, radius, color ):
        self.shape = 'Circle'
        self.pressed = False
        self.color = color
        self.center = center
        self.radius = radius
        self.image = Circle(center, radius)
        
    #Buttons know how to push themselves
    def push(self):
        self.pressed = True
        self.image.setFill('gray')
        
    #Buttons know how to unpush themselves
        
    def unpush(self):
        self.pressed = False
        self.image.setFill( self.color )
    #Draw self on win
        
    def draw(self, win):  
        self.image.setFill( self.color)
        self.image.draw(win)
        
    def checkIfPressed(self):
        return self.pressed
    
class SquareButton(Button):
    
    
    def __init__(self, top_left, bottom_right, color ):
        self.shape = 'Square'
        self.pressed = False
        self.color = color
        self.top_left = top_left
        self.bottom_right = bottom_right
        self.image = Rectangle(top_left, bottom_right)
        
