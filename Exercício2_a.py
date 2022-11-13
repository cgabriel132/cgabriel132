maximum_number = 10


def isPrime(value):

    for number in range(2,value):
        remainder = value % number
        print(str(value) + '/' + str(number) + '=' + str(remainder))
        if remainder == 0:
            return False
    return True
    

def main():
    print("Starting to compute prime numbers up to " + str(maximum_number))

    for number in range(1, maximum_number+1):
        if isPrime(number):
            print('Number ' + str(number) + ' is prime.')
        else:
            print('Number ' + str(number) + ' is not prime.')

if __name__ == "__main__":
    main()