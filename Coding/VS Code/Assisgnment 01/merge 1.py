import turtle
import math

# --- Part A: Triangle ---
#start section 1(a) create a triangle with if possible with 3 user inputs.
# Ask the user to input three numbers
a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))
Possible_triangle = False

# Check if the numbers can form a triangle using the triangle inequality theorem
if a + b > c and a + c > b and b + c > a:
    print("Yes, these three lengths can form a triangle.")
    Possible_triangle = True
else:
    print("No, these three lengths cannot form a triangle.")

# Trial attempt 1 Sean using turtle to draw a triangle:
if Possible_triangle == True:
    #inflate the three numbers by 100 so that the triangle isnt tiny (if you used stupidly sized numbers then your triangle wont fit, besides who wants a big triangle anyway)
    '''
    la = (a*10)
    lb= (b*10)
    lc = (c*10)
    currently useless makes a messy triangle
    '''
    # calculate the angles for the triangle based off the lengths a,b,c
    A = math.degrees(math.acos((b*b + c*c - a**2)/(2*b*c)))
    B = math.degrees(math.acos((a**2 + c*c - b**2)/(2*a*c)))
    C = math.degrees(math.acos((b*b + a**2 - c**2)/(2*b*a)))
    print(A, B, C)

    # use the calculated angles and given measurements to draw a triangle with turtle cause its funny.
    triangle = turtle.Turtle()
    turtle.screensize(100, 100)
    print("Please close the turtle graphics window to continue.")
    '''
    my messy attempt at trying to get the canvas to shrink or zoom in on the center to fit the turtle without having to do the long way
    triangle.penup()
    #triangle.goto(100,150)
    triangle.pendown()
    triPosx, triPosy = triangle.pos()
    ##set screen size and zoom on triangle:
    width = 1
    height = 1
    screen = turtle.Screen
    turtle.setworldcoordinates(triPosx - width, triPosy - height, triPosx / width, triPosy / width)
    '''
    turtle.forward(c)
    turtle.left(180 - B)
    turtle.forward(a)
    turtle.left(180 - C)
    turtle.forward(b)
    turtle.left(180 - A)
    turtle.done()
    

# --- Part B: Square ---
size = int(input("Enter the size of the square: "))

for i in range(size):
    if i == 0 or i == size - 1:
        print('* ' * size)
    else:
        print('* ' + '  ' * (size - 2) + '* ')
