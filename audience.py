from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from midpoint_circle import *
from midpoint_line import *

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