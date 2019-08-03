from random import *
from graphics import *
from math import *
from time import *


#Use the distance formula to calculate the distance between two points


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
        
def getDistance( p1, p2 ):
    distance = sqrt( (p1.getX() - p2.getX())**2 + (p1.getY() - p2.getY())**2)
    return distance

def isPointInArea( p1, top_left, bottom_right ):
    if ( p1.getX() >= top_left.getX() and
         p1.getX() <= bottom_right.getX() and
         p1.getY() <= top_left.getY() and
         p1.getY() >= bottom_right.getY()):
        return True
    else:
        return False

#Reactor interface
x = 700
y = 700
interface = GraphWin('Control Panel', x, y)
interface.setCoords( 0, 0, x, y)
interface.setBackground('brown')

list_of_buttons = []
#Draw the first button (TESTING ONLY)
button1 = Button( Point(x/2, y/2), 50, 'blue')
button1.draw(interface)
list_of_buttons.append(button1)
#Draw the second button (TESTING ONLY)
button2 = SquareButton( Point(100,200), Point(200, 100), 'green')
button2.draw(interface)
list_of_buttons.append(button2)



#bar = StatusBar( 100, Point(300, 600), Point(600, 100))
#bar.draw(interface, 'blue', 'cyan', 'red', 'green')
key_press = 'p'

while key_press.lower() != 'q':
    
    key_press = interface.checkKey()
    if key_press != None:
        if key_press.lower() == 'q':
            key_press = 'q'
            interface.close()
            continue
        
    click = interface.checkMouse()
    if click != None:
        print( click.getX(), 'click x')
        print( click.getY(), 'click y')
        for button in list_of_buttons:
            if button.shape == 'Circle':
                print('checking circle...')
                if getDistance(click, button.center) <= button.radius:
                    print('circle got pushed')
                    button.push()
                    sleep(.5)
                    button.unpush()
                    break
                
            elif button.shape == 'Square':
                print('checking square...')
                if isPointInArea( click, button.top_left, button.bottom_right) :
                    print('square got pushed')
                    button.push()
                    sleep(.5)
                    button.unpush()
                    break
    
