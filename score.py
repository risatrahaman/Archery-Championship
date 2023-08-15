from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from midpoint_line import *

def showScore(startX, startY, i):
    def drawZero(x, y):
        # Horizontal Lines
        drawLine(x, y, x + 20, y)
        drawLine(x, y - 40, x + 20, y - 40)
        # Vertical Lines
        drawLine(x, y, x, y - 40)
        drawLine(x + 20, y, x + 20, y - 40)
    def drawOne(x, y):
        drawLine(x, y, x, y - 40)
    def drawTwo(x, y):
        # Horizontal Lines
        drawLine(x, y, x + 20, y)
        drawLine(x, y - 20, x + 20, y - 20)
        drawLine(x, y - 40, x + 20, y - 40)
        # Vertical Lines
        drawLine(x + 20, y, x + 20, y - 20)
        drawLine(x, y - 20, x, y - 40)
    def drawThree(x,y):
        # Horizontal Lines
        drawLine(x, y, x + 20, y)
        drawLine(x, y - 20, x + 20, y - 20)
        drawLine(x, y - 40, x + 20, y - 40)
        # Vertical Lines
        drawLine(x + 20, y, x + 20, y - 20)
        drawLine(x + 20, y - 20, x + 20, y - 40)
    def drawFour(x, y):
        # Vertical Lines
        drawLine(x, y, x, y - 20)
        drawLine(x + 20, y, x + 20, y - 20)
        drawLine(x + 20, y - 20, x + 20, y - 40)
        # Horizonal Lines
        drawLine(x, y - 20, x + 20, y -20)
    def drawFive(x, y):
        # Horizontal Lines
        drawLine(x, y, x + 20, y)
        drawLine(x, y - 20, x + 20, y - 20)
        drawLine(x, y - 40, x + 20, y - 40)
        # Vertical Lines
        drawLine(x + 20, y - 20, x + 20, y - 40)
        drawLine(x, y, x, y - 20)
    if i == 1:
        drawOne(startX, startY)
        startX += 30
    elif i == 2:
        drawTwo(startX, startY)
        startX += 50
    elif i == 3:
        drawThree(startX, startY)
        startX += 50
    elif i == 4:
        drawFour(startX, startY)
        startX += 50
    elif i == 5:
        drawFive(startX, startY)
        startX += 50
    elif i == 0:
        drawZero(startX, startY)
        startX += 50