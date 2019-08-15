#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved
# Program: Calories Burned
# Description: Displays calories burned at a rate of 4.2 calories in 5 min
#              intervals.
# Status: Complete
# Date: 2019/08/14

# Declare variables
rate = 4.2

# Run through intervals & display cals burned
for x in range(10, 35, 5):
    kcals_burn = int(x*rate)
    print('Calories burned in', x, 'is', kcals_burn, 'kcals')
