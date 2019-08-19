#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved
# Program: Sum of Numbers
# Description: Sums a series of positive numbers.
# Status: Complete
# Date: 2019/08/19

# Declare variables
number = 0.00
summation = 0.00
zero = 0

# Get and sum numbers
print('\nEnter a NEGATIVE NUMBER to quit the series')
print('------------------------------------------')
while (number >= zero):
    summation += number
    number = float(input('Enter a positive number: '))

# Display
print('The sum is: ', summation)
