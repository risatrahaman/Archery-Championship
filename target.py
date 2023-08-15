from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from midpoint_circle import *

def showTarget():
    r = 50
    dividing = int(r/4)
    centerX, centerY = 390, 230

    for z in range(r,r-dividing,-1):
        glColor3f(0.2,0.7,1)
        drawCircle(centerX,centerY, z)

    r -= dividing

    for z in range(r,r-dividing,-1):
        glColor3f(1,1,1)
        drawCircle(centerX,centerY, z)

    r -= dividing
    
    for z in range(r,r-dividing,-1):
        glColor3f(0,1,0)
        drawCircle(centerX,centerY, z)

    r -= dividing
    
    for z in range(r,r-10,-1):
        glColor3f(0.8,0.1,0)
        drawCircle(centerX,centerY, z)

    for z in range(r-10,0,-1):
        glColor3f(1,1,0)
        drawCircle(centerX,centerY, z)