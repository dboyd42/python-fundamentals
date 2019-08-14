#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved

# Program: Magic Dates
# Description: Determines if month times day is equal to its year.
# Status: Complete
# Date: 2019/08/13

# Get date in numberic format
print('Enter the following date in a two digit format')
month = int(input('Enter month: '))
day = int(input('Enter day: '))
year = int(input('Enter year: '))

# Determine if magic date
if (month * day == year):
    magic_date = True
    message = 'a magic date'
else:
    magic_date = False
    message = 'nothing special'

# Display data
print('This date is', message)
