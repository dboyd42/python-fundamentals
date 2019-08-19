#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved
# Program: Tuition Increase
# Description: Calculates the projected semester tuition for the next 5 years
# Status: Complete
# Date: 2019/08/19

# Declare variables
init_cost = 8000
rate = 0.03
time_period = 5
years_tax = 0.00
years_tuition = 0.00

# Initialize variables
years_tax = (init_cost * rate)
years_tuition = (init_cost + years_tax)

# Calculate and display projected tuition
print('Year\t| Tuition Cost')
print('======================')
for year in range(1, time_period+1):
    print(year, '\t| $', format(years_tuition, '6,.2f'), sep='')
    years_tax = (years_tuition * rate)
    years_tuition += years_tax
