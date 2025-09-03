print("Which number is the smallest and largest of the three?")
a = int(input("Input first number: "))
b = int(input("Input second number: "))
c = int(input("Input third number: "))
if a==b==c:
    print("All numbers are equal")
else:
    if a>b and a>c:
        print("Largest is: ",a)
    elif b>a and b>c:
        print("Largest is: ",b)
    else:
        print("Largest is: ", c)
    if a<b and a<c:
        print("Smallest is: ", a)
    elif b<a and b<c:
        print("Smallest is", b)
    else:
        print("Smallest is", c)



