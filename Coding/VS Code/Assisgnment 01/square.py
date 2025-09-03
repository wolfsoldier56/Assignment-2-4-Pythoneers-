# Part B 
size = int(input("Enter the size of the square: "))

for i in range(size):
    if i == 0 or i == size - 1:
        print('* ' * size)
    else:
        print('* ' + '  ' * (size - 2) + '* ')