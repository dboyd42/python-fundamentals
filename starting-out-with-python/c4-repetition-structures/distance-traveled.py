#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved
# Program: Distance Traveled
# Description: Displays the distance a vehicle has traveled in a time period.
# Status: Complete
# Date: 2019/08/16

# Declare variables
speed = 0.00
time = 0

# Get speed and hours
speed = float(input('What is the speed of the vehicle in mph? '))
time = int(input('How many hours has it traveled? '))

# Calculate & display distance
print('Hour\tDistance Traveled')
print('-------------------------')
for hour in range(1, time+1):
    distance = int(hour * speed)
    print(hour, '\t\t', distance)

