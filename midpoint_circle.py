from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def drawPixel(x, y):
    glPointSize(3)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def draw8way(x, y, a, b):
    drawPixel(x+a, y+b)
    drawPixel(-x+a, y+b)
    drawPixel(x+a, -y+b)
    drawPixel(-x+a, -y+b)
    drawPixel(y+a, x+b)
    drawPixel(-y+a, x+b)
    drawPixel(y+a, -x+b)
    drawPixel(-y+a, -x+b)

# Full Circle
def drawCircle(a, b, r):
    d = 5 - 4 * r
    x = 0
    y = r

    draw8way(x, y, a, b)
    while x < y:
        if d < 0:
            d += (2 * x + 3) * 4
            x += 1
        else:
            d += 4 * (2 * x - 2 * y + 5)
            x += 1
            y -= 1

        draw8way(x, y, a, b)