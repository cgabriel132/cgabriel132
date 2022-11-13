import argparse
import random
import string
from readchar import readkey
from pprint import pprint
from time import time, ctime 
from colorama import Fore, Style
from collections import namedtuple

Input = namedtuple("Input", ["requested", "received", "duration"])

def main():
    
    parser = argparse.ArgumentParser(description="Typing Test help:")
    parser.add_argument('-utm', '--time_mode', type=int, help='Max number of secs for time mode')
    parser.add_argument('-mv', '--max_number', type=int, help='Maximum number of inputs for number of inputs mode')
    args = vars(parser.parse_args())

    if args['time_mode']:
        print('Using time mode. The test will run up to ' + str(args['time_mode']) + ' seconds')
        timemode(args['time_mode'])
    else:
        print('Test will ask for ' + str(args['max_number']) + ' responses')
        max_chars(args['max_number'])

def max_chars(max_number):

    # 1. Read all the inputs and put them in the keys list
    keys        = []
    KeysWanted  = []
    InputResult = []
    Hits        = 0
    Acuracy     = 0.0
    TestStart   = ''
    TestEnd     = ''
    TestStartS  = 0
    TestEndS    = 0
    TestDuration = ''
    ActualTimeS = 0
    AverageTypeDurationArray = []
    AverageHitDurationArray  = []
    AverageMissDurationArray = []
    CalculateAverageTypeDuration = 0.0
    CalculateAverageHitDuration  = 0.0
    CalculateAverageMissDuration = 0.0
    AverageTypeDuration = 0.0
    AverageHitDuration  = 0.0
    AverageMissDuration = 0.0
    LengthATD           = 0
    LengthAHD           = 0
    LengthAMD           = 0
    CounterATD          = 0
    CounterAHD          = 0
    CounterAMD          = 0
    InputDuration       = 0

    #Save Start Time
    TestStart = ctime()
    TestStartS= time()
    AverageTypeDurationArray.append(TestStartS)
    AverageHitDurationArray.append(TestStartS)
    AverageMissDurationArray.append(TestStartS)

    counter = 0

    while counter < max_number:

        c = random.choice(string.ascii_lowercase)  # random char 
        print("Type letter " + c)

        input_character = readkey()

        if input_character == c:
            print("You typed letter " + Fore.GREEN + input_character + Style.RESET_ALL)
        else:
            print("You typed letter " + Fore.RED + input_character + Style.RESET_ALL)

        counter += 1

        #Input Duration Calculator
        ActualTimeS = time()
        AverageTypeDurationArray.append(ActualTimeS)
        LengthATD = len(AverageTypeDurationArray)-1 
        InputDuration = AverageTypeDurationArray[LengthATD] - AverageTypeDurationArray[LengthATD - 1]

        #Verify Input
        if input_character == c:
            Hits +=1
            AverageHitDurationArray.append(ActualTimeS)
            InputResult.append('Key Wanted : ' + str(c) + ', Key pressed : '+ str(input_character) + ', Duration : '+ str(InputDuration) + ', Result : Correct')
        else:
            AverageMissDurationArray.append(ActualTimeS)
            InputResult.append('Key Wanted : ' + str(c) + ', Key pressed : '+ str(input_character) + ', Duration : '+ str(InputDuration) + ', Result : Incorrect')


        keys.append(input_character)
        KeysWanted.append(c)
        TestActualDuration = time() - TestStartS


    #Save End Time
    TestEnd = ctime()
    TestEndS = time()
    TestDuration = TestEndS - TestStartS

    #Calculate Number of Chars Entries
    total_chars = len(keys)

    #Acuracy calculator
    if Hits > 0:
        Acuracy = Hits/total_chars
    else:
        Acuracy = 0.0

    #Average Type Duration
    LengthATD = len(AverageTypeDurationArray)
    for lengthATD in AverageTypeDurationArray:
        #verify if at least 1 letter is pressed
        if CounterATD >= 1:
            CalculateAverageTypeDuration = AverageTypeDurationArray[CounterATD] - AverageTypeDurationArray[CounterATD-1]
        else:
            CalculateAverageTypeDuration = 0
        AverageTypeDuration = AverageTypeDuration + CalculateAverageTypeDuration
        CounterATD += 1
    #Verify if have more than 1 input    
    if LengthATD >= 2 : 
        AverageTypeDuration = AverageTypeDuration / LengthATD

    #Average Hit Duration
    LengthAHD = len(AverageHitDurationArray)
    for lengthAHD in AverageHitDurationArray:
        if CounterAHD >= 1:
            CalculateAverageHitDuration = AverageTypeDurationArray[CounterAHD] - AverageHitDurationArray[CounterAHD-1]
        else:
            CalculateAverageHitDuration = 0
        AverageHitDuration = AverageHitDuration + CalculateAverageHitDuration
        CounterAHD += 1
    #Verify if have more than 1 Hit   
    if LengthAHD >= 2 : 
        AverageHitDuration = AverageHitDuration / LengthAHD

    #Average Miss Duration
    LengthAMD = len(AverageMissDurationArray)
    for lengthAMD in AverageMissDurationArray:
        if CounterAMD >=1 :
            CalculateAverageMissDuration = AverageMissDurationArray[CounterAMD] - AverageMissDurationArray[CounterAMD-1]
        else:
            CalculateAverageMissDuration = 0
        AverageMissDuration = AverageMissDuration + CalculateAverageMissDuration
        CounterAMD += 1
    #Verify if have more than 1 Miss
    if LengthAMD >= 2 : 
        AverageMissDuration = AverageMissDuration / LengthAMD

    # Create the dictionary 
    my_dict = {"Acuracy": Acuracy,
                    "Inputs": InputResult,
                    "NumberOfHits" : Hits,
                    "NumberOfTypes":total_chars, 
                    "TestDuration":TestDuration,
                    "TestStart":TestStart,
                    "TestEnd": TestEnd,
                    "TypeAverageDuration": AverageTypeDuration,
                    "TypeHitAverageDuration": AverageHitDuration,
                    "TypeMissAverageDuration": AverageMissDuration}

    my_dict['Inputs'].append(Input(c, input_character, InputDuration))

    pprint(my_dict)

def timemode(max_time):
    
    # 1. Read all the inputs and put them in the keys list
    keys        = []
    KeysWanted  = []
    InputResult = []
    Hits        = 0
    Acuracy     = 0.0
    TestStart   = ''
    TestEnd     = ''
    TestStartS  = 0
    TestEndS    = 0
    TestDuration = ''
    ActualTimeS = 0
    AverageTypeDurationArray = []
    AverageHitDurationArray  = []
    AverageMissDurationArray = []
    CalculateAverageTypeDuration = 0.0
    CalculateAverageHitDuration  = 0.0
    CalculateAverageMissDuration = 0.0
    AverageTypeDuration = 0.0
    AverageHitDuration  = 0.0
    AverageMissDuration = 0.0
    LengthATD           = 0
    LengthAHD           = 0
    LengthAMD           = 0
    CounterATD          = 0
    CounterAHD          = 0
    CounterAMD          = 0
    InputDuration       = 0

    start_timer = time()

    #Save Start Time
    TestStart = ctime()
    TestStartS= time()
    AverageTypeDurationArray.append(TestStartS)
    AverageHitDurationArray.append(TestStartS)
    AverageMissDurationArray.append(TestStartS)

    while time() < start_timer + int(max_time):
        chars = random.choice(string.ascii_lowercase)  # random char 
        print("Type letter " + chars)
        input_chars = readkey()
        if input_chars == chars:
            print("You typed letter " + Fore.GREEN + input_chars + Style.RESET_ALL)
        else:
            print("You typed letter " + Fore.RED + input_chars + Style.RESET_ALL)
        
        #Input Duration Calculator
        ActualTimeS = time()
        AverageTypeDurationArray.append(ActualTimeS)
        LengthATD = len(AverageTypeDurationArray)-1 
        InputDuration = AverageTypeDurationArray[LengthATD] - AverageTypeDurationArray[LengthATD - 1]

        #Verify Input
        if input_chars == chars:
            Hits +=1
            AverageHitDurationArray.append(ActualTimeS)
            InputResult.append('Key Wanted : ' + str(chars) + ', Key pressed : '+ str(input_chars) + ', Duration : '+ str(InputDuration) + ', Result : Correct')
        else:
            AverageMissDurationArray.append(ActualTimeS)
            InputResult.append('Key Wanted : ' + str(chars) + ', Key pressed : '+ str(input_chars) + ', Duration : '+ str(InputDuration) + ', Result : Incorrect')


        keys.append(input_chars)
        KeysWanted.append(chars)
        TestActualDuration = time() - TestStartS

    #Save End Time
    TestEnd = ctime()
    TestEndS = time()
    TestDuration = TestEndS - TestStartS

    #Calculate Number of Chars Entries
    total_chars = len(keys)

    #Acuracy calculator
    if Hits > 0:
        Acuracy = Hits/total_chars
    else:
        Acuracy = 0.0

    #Average Type Duration
    LengthATD = len(AverageTypeDurationArray)
    for lengthATD in AverageTypeDurationArray:
        #verify if at least 1 letter is pressed
        if CounterATD >= 1:
            CalculateAverageTypeDuration = AverageTypeDurationArray[CounterATD] - AverageTypeDurationArray[CounterATD-1]
        else:
            CalculateAverageTypeDuration = 0
        AverageTypeDuration = AverageTypeDuration + CalculateAverageTypeDuration
        CounterATD += 1
    #Verify if have more than 1 input    
    if LengthATD >= 2 : 
        AverageTypeDuration = AverageTypeDuration / LengthATD

    #Average Hit Duration
    LengthAHD = len(AverageHitDurationArray)
    for lengthAHD in AverageHitDurationArray:
        if CounterAHD >= 1:
            CalculateAverageHitDuration = AverageTypeDurationArray[CounterAHD] - AverageHitDurationArray[CounterAHD-1]
        else:
            CalculateAverageHitDuration = 0
        AverageHitDuration = AverageHitDuration + CalculateAverageHitDuration
        CounterAHD += 1
    #Verify if have more than 1 Hit   
    if LengthAHD >= 2 : 
        AverageHitDuration = AverageHitDuration / LengthAHD

    #Average Miss Duration
    LengthAMD = len(AverageMissDurationArray)
    for lengthAMD in AverageMissDurationArray:
        if CounterAMD >=1 :
            CalculateAverageMissDuration = AverageMissDurationArray[CounterAMD] - AverageMissDurationArray[CounterAMD-1]
        else:
            CalculateAverageMissDuration = 0
        AverageMissDuration = AverageMissDuration + CalculateAverageMissDuration
        CounterAMD += 1
    #Verify if have more than 1 Miss
    if LengthAMD >= 2 : 
        AverageMissDuration = AverageMissDuration / LengthAMD
    
    # Create the dictionary 
    my_dict = {"Acuracy": Acuracy,
                    "Inputs": InputResult,
                    "NumberOfHits" : Hits,
                    "NumberOfTypes":total_chars, 
                    "TestDuration":TestDuration,
                    "TestStart":TestStart,
                    "TestEnd": TestEnd,
                    "TypeAverageDuration": AverageTypeDuration,
                    "TypeHitAverageDuration": AverageHitDuration,
                    "TypeMissAverageDuration": AverageMissDuration}

    my_dict['Inputs'].append(Input(chars, input_chars, InputDuration))

    pprint(my_dict)

if __name__ == "__main__":
    main()