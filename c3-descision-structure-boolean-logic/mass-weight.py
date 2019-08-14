#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved

# Program: Mass and Weight
# Description: Calculates an object's weight in netowns based of the object's
#              mass in kilograms.
# Status: Complete
# Date: 2019/08/13

# Get object's mass
mass = float(input('Enter the object\'s mass in kilograms: '))

# Calculate weight
weight = (mass * 9.8)
if weight > 500:
    limitation = True
    message = "too heavy"
elif weight < 100:
    limitation = True
    message = "too light"
else:
    limitation = False

# Display data
if limitation == True:
    print('The object is', message)
else:
    print('Weight =', weight, 'kilograms')
