'''
Group Name: The Three Pythoneers
Group Members:
Jorden Roderique - S243191
Sean William Le Roux - S375991
Gabriel Popesco - S393611
'''

# --- Part A: Triangle ---
#start section 1(a) create a triangle with if possible with 3 user inputs.

import turtle
import math

# Handle user input
def getUserSide():
    userInput = input("")
    try:
        return abs(float(userInput))
    except ValueError:
        print("Please enter a valid number: ", end="")
        return getUserSide()

# Ask user for 3 sides and handle their input
def getSides():
     print("Enter triangle sides between 10 and 300 for best results when drawing")
     print("Enter the first side: ", end="")
     a = getUserSide()
     print("Enter the second side: ", end="")
     b = getUserSide()
     print("Enter the third side: ", end="")
     c = getUserSide()

     return [a, b, c]

# Determine whether 3 sides of various lengths can form a valid triangle using triangle inequality theorem
def isValidTriangle(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)

# calculate the angles for the triangle based off the lengths a,b,c- law of cosines 
def getAnglesFromSides(a, b, c):
        A = math.degrees(math.acos((b*b + c*c - a**2)/(2*b*c)))
        B = math.degrees(math.acos((a**2 + c*c - b**2)/(2*a*c)))
        C = math.degrees(math.acos((b*b + a**2 - c**2)/(2*b*a)))

        return [A, B, C]

# Handle graphical drawing of said triangle
def drawTriangle(sides, angles):
    a, b, c = sides
    A, B, C = angles
    # Setup screen
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.title("Triangle Drawer")

    # Create a turtle object for drawing triangle
    triangle = turtle.Turtle()

    # use the calculated angles and given measurements to draw a triangle with turtle cause its funny.
    triangle.forward(c)
    triangle.left(180 - B)
    triangle.forward(a)
    triangle.left(180 - C)
    triangle.forward(b)
    triangle.left(180 - A)

    triangle.hideturtle()
    screen.exitonclick()


if __name__ == '__main__':
    # Triangle sides
    sides = getSides()

    # Validate whether provided sides can form a triangle
    valid = isValidTriangle(*sides)

    if valid:
        print("Yes, these three lengths can form a triangle.")

        # Triangle angles
        angles = getAnglesFromSides(*sides)

        # Draw triangle
        drawTriangle(sides, angles)
    else:
        print("No, these three lengths cannot form a triangle.")
