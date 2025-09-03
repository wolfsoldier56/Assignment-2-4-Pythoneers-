import turtle
import math

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

# 
# Trial attempt 1 Sean using turtle to draw a triangle:
if Possible_triangle == True:
    #inflate the three numbers by 100 so that the triangle isnt tiny (if you used stupidly sized numbers then your triangle wont fit, besides who wants a big triangle anyway)
    '''
    la = (a*10)
    lb= (b*10)
    lc = (c*10)
    currently useless makes a messy triangle
    '''
    #calculate the angles for the triangle based off the lengths a,b,c
    A = math.degrees(math.acos((b*b + c*c - a*a)/(2*b*c)))
    B = math.degrees(math.acos((b*b + c*c - a*a)/(2*a*c)))
    C = math.degrees(math.acos((b*b + c*c - a*a)/(2*b*a)))
    print(A,B,C)

    #use the calculated angles and given measurements to draw a triangle with turtle cause its funny.
    triangle = turtle.Turtle()
    