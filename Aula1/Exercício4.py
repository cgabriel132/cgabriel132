#1/usr/bin/env python

maximum_number = 496

def isPerfect(value):

    soma = 0

    for number in range(1, value):
        if value % number == 0:
            soma += number # soma = soma + number

    if value == soma:
        return True
    else:
        return False

def main():

    for number in range(1,maximum_number+1):
        if isPerfect(number):
            print("O numero " + str(number) + " é perfeito")
  
if __name__ == "__main__":
    main()