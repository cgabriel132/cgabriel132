#!/usr/bin/env python3

from collections import namedtuple

Complex = namedtuple('Complex', ['r', 'i'])

def addComplex(x, y):

    # (a+bi)+(c+di) = (a+c) + (b+d)i

    a = x.r
    b = x.i
    c = y.r
    d = y.i

    real = a + c
    imaginary = b + d

    return Complex(real, imaginary)

def multiplyComplex(x, y):

    # (a+bi)(c+di) = (ac−bd) + (ad+bc)i

    a = x.r
    b = x.i
    c = y.r
    d = y.i

    real = a * c - b * d
    imaginary = a * d + b * c

    return Complex(real, imaginary)

def printComplex(x):
    
    # Adapt code to use named tuples
    real = x.r
    imaginary = x.i
    print(str(real) + "+" + str(imaginary) + "i")

def main():
    
    # Define two complex numbers as tuples of size two
    c1 = Complex(5, 7)  # Use order when not naming
    c2 = Complex(-2, 4)  # If items are names order is not relevant
    printComplex(c1)
    printComplex(c2)

    # Test sum of both numbers
    c3 = addComplex(c1, c2)
    print("The sum of both numbers is:")
    printComplex(c3)

    # Test multiply
    print("Result of multiplication is:")
    printComplex(multiplyComplex(c1, c2))


if __name__ == '__main__':
    main()