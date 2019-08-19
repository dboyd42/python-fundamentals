#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved

# Program: Roman Numerals
# Description: Converts Arabic Numbers to Roman Numberals
# Status: Complete
# Date: 2019/08/13

# Declare variables
print('This program converts a number within the range of 1 through 10 to ' \
        'Roman Numberals')

# Get data
userNum = input('Enter an integer: ')

# Determine Roman Numberal
if userNum == '1':
    romNum = 'I'
elif userNum == '2':
    romNum = 'II'
elif userNum == '3':
    romNum = 'III'
elif userNum == '4':
    romNum = 'IV'
elif userNum == '5':
    romNum = 'V'
elif userNum == '6':
    romNum = 'VI'
elif userNum == '7':
    romNum = 'VII'
elif userNum == '8':
    romNum = 'VIII'
elif userNum == '9':
    romNum = 'IX'
elif userNum == '10':
    romNum = 'X'
else:
    romNum = 'Invalid Entry'

# Display Roman Numeral
print(romNum)
