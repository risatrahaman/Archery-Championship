from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from midpoint_line import *
from midpoint_circle import *
from midpoint_halfcircle import *

headRadius = 20
bodyLength = 100
armLength = 50
legLength = 50
arrowLength = 60
bowLength = 80

def Bow(posX, posY):
    
    # String
    glColor3f(1.0, 1.0, 1.0)
    drawLine(posX, posY, posX, posY - bowLength)
    
    # Handle
    glColor3f(0.6, 0.3, 0.0)
    radius = bowLength/2
    drawHalfCircle(posX, posY - radius, radius)

class Arrow:
    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY

    def show(self):
        glColor3f(1.0, 0.0, 1.0)
        # Body
        drawLine(self.posX, self.posY, self.posX + arrowLength, self.posY)

        # Bullet
        drawLine(self.posX + arrowLength, self.posY, self.posX + arrowLength - 5, self.posY + 5)
        drawLine(self.posX + arrowLength, self.posY, self.posX + arrowLength - 5, self.posY - 5)

class Person:
    def __init__(self, name, posX, posY):
        self.name = name
        self.posX = posX
        self.posY = posY

        # Arrow Position
        self.arrowX = self.posX + armLength - 10
        self.arrowY = self.posY - 30

        self.rightx1 = self.posX + armLength - 10
        self.righty1 = self.posY - armLength + 10

    def show(self):
        glColor3f(0.0, 1.0, 1.0)
        
        # Head
        drawCircle(self.posX, self.posY, headRadius)

        # Body
        drawLine(self.posX, self.posY - headRadius, self.posX, self.posY - bodyLength)

        # Right arm
        drawLine(self.posX, self.posY - headRadius, self.posX - armLength + 20, self.posY - armLength)

        # Right hand
        # Will Rotate only x1, y1
        drawLine(self.posX - armLength + 20, self.posY - armLength, self.rightx1, self.righty1)

        # Left Hand
        drawLine(self.posX, self.posY - headRadius, self.posX + armLength + 30, self.posY - 20)

        # Left Leg
        drawLine(self.posX, self.posY - bodyLength, self.posX - 20, self.posY - bodyLength -legLength)

        # Right Leg
        drawLine(self.posX, self.posY - bodyLength, self.posX + 20, self.posY - bodyLength -legLength)

        # Bow
        x = self.posX + armLength - 10
        y = self.posY + 10
        Bow(x, y)

        
    def showArrow(self):
        self.arrow = Arrow(self.arrowX, self.arrowY)
        self.arrow.show()