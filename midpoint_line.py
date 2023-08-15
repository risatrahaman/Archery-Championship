from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def drawPixel(x, y):
    glPointSize(3)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def findZone(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    if abs(dx) >= abs(dy):
        if dx >= 0:
            if dy >= 0:
                zone = 0
            else:
                zone = 7
        else:
            if dy >= 0:
                zone = 3
            else:
                zone = 4
    else:
        if dx >= 0:
            if dy >= 0:
                zone = 1
            else:
                zone = 6
        else:
            if dy >= 0:
                zone = 2
            else:
                zone = 5
    return zone

# Convert the particular zone to zone 0 in order to run the line drawing algorithm
def convertZoneTo0(x, y, zone):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return y, -x 
    elif zone == 3:
        return -x, y 
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return -y, x
    elif zone == 7:
        return x, -y
    
# Convert zone 0 back to the original zone; then draw the pixel
def draw8WayLine(x, y, zone):
    if zone == 0:
        drawPixel(x, y)
    elif zone == 1:
        drawPixel(y, x)
    elif zone == 2:
        drawPixel(-y, x)
    elif zone == 3:
        drawPixel(-x, y)
    elif zone == 4:
        drawPixel(-x, -y)
    elif zone == 5:
        drawPixel(-y, -x)
    elif zone == 6:
        drawPixel(y, -x)
    elif zone == 7:
        drawPixel(x, -y)

# Line drawing algorithm for zone 0
def drawLine0(x0, y0, x1, y1, zone):
    dx = x1 - x0
    dy = y1 - y0
    
    d = 2 * dy - dx

    delE = 2 * dy
    delNE = 2 * (dy - dx)

    x = x0
    y = y0
    draw8WayLine(x, y, zone)
    while x < x1:
        if d < 0:
            d += delE
            x += 1
        else:
            d += delNE
            x += 1
            y += 1 
        draw8WayLine(x, y, zone)


def drawLine(x0, y0, x1, y1):
    zone = findZone(x0, y0, x1, y1)
    x0, y0 = convertZoneTo0(x0, y0, zone)
    x1, y1 = convertZoneTo0(x1, y1, zone)

    drawLine0(x0, y0, x1, y1, zone)