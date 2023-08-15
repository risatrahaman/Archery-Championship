from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
import time
import random
import math
from midpoint_line import *
from midpoint_circle import *
from midpoint_halfcircle import *
from logo import *
from person_and_bow import *
from target import *
from audience import *
from score import *
from score_board import *

def drawPixel(x, y):
    glPointSize(3)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def iterate():
    glViewport(0, 0, 600, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 600, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

user_input = int(input("Enter a value from 1 to 5: "))

moveX = 10
moveY = -2
score = 0
# Arrow move - 7.5 to 12.5; 10 hits bullseye, 9.5 | 10.5: 3; 8.5 | 11: 2; 7.5 | 12.5: 1
        # 10: user input -> 1
        # 9.5 and 10.5: user input -> 2
        # 9 and 11 : user input -> 3
        # 8.5 and 11.5: user input -> 4
        # 7.5 and 12.5: user input -> 5
if user_input == 5:
    moveX = 10
    score = 5
elif user_input == 4:
    moveX = random.choice((9.5, 10.5))
    score = 4
elif user_input == 3:
    moveX = random.choice((9, 11))
    score = 3
elif user_input == 2:
    moveX = random.choice((8.4, 11.6))
    score = 2
elif user_input == 1:
    moveX = random.choice((7.5, 12.5))
    score = 1
else:
    moveX = 4

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glLoadIdentity()
    iterate()

    person = Person('person', 100, 300)

    for i in range(20):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        logo() # Archery Championship Logo

        # Translate matrix
        translate = np.array([
            [1, 0, moveX],
            [0, 1, moveY],
            [0, 0, 1]
        ])

        # Rotation degree
        a = math.cos(math.radians(1))
        b = math.sin(math.radians(1))

        # Rotation matrix
        rotation = np.array([
            [a, b, 0],
            [-b, a, 0],
            [0, 0, 1]
        ])

        # Displaying person object
        person.show()
        # Setting up arrow's initial position
        arrowX = person.arrowX
        arrowY = person.arrowY

        # Arrow Position Vector
        arrowPosition = np.array([
            [arrowX],
            [arrowY],
            [1]
        ])

        # The shooter's right hand position
        rightHand = np.array([
            [person.rightx1], 
            [person.righty1],
            [1]
        ])

        showTarget() # Display target
        showAudience() # Display audience
        person.showArrow() # Display arrow

        # Translating the arrow position vector 
        x, y, dummy = np.matmul(translate, arrowPosition)
        
        # Updating arrow's position
        person.arrowX, person.arrowY = x[0], y[0]
        
        # Rotating the right hand position vector
        x, y, dummy = np.matmul(rotation, rightHand)
        
        # Updating the right hand's position
        person.rightx1, person.righty1 = x[0]-5, y[0]
        
        scoreBoard() # Display score board

        glFlush() # Force display

        # Display score
        glColor3f(1.0, 1.0, 1.0)
        showScore(345, 80, score)
        showScore(373, 80, 0)

        # FPS
        time.sleep(0.01)

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(600, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Archery Championship")
glutDisplayFunc(showScreen)
glutMainLoop()
