#Import library
from readchar import readkey
from colorama import Fore, Style
from collections import namedtuple
from pprint import pprint
from time import time, ctime 
from time import time
import random
import string
import argparse

StopEvent = True
ModeSelected = []

Input = namedtuple("Input", ["requested", "received", "duration"])

#Main
def main():

    parser = argparse.ArgumentParser(description="Typing Test help:")
    parser.add_argument('-utm', '--time_mode', type=int, help='Max number of secs for time mode')
    parser.add_argument('-mv', '--max_number', type=int, help='Maximum number of inputs for number of inputs mode')
    args = vars(parser.parse_args())
    print(args)
    if args['time_mode']:
        print('Using time mode. The test will run up to ' + str(args['time_mode']) + ' seconds')
        ModeSelected.append(2)
        ModeSelected.append(str(args['time_mode']))
        countNumbersUpTo(StopEvent)
    elif args['max_number']:
        print('Test will ask for ' + str(args['max_number']) + ' responses')
        ModeSelected.append(1)
        ModeSelected.append(str(args['max_number']))
        countNumbersUpTo(StopEvent)
    else:
        ModeSelected.append(0)
        ModeSelected.append(0)


def countNumbersUpTo(StopEvents):
    StopChar    = ' '   #Define Stop Char
    StartTest   = False #Start Test Memory
    ActiveMode  = 0     #Active Mode
    MaxLimit    = 0     #Define Maximum Limit
    keys        = []    #Array key Pressed
    KeysWanted  = []    #Array key Wanted
    InputResult = []    #Array Inputs
    Hits        = 0     #Number of Hits
    Acuracy     = 0.0   #Acuracy Result
    TestStart   = ''    #Date Start Test
    TestEnd     = ''    #Date End Test
    TestStartS  = 0     #Date Start Test in second
    TestEndS    = 0     #Date End Test in second
    TestDuration = ''   #Duration of Test
    ActualTimeS = 0     #Duration of Test 
    AverageTypeDurationArray = [] #Array With Times key Pressed
    AverageHitDurationArray  = [] #Array With Times Hit
    AverageMissDurationArray = [] #Array With Times Miss
    CalculateAverageTypeDuration = 0.0 #Memory to Calculate average type
    CalculateAverageHitDuration  = 0.0 #Memory to Calculate average Hit
    CalculateAverageMissDuration = 0.0 #Memory to Calculate average Miss
    AverageTypeDuration = 0.0   #Average Type Duration
    AverageHitDuration  = 0.0   #Average Hit Duration
    AverageMissDuration = 0.0   #Average Miss Duration
    LengthATD           = 0     #Lenght of Array Average Type Duration 
    LengthAHD           = 0     #Lenght of Array Average Hit Duration 
    LengthAMD           = 0     #Lenght of Array Average Miss Duration 
    CounterATD          = 0     #Counter for Array Average Type Duration 
    CounterAHD          = 0     #Counter for Array Average Hit Duration 
    CounterAMD          = 0     #Counter for Array Average Miss Duration 
    InputDuration       = 0     #Last Input Duration


    print("Press a key to start test")

    key = readkey()             #Validate Start Test
    if key != '':
        StartTest = True

    ActiveMode  = ModeSelected[0]       #Define Active Mode
    MaxLimit    = int(ModeSelected[1])  #Define Limit Max

    #Save Start Time 
    TestStart = ctime()
    TestStartS= time()
    AverageTypeDurationArray.append(TestStartS)
    AverageHitDurationArray.append(TestStartS)
    AverageMissDurationArray.append(TestStartS)

    while (StartTest and 
        ((ActiveMode == 1 and LengthATD < MaxLimit) or
        (ActiveMode == 2 and time() < TestStartS + MaxLimit ))): 

        KeyWanted = random.choice(string.ascii_lowercase) #chose New Letter
        print('Enter a key "' + KeyWanted + '"')   #Print New Letter
        key = readkey()

        if KeyWanted == key:
            print("You typed letter " + Fore.GREEN + key + Style.RESET_ALL)
        else:
            print("You typed letter " + Fore.RED + key + Style.RESET_ALL)

        if key == StopChar: #BreakPoint in case of space enterred
            StopEvents 
            break

        #Input Duration Calculator
        ActualTimeS = time()
        AverageTypeDurationArray.append(ActualTimeS)
        LengthATD = len(AverageTypeDurationArray)-1 
        InputDuration = AverageTypeDurationArray[LengthATD] - AverageTypeDurationArray[LengthATD - 1]

        #Verify Input
        if key == KeyWanted:
            Hits +=1
            AverageHitDurationArray.append(ActualTimeS)
            InputResult.append('Key Wanted : ' + str(KeyWanted) + ', Key pressed : '+ str(key) + ', Duration : '+ str(InputDuration) + ', Result : Correct')
        else:
            AverageMissDurationArray.append(ActualTimeS)
            InputResult.append('Key Wanted : ' + str(KeyWanted) + ', Key pressed : '+ str(key) + ', Duration : '+ str(InputDuration) + ', Result : Incorrect')


        keys.append(key)
        KeysWanted.append(KeyWanted)
        TestActualDuration = time() - TestStartS
    else:
        StopEvents
        key = ' '

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

    pprint(my_dict)


if __name__ == "__main__":
    main()