#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved

# Program: Day of the Week
# Description: Displays corresponding number to day of the week.
# Status: Complete
# Date: 2019/08/13

# Get data
day = input('Enter number for the day of the week: ')

# Calculate & Display data
if day == '1':
    print('Monday')
elif day == '2':
    print('Tuesday')
elif day == '3':
    print('Wednesday')
elif day == '4':
    print('Thursday')
elif day == '5':
    print('Friday')
elif day == '6':
    print('Saturday')
elif day == '7':
    print('Sunday')
else:
    print('Invalid Entry')
