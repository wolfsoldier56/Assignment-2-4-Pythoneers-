# Ask the user to input three numbers
a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))

# Check if the numbers can form a triangle using the triangle inequality theorem
if a + b > c and a + c > b and b + c > a:
    print("Yes, these three lengths can form a triangle.")
else:
    print("No, these three lengths cannot form a triangle.")
