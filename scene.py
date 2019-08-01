# -------------------------------------------------
#        Name: Josh Torres
#    Filename: scene.py
#        Date: July 31, 2019
#
# Description: Truly the nicest apple tree I've ever
#               drawn. This program generates a random
#               apple tree every time it's run. If it
#               looks ugly, keep running the code until
#               it looks pretty :)
# -------------------------------------------------

from graphics import *
from random import randint, choice
def drawCloud(canvas, x, y):
    for i in range(20):
        puff = Circle( Point( randint(x-150, x+150), randint(y-40, y+40) ), randint(10, 50))
        color_value = randint( 200, 255)
        puff.setFill( color_rgb( color_value, color_value, color_value) )
        puff.draw(canvas)
def makeTree(canvas, x, y, color_scale):
    
    #Tree Trunk
    trunk = Rectangle( Point(x-20, 0), Point(x+20, y))
    trunk.setFill(color_rgb(79, 60, 32)  )
    trunk.draw(canvas)
    
    #Make a bunch of branches, and make them point in random directions
    for i in range(10):
        branch = Line( Point( randint(x-20, x+20), randint(y-20, y+20)), Point( randint(x-150, x+150), randint(y-150, y+150)))
        branch.setFill( color_rgb(79, 60, 32) )
        branch.setWidth( randint(4, 10) )
        branch.draw(canvas)
        
    #Make a million little leaf bunches and stick them on the tree
    for i in range(50):
        
        leaf = Circle( Point( randint(x-150, x+150), randint(y-150, y+150)), randint(20, 50))
        #Randomness element ensures that the tree has a healthy variety in the greens available
        if color_scale == 'red':
            leaf.setFill( color_rgb( randint( 100, 200), randint(200, 255), 0))
        elif color_scale == 'green':
            leaf.setFill( color_rgb( randint( 0, 20), randint(200, 255), randint(0, 40)))
        leaf.draw(canvas)
        
    #Because I'm really craving apples right now
    for i in range(15):
        apple = Circle( Point( randint(x-150, x+150), randint(y-150, y+150)), randint(9, 15))
        apple.setFill( color_rgb( randint( 200, 255), randint(0, 200), randint(0, 20)))
        apple.draw(canvas)
        
canvas = GraphWin('My Painting', 1300, 700)
#as someone who graphed a lot of functions, i'm very deeply hurt by
#the inverted coordinate system used by the graphics module
canvas.setCoords(0, 0, 1300, 700)
#so i googled how to change it
sun = Circle( Point(1200, 600), 50)
sun.setFill('yellow')
sun.draw(canvas)
canvas.setBackground(color_rgb(27, 196, 247))
for i in range(3):
    drawCloud(canvas, randint(100, 1300), randint(500, 700))
for i in range(6):
    color = choice(['red', 'green'])
    makeTree(canvas, randint(100, 1300), randint(200, 300), color)
    
