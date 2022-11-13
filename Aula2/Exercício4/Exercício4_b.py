#!/usr/bin/env python3

from readchar import readkey

def readAllUpTo(stop_char):

    while True:
        print('Enter a key')
        key = readkey()

        print('You pressed ' + key)

        if key == stop_char:
            break

def printAllPreviousChars():

    stop_character = readkey()
    stop_number = ord(stop_character)

    print('Printing all chars up to ' + stop_character)

    characters = []
    for number in range(32, stop_number):
        character = chr(number)
        characters.append(character)

    print(characters)

def main():

    readAllUpTo('x')

if __name__ == '__main__':
    main()