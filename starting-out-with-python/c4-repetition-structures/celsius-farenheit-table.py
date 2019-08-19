#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved
# Program: Celsius to Farenheit Table
# Description: Displays a table of the Celsius temps 0-20 and their Farenheit
#              equivalents.
# Status: Complete
# Date: 2019/08/19

# Declare variables
farenheit = 0.00
max_temp = 20

# Calculate & Display C-F table
print('Celsius | Ferenheit')
print('===================')
for celsius in range(max_temp+1):
    farenheit = (9/5)*celsius+32
    print(celsius, '\t| ', format(farenheit, '.2f'))
