from time import *
from reactorConstruct import *
from reactorfunctions import *

#Reactor interface
x = 800
y = 800
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
