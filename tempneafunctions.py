import math

inp = int(input('Enter a number'))

pi = math.pi

exp = int(input('Enter power'))

print('Pi =', pi)

def sin(num):
    print(math.sin(math.radians(num)))
sin(inp)

def cos(num):
    print(math.cos(math.radians(num)))
cos(inp)

def tan(num):
    print(math.tan(math.radians(num)))
tan(inp)

def fact(num):
    print(math.factorial(num))
fact(inp)

def sqr(num):
    print(num**2)
sqr(inp)

def sqrroot(num):
    print(num**(1/2))
sqrroot(inp)

def exponent(num,power):
    print(num**power)
exponent(inp,exp)

#For arcsin , arctan , arccos its the same function just math.asin (for instance) , so they have not been included.