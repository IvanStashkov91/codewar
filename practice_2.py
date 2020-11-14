'''
Implement a function that adds two numbers together and returns their sum in binary.
The conversion can be done before, or after the addition.
The binary number returned should be a string.
'''
def add_binary(a, b):
    result = bin(a + b)
    return str(result[2:])

#or
def add_binary2(a,b):
    return str(bin(a+b))[2:]

print(add_binary(2325, 24356))
print(add_binary2(4256378, 1456789))