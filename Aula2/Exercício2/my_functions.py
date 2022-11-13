#!/usr/bin/env python

def getDividers(value):
    """
    Return a list of dividers for the number value
    :param value: the number to test
    :return: a list of dividers.
    """

    dividers = []
    for number in range(1, value):
        remainder = value % number
        if remainder == 0: # É divisor
            print(str(number) + ' is a divider of ' + str(value))
            dividers.append(number)

    return dividers


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