#----------------------------------------------------------------#
# Title: Lab 1-2
# Change Log:
# D. Rodriguez, 2019-01-14, Created File
#----------------------------------------------------------------#

# def basic_math(a, b):
#     print("The sum of ", a, " and ", b, "is: ", a + b)
#     print("The difference of ", a, " and ", b, "is: ", a - b)
#     print("The product of ", a, " and ", b, "is: ", a * b)
#     print("The quotient of ", a, " and ", b, "is: ", a / b)

def sum(a, b):
    return a + b

def difference(a, b):
    return a - b

def product(a, b):
    return a * b

def quotient(a, b):
    return a / b  

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# basic_math(a, b)
print("The sum of ", a, " and ", b, "is: ", sum(a, b))
print("The difference of ", a, " and ", b, "is: ", difference(a, b))
print("The product of ", a, " and ", b, "is: ", product(a, b))
print("The quotient of ", a, " and ", b, "is: ", quotient(a, b))