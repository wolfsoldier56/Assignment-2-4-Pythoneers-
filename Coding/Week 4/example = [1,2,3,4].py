# example = [1,2,3,4]
# print(example)

# example [3] = 0
# print(example)

# example = [1,3]
# print(example)

# example.insert(1,2)
# print(example)

# #output [1, 2, 3] 

# example.insert(3,4)
# print(example)

# #output [1, 2, 3, 4] - put together 

# example.append(5)
# print(example) 

# # output [1, 2, 3 ,4 ,5] - add 5 at the end 

# example.extend([6, 7])
# print(example)

# #output [1, 2, 3, 4, 5, 6, 7]- extends by 6 and 7 

# print(example.pop(6))
# print(example)

#- pop removes last element from the list [1, 2, 3 ,4 ,5 ,6] 0-6( 6th element is 7)
#without paramter removes the last element naturally 

# def function_name():
#     #sample fucntion code- simple function - call on fucntion 
#     print('Hello')
# function_name()

# def function_name(name):
#     print('hello', name) 
# function_name("joe")
# # input variable - call on function with changing variable 
# function_name(2)

# def sqr(num1):
#     sqrt = num1 * num1 
#     print(sqrt)

# sqr(2) # prints result of function with 2 as variable 

# def sqr(num1):
#     sqrt = num1 * num1 
#     return(sqrt)

# print(sqr(2)) #print sqr 

# num2 = int(input("Enter first number"))
# num3 = int(input("Enter a second number"))

# def addnum(num2, num3):
#     addition = num2 + num3
#     return addition
# print(addnum(num2, num3))

# #adds two numbers 

# num2 = int(input("Enter first number"))
# num3 = int(input("Enter a second number"))

# def addnum(num2, num3):
#     addition = num2 + num3
#     subtraction = num2 - num3
#     return addition, subtraction

# x, y = addnum(num2, num3)
# print(x)
# print(y)

#-add and subtracts in same function- prints results on seperate lines 

# def calculator(num2, num3, opn):
#     if opn == "add":
#         out = num2 + num3
#     elif opn == "sub":
#         out = num2 - num3
#     return out

# print(calculator(5, 3, "add") )
# print(calculator(5, 3, "sub") )

# student_details = {
#     's1':{'name':'sarah','country':'australia'},
#     's2':{'name':'nathan','country':'india'},
#     's3':{'name':'joe','country':'china'}
# }

# print(student_details['s1'])
# print(student_details['s1']['country'])

#Q1 - total of a list 

# total = 0
# numbers = (input("Enter any range of whole numbers, put commas in between: "))
# numbers_list = numbers.split(",")

# # total = sum(map(int, numbers_list)) #map used here as it seperate each iterable in the function 
# # print(total)
# # #or you can use 

# for n in numbers_list:
#     total += int(n)

# print(total)

#Q2 - total of a list of numbers 

# x = int(input("Enter a number: "))
# y = int(input("Enter a number: "))



# def sum_numbers():  #defining the function 
#     upperlimit = max(x, y)
#     lowerlimit = min (x,y)
#     range_num = list(range(lowerlimit, upperlimit + 1))
#     total = sum(range_num)
#     return total
# print(sum_numbers())

#total = sum(map(int, range_num)) - not needed in this case 

#3 - variable data 

# my_dict = {"b":20, "a":35,}
# my_dict["c"]= 40 # adds changes value 
# my_dict["b"] = 21
# list_sort = sorted(my_dict.keys()) #sorts only keys
# print(list_sort)
# del my_dict["b"] #deletes key "b"
# list_sort2 = sorted(my_dict.keys()) #sorts only keys
# print(list_sort2)

#Q4 failed attempt 

# print("Find min numbers in list")
# numbers = (input("Enter any range of whole numbers, put commas in between: "))
# numbers_list = numbers.split(",")
# minboy = min(numbers_list)

# minboyint = int(minboy)

# if isinstance(minboyint, int):  #isinstance checks for input to be what you say ie int,float,string and if it is rturns true if not returns false 
#     print(minboy)
# else:
#     print("Please try again").  #true and fale only using el and if- as minboyint is always an int- program will always be true 

#Q4 attempt 2 
    
# print("Find min numbers in list")


# while True:
#    numbers = (input("Enter any range of whole numbers, put commas in between OR press Enter to exit: ")) #must stay within while true loop but out of if loop as its input 
#    numbers_list = numbers.split(",") #must stay within if loop, after  input 

#    if numbers == "":
#       print("Exiting program")   #if user presses enter- exits 
#       break
   
#    try:
#       numbers_list = [int(n) for n in numbers_list] #checks each iterable and converts it ot an int- loops for the n in the list. good trick 
   
#    except ValueError:
#       print("Invlad input")
#       continue
   
#    else:
#       minboy = min(numbers_list)
#       print("Minimum is : ", minboy)
#       break

#Q5 

my_dict = {
1:10, 2:20,
3:30, 4:40,
5:50,6:60,
}

print(my_dict)

dict1 = {1:10, 2:20}
dict2 = {3:30, 4:40}
dict3 = {5:50,6:60}

combined = {**dict1, **dict2, **dict3} #

print(combined)



# summary = (dic1, dic2, dic3) 

# print(summary)

# result = {}.  #starts with empty dictionary 
# for d in (dic1, dic2, dic3):   #loop through each dictionary 
#     result.update(d) #adds key values from each dictinoary as it loops through each d (each dic1, dic2 etc)

# print("Expected Results:", result)











    





    

























