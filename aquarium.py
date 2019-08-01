# -------------------------------------------------
#        Name: Zaira Garcia, Josh Torres
#    Filename: aquarium.py
#        Date: July 31, 2019
#
# Description: An aquarium created using the graphics
#               module. Contains moving fish, dynamic
#               bubbles, and a randomized background.
# -------------------------------------------------

from graphics import *
from random import randint, choice
### CODE FROM THE LAB WEBPAGE ###
class Fish:
    """Definition for a fish with a body, eye, and tail"""
    def __init__(self, win, position):
        """constructs a fish made of 1 oval centered at `position`,
        a second oval for the tail, and a circle for the eye"""
        red = randint(0,255)
        green = randint(0,255)
        blue = randint(0,255)

        # body
        p1 = Point(position.getX()-40, position.getY()-20 )
        p2 = Point(position.getX()+40, position.getY()+20)
        self.body = Oval( p1, p2 )
        self.body.setFill(color_rgb(red, green, blue))

        # tail
        p1 = Point(position.getX()+30, position.getY()-30)
        p2 = Point(position.getX()+50, position.getY()+30)
        self.tail = Oval( p1, p2 )
        self.tail.setFill( "black" )

        # eye
        center2 = Point( position.getX()-15, position.getY()-5)
        self.eye = Circle( center2, 5 )
        self.eye.setFill( "black" )
        
    def draw( self, win ):
        """draw the fish to the window"""
        self.body.draw( win )
        self.tail.draw( win )
        self.eye.draw( win )
        
    def move( self , dx, dy):
        """move the fish by dx"""
        self.body.move( dx, dy )
        self.tail.move( dx, dy )
        self.eye.move( dx, dy )
### END OF CODE TAKEN FROM LAB PAGE ###

#Because our fish live in a post-climate change world, they have no plants. Just random
# assortments of rocks.
def aquariumBackground(win):
    list_of_rocks = []
    water = Rectangle(Point(-1, -1), Point(1000, 1000))
    water.setFill('blue')
    water.draw(win)
    for i in range(50):
        rock = Circle( Point(randint(0, 900), 800), randint(0, 100))
        rock.setFill('grey')
        list_of_rocks.append(rock)
    for boulder in list_of_rocks:
        boulder.draw(win)

        
#Create bubble object - literally just circles filled white
        
class Bubble():
    
    def __init__(self):
        self.size = randint(3, 10)
        self.center = Point( randint(10, 790), randint(800, 1300))
        self.image = Circle( self.center, self.size)
        self.image.setFill('white')
        
    def draw(self, win):
        self.image.draw(win)
        
    def rise(self):
        self.image.move(randint(-3, 3), -10)

        
def main():
    win = GraphWin('Aquarium', 900, 800)
    aquariumBackground(win)
    
    list_of_fish = []
    list_of_bubbles = []
    counter = 0
    for dummy in range(7):
        fish1 = Fish(win, Point(randint(100, 750), randint(100, 750)))
        fish1.draw(win)
        list_of_fish.append(fish1)
        
    for dummy2 in range(30):
        bubble = Bubble()
        bubble.draw(win)
        list_of_bubbles.append(bubble)
        
    for dummyvar in range(200):
        for aquatic in list_of_fish:
            dy = randint(-3, 3)
            aquatic.move(-5, dy)
        
        for orb in list_of_bubbles:
            counter += 1
            orb.rise()
            
main()
        
