#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved
# Program: Population
# Description: Predicts the approximate size of a population of organisms.
# Status: Complete
# Date: 2019/08/19

# Declare variables
rate = 0.00
init_organisms = 0
nDays = 0
population = 0.00

# Get organism-population numbers
init_organisms = int(input('Starting number of organisms: '))
rate = float(input('Average daily increase: '))
nDays = int(input('Number of days to multiply: '))

# Initialize data
rate /= 100
population = init_organisms

# Calculate & display population growth
print()
print('Day Approximate\t| Population')
print('=================================')
for day in range(1, nDays+1):
    print(day, '\t\t| ', population)
    population += (population*rate)
