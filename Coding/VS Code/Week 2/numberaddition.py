print("addition of numbers in a range defined")
lower=int(input("enter the lower bound "))
upper=int(input("enter the upper bound "))
sum=0
for count in range(lower,upper+1):
    sum=sum+count
print("sum is", sum)

