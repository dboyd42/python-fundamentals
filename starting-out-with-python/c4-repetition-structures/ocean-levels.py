#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved
# Program: Ocean Levels
# Description: Displays the rising ocean levels at a rate of 1.6 mm per year.
# Status: Complete
# Date: 2019/08/19

# Declare variables
nYears = 25
rising_rate = 1.6  # millimeters
total_level = 0.00

# Calculate and display the levels each year
print('Year\t| Ocean Level (mm)')
print('==========================')
for year in range(nYears+1):
    total_level = (rising_rate * year)
    print(year, '\t| ', format(total_level, '.2f'))

# Display totals
print('\nTotal ocean level after', nYears, 'is', format(total_level, ',.2f'), \
        'mm')
