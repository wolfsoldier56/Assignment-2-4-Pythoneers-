# Question 1
def get_raw_text():
  try:
    with open("Assignment 2/raw_text.txt", "r") as file:
      content = file.read()
      return content
  except Exception as e:
    print("There was a problem reading the file: ", e)
    exit()

def wrap_unicode(code):
  return code % 0x110000

def encrypt_lowercase_char(char, shift1, shift2):
  code = ord(char)

  if code in range(97, 110):
    encrypted_code = code + (shift1 * shift2)
    encrypted_char = chr(wrap_unicode(encrypted_code))
    return encrypted_char

  if code in range(110, 123):
    encrypted_code = code - (shift1 + shift2)
    encrypted_char = chr(wrap_unicode(encrypted_code))
    return encrypted_char

  return char

def encrypt_uppercase_char(char, shift1, shift2):
  code = ord(char)

  if code in range(65, 78):
    encrypted_code = code - shift1
    encrypted_char = chr(wrap_unicode(encrypted_code))
    return encrypted_char

  if code in range(78, 91):
    encrypted_code = code + (shift2 ** 2)
    encrypted_char = chr(wrap_unicode(encrypted_code))
    return encrypted_char

  return char

def encrypt_char(char, shift1, shift2):
  if char.islower():
    return encrypt_lowercase_char(char, shift1, shift2)

  if char.isupper():
    return encrypt_uppercase_char(char, shift1, shift2)

  return char


def encrypt(str, shift1, shift2):
  return "".join([encrypt_char(char, shift1, shift2) for char in str])

# # Testing to see if decryption is possible
# def decrypt_char(char, shift1, shift2):
#   am = nz = AM = NZ = False
#   code = ord(char)

#   if wrap_unicode(code - (shift1 * shift2)) in range(97, 110):
#     am = True
#   if wrap_unicode(code + (shift1 + shift2)) in range(110, 123):
#     nz = True
#   if wrap_unicode(code + shift1) in range(65, 78):
#     AM = True
#   if wrap_unicode(code - (shift2 ** 2)) in range(78, 91):
#     NZ = True

#   if not (am or nz or AM or NZ):
#     return char

#   print(am, nz, AM, NZ)

# def decrypt(str, shift1, shift2):
#   return "".join([decrypt_char(char, shift1, shift2) for char in str])

content = get_raw_text()
print(encrypt(content, 38, 10))