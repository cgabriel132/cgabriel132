#!/usr/bin/env python

maximum_number = 11  # maximum number to test.


def getDividers(value):
    """
    Return a list of dividers for the number value
    :param value: the number to test
    :return: a list of dividers.
    """
    for number in range(2, value):
        remainder = value % number
        if remainder == 0: # Não é primo
            print('This number is not prime. Tested dividers are ' + str(list(range(2,number+1))))
            return False

    return True # Caso seja primo



def isPerfect(value):
    """
    Checks whether the number value is perfect.
    :param value: the number to test.
    :return: True or False
    """

    soma = 0

    for number in range(1, value):
        if value % number == 0:
            soma += number # soma = soma + number

    if value == soma:
        return True
    else:
        return False

def main():
    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for number in range(1,maximum_number+1):
        if isPerfect(number):
            print("O número " + str(number) + " é perfeito")

    print('Starting to compute dividers up to ' + str(maximum_number))
    for number in range(1,maximum_number+1):
        if getDividers(number):
            print('Number ' + str(number) + ' is prime.')
        else:
            print('Number ' + str(number) + " is not prime.")

if __name__ == "__main__":
    main()