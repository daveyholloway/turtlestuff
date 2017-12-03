import turtle
import random

# ##############################################################################
# Draw a tree using recursion - New version that creates a new turtle every
# time!
#
# Basically draw a line then calls itself twice at random angles and a reduced 
# size until a specified size of branch is reached.
# ##############################################################################
def newTree(pX, pY, pHeading, pSize, pLimit):

    # Create a turtle
    wTurtle = turtle.Turtle()

    # Lift the pen before moving
    wTurtle.penup()

    # Move the turtle
    wTurtle.setx(pX)
    wTurtle.sety(pY)

    # Put the pen down
    wTurtle.pendown()

    # Set the thickness
    wTurtle.pensize(pSize/10)

    # Set the colour
    if pSize > (pLimit * 2):
        wTurtle.color("brown")
    else:
        wTurtle.color("green")

    # Face the direction passed in and move forward the specified amount
    wTurtle.setheading(pHeading)
    wTurtle.forward(pSize)

    # If the size of branch is still greater than the limit passed in
    # recursively call myself to draw 2 random branches
    if pSize > pLimit:

        newTree(wTurtle.xcor(), wTurtle.ycor(),pHeading-random.randint(1,60),pSize - 15,pLimit)
        newTree(wTurtle.xcor(), wTurtle.ycor(),pHeading-random.randint(-30,30),pSize - 15,pLimit)
        newTree(wTurtle.xcor(), wTurtle.ycor(),pHeading+random.randint(1,60),pSize - 15,pLimit)
       


# ##############################################################################
# Start of main code
#
# ##############################################################################


# Change the window title
turtle.title("Dave's Turtle")
# Use logo mode (North is up)
turtle.mode("logo")

# Create a turtle
wTurtle = turtle.Turtle()

# Set the speed of the turtle
wTurtle.speed('fast')

newTree(-50,-100,0,70,20)
newTree(0,-100,0,70,20)
newTree(50,-100,0,70,20)


