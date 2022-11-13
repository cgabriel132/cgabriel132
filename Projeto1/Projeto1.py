#!/usr/bin/python3

import argparse
import random
import string
from readchar import readkey
from colorama import Fore, Style
import time
from collections import namedtuple
from pprint import pprint

my_dict = {'accuracy': 0.0,
 'inputs': [],
 'number_of_hits': 0,
 'number_of_types': 0,
 'test_duration': 0,
 'test_end': None,
 'test_start': None,
 'type_average_duration': 0.0,
 'type_hit_average_duration': 0.0,
 'type_miss_average_duration': 0.0}

Input = namedtuple("Input", ["requested", "received", "duration"])

def main():

    parser = argparse.ArgumentParser(description="Typing Test help:")
    parser.add_argument('-utm', '--time_mode', action='store_true', help='Max number of secs for time mode')
    parser.add_argument('-mv', '--max_number', type=int, help='Maximum number of inputs for number of inputs mode')
    args = vars(parser.parse_args())
    print(args)

    if args['time_mode']:
        print('Using time mode. The test will run up to ' + str(args['max_number']) + ' seconds')
    else:
        print('Test will ask for ' + str(args['max_number']) + ' responses')
        max_chars(args['max_number'])

def max_chars(max_number):

    counter = 0

    while counter < max_number:
        
        i = time.localtime() # Time at the moment that we start the test
        inicio = time.mktime(i)

        c = random.choice(string.ascii_lowercase)  # random char 
        print("Type letter " + c)

        input_character = readkey()

        if input_character == c:
            print("You typed letter " + Fore.GREEN + input_character + Style.RESET_ALL)
        else:
            print("You typed letter " + Fore.RED + input_character + Style.RESET_ALL)

        f = time.localtime()  # Time at the moment that we finish the test
        fim = time.mktime(f)

        duration = (fim-inicio)

        counter += 1

        my_dict['inputs'].append(Input(c, input_character, duration))

    pprint(my_dict)

if __name__ == '__main__':
    main()