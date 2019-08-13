#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved

# Program: Male and Female Percentages
# Description: This program dispalyst the percentage of males and females in a
#              group/class.
# Status: Incomplete
# Date: 2019/08/13

# Get data
males = int(input('Enter the number of males: '))
females = int(input('Enter the number of females: '))

# Calculate data
total = (males + females)
male_perc = (males/total)
female_perc = (females/total)
male_standard_notation = (male_perc * 100)
female_standard_notation = (female_perc * 100)

# Display data
print('\nPercentages')
print('==============')
print('Males  : ', male_standard_notation, '%', sep='')
print('Females: ', female_standard_notation, '%', sep='')
