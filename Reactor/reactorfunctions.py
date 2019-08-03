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

def buildReactorInterface(
