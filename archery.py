from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
import time
from midpoint_line import *
from midpoint_circle import *
from midpoint_halfcircle import *

def drawPixel(x, y):
    glPointSize(3)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def drawLine(x0, y0, x1, y1):
    zone = findZone(x0, y0, x1, y1)
    x0, y0 = convertZoneTo0(x0, y0, zone)
    x1, y1 = convertZoneTo0(x1, y1, zone)

    drawLine0(x0, y0, x1, y1, zone)

headRadius = 20
bodyLength = 100
armLength = 50
legLength = 50
arrowLength = 60
bowLength = 80

def Bow(posX, posY):
    
    # Handle
    glColor3f(1.0, 1.0, 1.0)
    drawLine(posX, posY, posX, posY - bowLength)
    
    # String
    glColor3f(0.6, 0.3, 0.0)
    radius = bowLength/2
    drawHalfCircle(posX, posY - radius, radius)

class Arrow:
    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY

        self.hit = (self.posX + arrowLength, posY)

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
        

    def show(self):
        glColor3f(0.0, 1.0, 1.0)
        
        # Head
        drawCircle(self.posX, self.posY, headRadius)

        # Body
        drawLine(self.posX, self.posY - headRadius, self.posX, self.posY - bodyLength)

        # Left arm
        drawLine(self.posX, self.posY - headRadius, self.posX - armLength + 20, self.posY - armLength)

        # Left hand
        drawLine(self.posX - armLength + 20, self.posY - armLength, self.posX + armLength - 10, self.posY - armLength + 10)

        # Right Hand
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

def showTarget():
    r = 50
    dividing = int(r/4)
    centerX, centerY = 390, 230

    drawCircle(centerX,centerY, r)

    for z in range(r,r-dividing,-1):
        glColor3f(0.2,0.7,1)
        drawCircle(centerX,centerY, z)

    r -= dividing

    for z in range(r,r-dividing,-1):
        glColor3f(1,1,1)
        drawCircle(centerX,centerY, z)
    drawCircle(centerX, centerY, r)

    r -= dividing

    for z in range(r,r-dividing,-1):
        glColor3f(0,1,0)
        drawCircle(centerX,centerY, z)
    drawCircle(centerX, centerY, r)

    r -= dividing

    for z in range(r,r-dividing,-1):
        glColor3f(0.8,0.1,0)
        drawCircle(centerX,centerY, z)
    drawCircle(centerX, centerY, r)

def showAudience():
    glColor3f(0.0, 0.5, 0.0)
    k=1
    count=0
    while k<=5:
        count=count+50

        #e,f,rb=audience(250,350,3)
        # e -> x center; f -> y center; rb -> radius
        
        e=170+count
        f=370
        rb=10
        # Head
        drawCircle(e,f+7, rb)
        # Neck
        drawLine(e, f-3, e, f-17)
        # Body
        drawLine(e, f-17, e+20, f-7)
        # Right hand
        drawLine(e-20, f-7, e, f-17)
        # Left hand
        drawLine(e, f-17, e, f-40)
        # Left leg
        drawLine(e, f-40, e-10, f-45)
        # Right leg
        drawLine(e, f-40, e+10, f-45)

        k+=1

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glLoadIdentity()
    iterate()

    #user_input = int(input("Enter a value from 1 to 6: "))
    user = Person('player1', 100, 300)

    for i in range(20):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # user_input + 6.5: 1 to 6
        # Arrow move - 7.5 to 12.5; 10 hits bullseye
        moveX = 10 #+ user_input
        moveY = -2
        
        translate = np.array([
            [1, 0, moveX],
            [0, 1, moveY],
            [0, 0, 1]
        ])

        user.show()
        arrowX = user.arrowX
        arrowY = user.arrowY
        arrowPosition = np.array([
            [arrowX],
            [arrowY],
            [1]
        ])

        showTarget()
        showAudience()
        user.showArrow()

        x, y, d = np.matmul(translate, arrowPosition)
        user.arrowX, user.arrowY = x[0], y[0]

        glFlush()
        time.sleep(0.03)

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Archery Championship")
glutDisplayFunc(showScreen)
glutMainLoop()
