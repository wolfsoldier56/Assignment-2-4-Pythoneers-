"""
So far we have written programs which accept input 
from the user via keyboard and display the generated output 
on the standard output (console).

This activity has the following disadvantages:
Feasible for small inputs, but cumbersome in case of large inputs.
The entire input has to be entered every time the program is executed.
The output generated is not saved for sharing or later use.

Any information can be stored on a computer disk as file

Python comes with the in-built ability to interact with files. 
Through file handling, 
Python programs can read a file to provide input data 
and output the results into a file for later use.
"""

"""
Files can be opened using the built-in function
    open(file_name, mode=) function

It can either be an absolute path or a relative path as shown below:
    Relative path
        - 'fname.txt' is the relative path of a text file residing in the 
        current working directory from where the python script is being executed.

        - '../fname.txt' is the relative path of a text file outside 
        the current directory where the python script is being executed.

    Absolute path
        - '/Users/edpunk/Documents/fname.txt' is the absolute path
        of a text file which can be opened by the python script from 
        any location as long as it is in the same system.
"""

# open('test/test.txt')
"""
After opening a file and performing some file operations, 
it can be safely closed using the close() method
"""
# f = open('info.txt', 'r')
# f.close()


# read(size=)  read size numbers of bytes of data from a file at a time

f = open('info.txt', 'r')
print(f.read(3))
print(f.read(4))
f.close()

# with open('test.txt', 'r') as f:
#     print(f.read(3))
#     print(f.read(4))

# with open('test.txt', 'r') as f:
#     print(f.read())


# readline(size=) read and return one line at a time from the given file
# returns at most size bytes of data or the data until it encounters 
# the newline character
# with open('info.txt', 'r') as f:
#     print(f.readline(3))
#     print(f.readline(20))

# with open('info.txt', 'r') as f:
#     print(f.readline())

# with open('info.txt', 'r') as f:
#     for line in f:
#         print(line, end='')

# readlines() returns a list of strings representing the lines with newline character
# with open('info.txt', 'r') as f:
#     # print(f.readlines())
#     data = f.readlines()
# print(data)

# write(s) for writing a string s into a file
# s = "New text!"
# with open("info.txt", "w") as f:
#     f.write(s)

# writelines(lines) method writes a list of strings into a file
# lines = ["Hi World\n", "Thank You\n"]
# with open("info.txt", "w") as f:
#     f.writelines(lines)


# Q1
# even_sum = 0
# odd_sum = 0

# while True:
#     user_input = input("Enter a number: ")
    
#     if user_input == "":
#         break
        
#     try:
#         number = int(user_input)
#     except ValueError:
#         print("Please enter a valid number")
#         continue

#     if number % 2 == 0:
#         even_sum += number
#     else:
#         odd_sum += number

# print(f"Sum of even numbers: {even_sum}")
# print(f"Sum of odd numbers: {odd_sum}")


# Q2
# input_string = input("Enter a string: ")
# lowercase_str = ""
# vowel_count = 0
# vowels = 'aeiou'

# for char in input_string:
#     # ASCII values: A-Z (65-90), a-z (97-122)
#     # If character is uppercase, convert to lowercase by adding 32 
#     ascii_value = ord(char)
#     if 65 <= ascii_value <= 90:
#         lowercase_char = chr(ascii_value + 32)
#     else:
#         lowercase_char = char
    
#     lowercase_str += lowercase_char
    
#     if lowercase_char in vowels:
#         vowel_count += 1
       
# print(f"Lowercase string: {lowercase_str}")
# print(f"Number of vowels: {vowel_count}")

# "".join(chr(ord(c) + 32) if (ord(c) >= 65 and ord(c) <= 90) else c for c in input_string)
# sum(1 if c in 'aeiou' else 0 for c in input_string)

# print(f"Lowercase string: {lowercase_str}")
# print(f"Number of vowels: {vowel_count}")


# Q3
# number = int(input("Enter number: "))
# is_prime = True

# if number < 2:
#     is_prime = False


# for i in range(2, number):
#     if number % i == 0:
#         is_prime = False
#         break

# if is_prime:
#     print(f"Number {number} is a prime number.")
# else:
#     print(f"Number {number} is not a prime number.")


# Q4
# rows = int(input("Enter number: "))
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()

# """
# asterisk * is the "unpacking operator"
# takes an iterable and unpacks its elements as individual arguments
# """
# for i in range(1, rows + 1):
#     print(*range(1, i + 1))


# Q5
sentence = input("Enter number: ")
letter_count = 0
digit_count = 0
for char in sentence:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1

print("LETTERS: {letter_count}")
print("DIGITS: {digit_count}")

# letter_count = sum(1 if char.isalpha() else 0 for char in sentence )
# digit_count = sum(1 for char in sentence if char.isdigit())

# print(f"LETTERS: {letter_count}")
# print(f"DIGITS: {digit_count}")
