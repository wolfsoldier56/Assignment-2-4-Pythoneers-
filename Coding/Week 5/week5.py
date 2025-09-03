# def sum(lower, upper):

#     result = 0
#     while lower <= upper:
#         result += lower
#         lower += 1
#     return result



# while True:
#   try:
#       lower = int(input("Enter the lower bound: "))    
#       upper = int(input("Enter the upper bound: "))
#       if lower > upper:
#           print("Lower bound must be less than or equal to upper bound.")    
#           continue
#       else:
#           print("The sum of integers from", lower, "to", upper, "is:", sum(lower, upper))
#           break
#   except ValueError:
#      print("Please enter valid integers for the bounds.")                        
#      continue

# for i in (-50, 100, -4.4, 3.14, 0, -0.5):
#     print(round(i))
#     print(abs(i))

# print(range(10,50,-1))
          
# def factorial(n):
#     if n < 0:
#         return "Factorial is not defined for negative numbers."
#     elif n == 0 or n == 1:
#         return 1
    
#     else:
#         result = 1
#         for i in range(2, n + 1):
#             result *= i
#         return result    

# n = 5
# print(f"The factorial of {n} is: {factorial(n)}")

# def fact_rec(n):
#     if n < 0:
#         return "Factorial is not defined for negative numbers."
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         return n * fact_rec(n - 1)

# print(f"The factorial of {3} is: {fact_rec(3)}")

# def xpowy_loop(x, y):
#     return x ** y

# print(xpowy_loop(5, 5)) 

    


# def xpowy_loop(base, exp):
#     pow = 1
#     for i in range(exp):
#         pow = pow * base
#     return pow
    
# print(xpowy_rec(5, 0))

# def xpowy_rec(base, exp):
#     if exp == 0:
#         return 1
#     else :
#         return base * xpowy_rec(base, exp - 1)
    
# print(xpowy_rec(5, 5))

# def fib(n):
#     if n <= 0:
#         return "Fibonacci is not defined for non-positive integers."
#     elif n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     else:
#         a, b = 1, 1
#         for i in range(2, n):
#             a, b = b, a + b
#         return b
    
# print(f"The {10}th Fibonacci number is: {fib(10)}")

# def fib_rec(n):
#     if n <= 0:
#         return "Fibonacci is not defined for non-positive integers."
#     elif n == 1 or n == 2:
#         return 1
#     else:
#         return fib_rec(n - 1) + fib_rec(n - 2)

# print(f"The {10}th Fibonacci number is: {fib_rec(10)}")


# def count_digits(n):
#     if n < 0:
#         n = -n  # Make n positive if it's negative
#     count = 0
#     while n > 0:
#         n //= 10  # Remove the last digit
#         count += 1
#     return count
# print(f"The number of digits in 123456789 is: {count_digits(123456789)}")

# def counter(n):
#     if n < 0:
#         n = -n  # Make n positive if it's negative
#     count = 0
#     while n > 0:
#         n //= 10  # Remove the last digit
#         count += 1
#     return count

# def counter_str(n): #easiest string way
#     if n <0:
#         n = -n
#     else:
#         return len(str(n))
    
# def counter_rec(n):
#     if n < 0:
#         n = -n  # Make n positive if it's negative
#     if n == 0:
#         return 0
#     else:
#         return 1 + counter_rec(n // 10)


def palindrome(s):
    s = s.lower().replace(" ", "") #normalisze: lowercase and remove spaces
    return s == s[::-1]  # Check if the string is equal to its reverse

print(palindrome("racecar"))

def palindrom_rec(s):
    s = s.lower().replace(" ", "") # Normalize: lowercase and remove spaces
    if len(s) <= 1:
        return True  # A single character or empty string is a palindrome
    if s[0] != s[-1]:
        return False  # First and last characters must match
    return palindrom_rec(s[1:-1])  # Check the substring without first and last characters





def palindrome_str(s):
    s = s.lower().replace(" ", "")  # Normalize: lowercase and remove spaces
    if s == s[::-1]:
        return True
    else:
        return False
    

print(palindrome_str("racecar"))
    
