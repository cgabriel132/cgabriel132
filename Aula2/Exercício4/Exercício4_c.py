#!/usr/bin/env python3

from readchar import readkey

def countNumbersUpTo(stop_char):
    
    keys = []
    total_numbers = 0
    total_others = 0
    
    while True:
        print('Enter a key')
        key = readkey()

        print('You pressed ' + key)

        if key == stop_char:
            break

        keys.append(key)

    print('User pressed ' + str(keys))

    keys_numbers = []
    keys_others = []

    for key in keys:
        if key.isnumeric():
            keys_numbers.append(key)
        else:
            keys_others.append(key)

    print('Keys numbers ' + str(keys_numbers))
    print('Keys others ' + str(keys_others))

    total_numbers = len(keys_numbers)
    total_others = len(keys_others)

    print('You entered ' + str(total_numbers) + ' numbers.')
    print('You entered ' + str(total_others) + ' others.')

def main():

    countNumbersUpTo('x')

if __name__ == '__main__':
    main()