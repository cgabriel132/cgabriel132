#!/usr/bin/env python3

def addComplex(x, y):
    
    # (a+bi)+(c+di) = (a+c) + (c+d)i

    a, b = x
    c, d = y

    real = a + c
    imaginary = b + d

    return(real,imaginary)

def multiplyComplex(x, y):

    # (a+bi)(c+di) = (ac−bd) + (ad+bc)i

    a, b = x
    c, d = y

    real = a * c - b * d
    imaginary = a * d + b * c

    return(real, imaginary)

def printComplex(x):
    
    real, imaginary = (x)
    print(str(real) + "+" + str(imaginary) + "i")

def main():

    # Define two complex numbers as tuples of size two
    c1 = (5, 3)
    c2 = (-2, 7)

    # Test sum
    c3 = addComplex(c1, c2)
    print("The sum of the two complex numbers is:")
    printComplex(c3)

    # Test multiply
    c4 = multiplyComplex(c1, c2)
    print("c1 times c2 is:")
    printComplex(c4)


if __name__ == '__main__':
    main()