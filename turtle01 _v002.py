#!/usr/bin/env python3

import sys
import turtle
import random

mineChar = "X"
clearChar = "."

# Draw the starting grid
def grid(turtle, gridSize, xLimit, yLimit):
    for i in range(gridSize):
        draw(turtle,0,ylimit-(i+1)*(ylimit/gridSize),xLimit,ylimit-(i+1)*(ylimit/gridSize),"grey")
        draw(turtle,i*(xlimit/gridSize),0,i*(xlimit/gridSize),yLimit,"grey")

def move(turtle, x, y):
    turtle.pu()
    turtle.setx(x)
    turtle.sety(y)
    turtle.pd()

def draw(turtle, x1, y1, x2, y2, colour):
    move(turtle, x1, y1)
    turtle.pencolor(colour)
    turtle.setposition(x2, y2)

def cell(turtle, x, y, sx, sy, colour):
    draw(turtle,x,y,x+sx, y, colour)
    draw(turtle,x+sx, y, x+sx, y+sy, colour)
    draw(turtle,x+sx, y+sy, x, y+sy, colour)
    draw(turtle,x, y+sy, x, y, colour)

# Create a maze that's full of mines!
def createMaze(xSize,ySize):
    # create an empty list
    mazeArray=[]
    # create a line of mines
    allMines=xSize*mineChar
    # now build a list of these
    for i in range(ySize):
        mazeArray.append(allMines)
    return(mazeArray)

# Print a text representation of the minefield
def printMineField(mf):

    # Loop thru the list
    for i in range(len(mf)):
        print(mf[i])
    print()

def setMine(mf,x,y):
    s=list(mf[y])
    s[x]=mineChar
    mf[y]="".join(s)
    return(mf)

def clearMine(mf,x,y):
    s=list(mf[y])
    s[x]=clearChar
    mf[y]="".join(s)
    return(mf)

def inactiveMine(mf,x,y):
    return(mf[y][x]==clearChar)

# A further sensible check, is the destination cell a valid one
def validDest(mf, curx, cury, x, y, gridSize):

    for i in range(-1,1):
        for j in range(-1,1):

            checkX = x + i
            checkY = y + j

            if (checkX != curx) and (checkY != cury):
                print("checking (" + str(checkX) + ", " + str(checkY) + ")")
                if inactiveMine(mf,checkX, checkY):
                   return(False)
            else:
                print("ignoring (" + str(checkX) + ", " + str(checkY) + ")")
    return (True)


# Make a route through the mines
def makeRoute(mf,x,y,gridSize):

    printMineField(mineField)

    # Are we done?
    if y == gridSize-1:
        mf=clearMine(mf,x,y)
        return mf
    else:
        sensible = False

        mf=clearMine(mf,x,y)

        while not sensible:
            dx = random.randint(-5,5)
            dy = random.randint(-5,5)

            if dx > 1:
                dx = 1
            if dx < -1:
                dx = -1
            if dy > 1:
                dy = 1
            if dy < -1:
                dy = -1

            if dx==0 and dy==0:
                sensible = False
            elif x+dx < 0:
                sensible = False
            elif x+dx > gridSize-1:
                sensible = False
            elif y+dy < 0:
                sensible = False
            elif y+dy > gridSize -1:
                sensible = False
            elif validDest(mf,x,y,x+dx,y+dy,gridSize)==False:
                sensible = False
            else:
                sensible = True

        

        makeRoute(mf, x+dx, y+dy, gridSize)
        
# **********************************************************************
# Set up some variables and do a bit of initialisation
#
# **********************************************************************
xlimit = 700
ylimit = 700
gridSize = 10
cellSizeX = xlimit/gridSize
cellSizeY = ylimit/gridSize

# Create screen and turtle.
screen = turtle.Screen()
screen.title('Death Maze 2000!')
screen.setup (width=800, height=800, startx=0, starty=0)
t = turtle.Turtle()
t.speed(0)

#screen.screensize(700,700)
screen.setworldcoordinates(0,0,700,700)

# Plot the grid
# grid(t, gridSize, xlimit, ylimit)

# Set up a maze array, use a list of strings to do 2 dimensions
mineField=createMaze(gridSize, gridSize)

# Print off a text version
# printMineField(mineField)

# Build a path through
# Start half way through the top row
myx = int(gridSize/2)-1
myy = 0

makeRoute(mineField,myx,myy, gridSize)

printMineField(mineField)

