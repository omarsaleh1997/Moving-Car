from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *

def myinit():
    glMatrixMode(GL_PROJECTION)
    glClearColor(0,1,0,0)
    glClear(GL_COLOR_BUFFER_BIT)
    # glOrtho(-10,10,-10,10,-10,10)
    gluPerspective(60,1,0.1,50)
    gluLookAt(10,10,10,0,0,0,0,1,0)
x=0
angle=0
reverse=True
def draw1():
    glClear(GL_COLOR_BUFFER_BIT)
    global x
    global angle
    global reverse

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glColor3f(0, .8, .8)
    glTranslate(-10, -1, 0)
    glScale(55, .05, 10)
    glutSolidCube(1)

    glLoadIdentity()
    glColor3f(0, .3, .8)
    glTranslate(-10, -1, 0)
    glScale(30, .5, 5)
    glutSolidCube(.2)

    glLoadIdentity()
    glColor3f(0, .3, .8)
    glTranslate(0, -1, 0)
    glScale(30, .05, 5)
    glutSolidCube(.2)

    glLoadIdentity()
    glColor3f(0, .3, .8)
    glTranslate(10, -1, 0)
    glScale(30, .05, 5)
    glutSolidCube(.2)

    glLoadIdentity()
    glColor3f(0, .5, .5)
    glTranslate(10, 3.5, 0)
    glScale(30, 8, 2)
    glutSolidCube(.2)

    glLoadIdentity()
    glColor3f(0, .5, .5)
    glTranslate(3.5, 3.5, 0)
    glScale(30, 8, 2)
    glutSolidCube(.2)

    glLoadIdentity()
    glColor3f(0, .5, .5)
    glTranslate(-3.5, 3.5, 0)
    glScale(30, 8, 2)
    glutSolidCube(.2)

    glLoadIdentity()
    glColor3f(0, .5, .5)
    glTranslate(-10.5, 3.5, 0)
    glScale(30, 8, 2)
    glutSolidCube(.2)

    glLoadIdentity()
    glColor3f(0, .5, .5)
    glTranslate(-17.5, 3.5, 0)
    glScale(30, 8, 2)
    glutSolidCube(.2)

    glLoadIdentity()
    glColor3f(0, .5, .5)
    glTranslate(0, 1, 5.5)
    glScale(200, 3, 7)
    glutSolidCube(.2)

####################
    glLoadIdentity()
    glColor3f(0,0,0)
    glTranslate(x+1,.25,.5)
    glScale(1,.25,0.5)
    glutSolidCube(5)

    glLoadIdentity()
    glTranslate(x+.5,.65,0.64)
    glScale(.5,0.4,0.5)
    glutSolidCube(5)

#toras
    glColor3f(1,1,0)
    glLoadIdentity()
    glTranslate(x+2.5,2.5*.25,2.5)
    glRotate(angle,0,0,1)
    glutWireTorus(0.125,0.5,100,100)

    # glColor3f(0, 0, 1)
    # glLoadIdentity()
    # glTranslate(x+.25, 2.5 * .25, .05)
    # glRotate(angle, 0, 0, 1)
    # glutWireTorus(0.125, 0.5, 12, 8)

    glColor3f(1, 1, 0)
    glLoadIdentity()
    glTranslate(x+0.25, 2.5 * .25, 2.5)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.125, 0.5, 100, 100)



    # sphere
    glColor(1, 1, 0)
    glLoadIdentity()
    glTranslate(x+3.5, .6, 1.7)
    glRotate(angle, 0, 0, 1)
    glutWireSphere(.2, 10, 100)

    glColor(1, 1, 0)
    glLoadIdentity()
    glTranslate(x + 3.5, .6, -.1)
    glRotate(angle, 0, 0, 1)
    glutWireSphere(.2, 10, 100)






    angle -=0.1
    if reverse==True:
        x-=0.01
        if x<-20:
            reverse=False
    if reverse==False:
        x+=.01
        if x>8:
            reverse=True









def main():

    draw1()
    

    glFlush()


###########################################################################################
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"Moving car")
glutDisplayFunc(main)
glutIdleFunc(main)
myinit()
glutMainLoop()
