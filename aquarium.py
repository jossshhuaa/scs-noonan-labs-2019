# -------------------------------------------------
#        Name: Michelle Chen, Nina Kagan, & Josh Torres
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
        self.eye_level = center2.getY()
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
        self.eye_level += dy
### END OF CODE TAKEN FROM LAB PAGE ###

#Because our fish live in a post-climate change world, they have no plants. Just random
# assortments of rocks.
def aquariumBackground(win):
##    list_of_rocks = []
##    water = Rectangle(Point(-1, -1), Point(1000, 1000))
##    water.setFill('blue')
##    water.draw(win)
##    for i in range(50):
##        rock = Circle( Point(randint(0, 900), 800), randint(0, 100))
##        rock.setFill('grey')
##        list_of_rocks.append(rock)
##    for boulder in list_of_rocks:
##        boulder.draw(win)


##Code Taken From StackOverflow
##User: Rod
##URL: https://stackoverflow.com/a/19250144
    
    myImage = Image(Point(450,350), "aquariumbg.gif")
    myImage.draw(win)

##END BORROWED CODE##

    
#Create bubble object - literally just circles filled white
        
class Bubble():
    
    def __init__(self):
        self.size = randint(3, 10)
        self.center = Point( randint(10, 790), randint(800, 1300))
        self.image = Circle( self.center, self.size)
        self.image.setFill('white')

    #Draw the bubble
    def draw(self, win):
        self.image.draw(win)
    #Make the image rise and bob left/right
    def rise(self):
        self.image.move(randint(-3, 3), -10)

#Food is just bubbles - but brown and heavier
class Food():
    def __init__(self):
        self.size = randint(3, 6)
        self.center = Point( randint(10, 790), randint(-100, 0))
        self.height = self.center.getY()
        self.image = Circle( self.center, self.size)
        self.image.setFill('brown')
        
    def draw(self, win):
        self.image.draw(win)
    #Opposite of bubble 'rise' -  fish food sinks
    def sink(self, win):
        self.image.move(randint(-3, 3), 10)
        self.height += 10
        
def main():
    win = GraphWin('Aquarium', 900, 800)
    aquariumBackground(win)
    #Three empty lists, ready to be filled
    list_of_fish = []
    list_of_bubbles = []
    list_of_food = []
    
    #Draw 7 random fish on the right side of the screen
    for dummy in range(7):
        fish1 = Fish(win, Point(randint(700, 750), randint(100, 750)))
        fish1.draw(win)
        list_of_fish.append(fish1)
        
    #Draw 30 bubbles below the screen and let them rise up into it
    for dummy2 in range(30):
        bubble = Bubble()
        bubble.draw(win)
        list_of_bubbles.append(bubble)
        
    key_press = 0
    is_there_food = False

    
    while key_press != 'q':
        key_press = win.checkKey()
        click_location = win.checkMouse()
        #If you did in fact click on something, make a fish there
        if click_location != None:
            fish = Fish( win, click_location)
            fish.draw(win)
            list_of_fish.append(fish)

        #Quit once user hits 'q'
        elif key_press.lower() == 'q':
            print('ABORT - SELF DESTRUCT SEQUENCE INITIALIZED')
            continue

        #If user hits 'f', feed the fish
        elif key_press.lower() == 'f':
            for dummy2 in range(30):
                food = Food()
                food.draw(win)
                list_of_food.append(food)
                is_there_food = True
                
        #if user hits 'b', make bubbles
        elif key_press.lower() == 'b':
            for dummy2 in range(30):
                bubble = Bubble()
                bubble.draw(win)
                list_of_bubbles.append(bubble)
        #If you didn't do ANYTHING else, move everything a little
        else:
            #Make the bubbles rise
            for orb in list_of_bubbles:
                    orb.rise()
            #If there's no food, don't bother making the nonexistent food rise
            if not is_there_food:
                for aquatic in list_of_fish:
                    dy = randint(-3, 3)
                    aquatic.move(-5, dy)
            #If there's food, make the food AND the bubbles AND the fish rise
            elif is_there_food:        
                for pellet in list_of_food:
                    pellet.sink(win)

                #Fish will move towards the food which was fed
                for aquatic in list_of_fish:
                    pellet_height = pellet.height
                    fish_height = aquatic.eye_level
                    difference = fish_height - pellet_height
                    #If food is above the fish, make the fish rise
                    if difference >= 0:
                        aquatic.move(-5, -5)
                    #If food is below the fish, make the fish sink
                    else:
                        aquatic.move(-5, 5)
                    
    win.close()
            
main()
