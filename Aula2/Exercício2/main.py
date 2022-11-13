#!/usr/bin/env python

from my_functions import *

maximum_number = 28  # maximum number to test.

def main():
    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for number in range(1,maximum_number+1):
        if isPerfect(number):
            print("O número " + str(number) + " é perfeito.")
        else:
            print('O número ' + str(number) + ' não é perfeito.')

if __name__ == "__main__":
    main()