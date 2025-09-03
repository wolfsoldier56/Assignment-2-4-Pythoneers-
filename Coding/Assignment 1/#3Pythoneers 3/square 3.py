'''
Group Name: The Three Pythoneers
Group Members:
Jorden Roderique - S243191
Sean William Le Roux - S375991
Gabriel Popesco - S393611
'''

# --- Part B: Square ---
#start section 1(b) create a hollow square with sides of length n where n is provided by the user.

# Get n from user
def getUserInt():
    userInput = input("Enter the size of the square or press 'Enter' to exit: ")
    if userInput.strip() == "":
        return None
    try:
        return int(userInput)
    except ValueError:
        print("Please enter a valid integer.")
        return getUserInt()

# Print square of size n to the terminal
def printNSquare(n):
  for i in range(n):
      if i == 0 or i == n - 1:
          print('* ' * n)
      else:
          print('* ' + '  ' * (n - 2) + '*')

if __name__ == '__main__':
  while True:
      size = getUserInt()
      if size is None:
          break
      if size >= 0:
          printNSquare(size)
      else:
          print("Please enter a positive integer.")
