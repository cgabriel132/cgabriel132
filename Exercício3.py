#!/usr/bin python3

from colorama import Fore, Back, Style

maximum_number = 11

def isPrime(value):

    for number in range(2, value):
        remainder = value % number
        if remainder == 0: # Não é primo
            print('This number is not prime. Tested dividers are ' + str(list(range(2, number +1))))
            return False

    return True # Caso não seja primo

    

def main():
    print("Starting to compute prime numbers up to " + str(maximum_number))

    for number in range(1, maximum_number + 1):
        if isPrime(number):
            print( Style.BRIGHT + Fore.GREEN + 'Number ' + str(number) + ' is prime.' + Style.RESET_ALL)
        else:
            print('Number ' + str(number) + ' is not prime.')

if __name__ == "__main__":
    main()
