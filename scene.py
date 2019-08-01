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
from random import randint

canvas = GraphWin('My Painting', 500, 500)

#as someone who graphed a lot of functions, i'm very deeply hurt by
#the inverted coordinate system used by the graphics module
canvas.setCoords(0, 0, 500, 500)
#so i googled how to change it

canvas.setBackground(color_rgb(27, 196, 247))



def makeTree(canvas):
    
    #Tree Trunk
    trunk = Rectangle( Point(230, 0), Point(270, 300))
    trunk.setFill(color_rgb(79, 60, 32)  )
    trunk.draw(canvas)
    
    #Make a bunch of branches, and make them point in random directions
    for i in range(10):
        branch = Line( Point( randint(230, 270), randint(230, 270)), Point( randint(100, 400), randint(100, 400)))
        branch.setFill( color_rgb(79, 60, 32))
        branch.setWidth( randint(3, 10))
        branch.draw(canvas)
        
    #Make a million little leaf bunches and stick them on the tree
    for i in range(50):
        leaf = Circle( Point( randint(100, 400), randint(100, 400)), randint(20, 50))
        #Randomness element ensures that the tree has a healthy variety in the greens available
        leaf.setFill( color_rgb( randint( 0, 20), randint(200, 255), randint(0, 40)))
        leaf.draw(canvas)
        
    #Because I'm really craving apples right now
    for i in range(15):
        apple = Circle( Point( randint(100, 400), randint(100, 400)), randint(9, 15))
        apple.setFill( color_rgb( randint( 200, 255), randint(0, 200), randint(0, 20)))
        apple.draw(canvas)
makeTree(canvas)
