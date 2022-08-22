import sys
import sdl2
from OpenGL.GL import *
from OpenGL.GLU import *
import math
from PIL import Image

N = 20
 
def InitGL(Width, Height):             
    glClearColor(0.0, 0.0, 0.0, 0.0) 
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)               
    glEnable(GL_DEPTH_TEST)            
    glShadeModel(GL_SMOOTH)            
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def map(valor, v0, vf, m0, mf):
    return m0+(((valor-v0)*(mf-m0))/(vf-v0))




def cor(i,j):
    theta = map(i,0,N,-math.pi/2,math.pi/2)
    phy = map(j,0,N,0,2*math.pi)
    r = 0.5+0.5*math.sin(theta)
    g = 0.5+0.5*math.cos(phy)
    b = r
    return r, g, b

def defZ1(x,y):
    return x**2 + y**2

def defZ2(x,y):
    return x**2 - y**2

a=0
r=1
var = 4/N
def forma1():
    global a
    glLoadIdentity()       
    glTranslatef(0.0,5.0,-35.0)
    glRotatef(a,0.0,1.0,0.0)
    y =-2
    for i in range(0,N):
        glBegin(GL_TRIANGLE_STRIP)
        x=-2
        for j in range(0,N+1):
            r, g, b = cor(i,j)
            z = defZ1(x,y)
            glColor3f(r,g,b)
            glVertex3f(x,y,z)
            r, g, b = cor(i-1,j)
            z = defZ1(x,y+var)
            glColor3f(r,g,b)
            glVertex3f(x,y+var,z)
            x +=var
        glEnd()
        y+=var

    a+=0.2

def forma2():
    global a
    glLoadIdentity()       
    glTranslatef(0.0,-5.0,-35.0)
    glRotatef(a,0.0,1.0,0.0)
    y =-2
    for i in range(0,N):
        glBegin(GL_TRIANGLE_STRIP)
        x=-2
        for j in range(0,N+1):
            r, g, b = cor(i,j)
            z = defZ2(x,y)
            glColor3f(r,g,b)
            glVertex3f(x,y,z)
            r, g, b = cor(i-1,j)
            z = defZ2(x,y+var)
            glColor3f(r,g,b)
            glVertex3f(x,y+var,z)
            x +=var
        glEnd()
        y+=var

    a+=0.2

def desenha():
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)    
    glPushMatrix()
    forma1()
    glPopMatrix()
    glPushMatrix()
    forma2()
    glPopMatrix()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

sdl2.SDL_Init(sdl2.SDL_INIT_EVERYTHING)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MAJOR_VERSION, 2)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MINOR_VERSION, 1)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_PROFILE_MASK,sdl2.SDL_GL_CONTEXT_PROFILE_CORE)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_DOUBLEBUFFER, 1)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_DEPTH_SIZE, 24)
sdl2.SDL_GL_SetSwapInterval(1)
window = sdl2.SDL_CreateWindow(b"Esfera", sdl2.SDL_WINDOWPOS_CENTERED, sdl2.SDL_WINDOWPOS_CENTERED, WINDOW_WIDTH, WINDOW_HEIGHT, sdl2.SDL_WINDOW_OPENGL | sdl2.SDL_WINDOW_SHOWN)
if not window:
    sys.stderr.write("Error: Could not create window\n")
    exit(1)
glcontext = sdl2.SDL_GL_CreateContext(window)
InitGL(WINDOW_WIDTH,WINDOW_HEIGHT)
running = True
event = sdl2.SDL_Event()
while running:
    while sdl2.SDL_PollEvent(ctypes.byref(event)) != 0:
        if event.type == sdl2.SDL_QUIT:
            running = False
        if event.type == sdl2.events.SDL_KEYDOWN:
            if event.key.keysym.sym == sdl2.SDLK_ESCAPE:
                running = False
    desenha()
    sdl2.SDL_GL_SwapWindow(window)
