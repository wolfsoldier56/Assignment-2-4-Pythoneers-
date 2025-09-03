with open(r"C:\Users\Gabriel\Desktop\Assignment 2\raw_text.txt", "r") as file:
    content = file.read()
print(content)

def warpcode():
    codes = []
    for char in content:
        codes.append(ord(char))
    return codes

print(warpcode())

def warpcode():
    return [ord(char) for char in content] 

print(warpcode())