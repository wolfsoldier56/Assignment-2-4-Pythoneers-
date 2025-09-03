while True:
    print("Hello and welcome to triangle checker")
    print("I will verify if your lengths can form a triangle!")
    print()
    a = float(input("Enter first side "))
    b = float(input("Enter second side "))
    c = float(input("Enter third side "))
    if a+b>c and a+c>b and b+c>a:
        print("Yes, these lengths can form a triangle")
        print()
    else:
        print("No these lengths cannot form a triangle")
        print()
    print("Press 1 to continue or 2 to end program")
    print()
    while True:
        choice=int(input("1/2? "))
        if choice == 1:
            print("Continuing program...")
            print()
            break
        elif choice == 2:
            print("Ending program...")
            print()
            
            exit()
        else:
            print("Invalid input, Press 1 to continue or 2 to end program ")
            print()