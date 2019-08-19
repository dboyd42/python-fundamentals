#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved

# Program: Celsius to Fahrenheit Temperature Converter
# Description: This program converts Celsius temperatures to Fahrenheit
#              temperatures by asking for the Celsius temperature.
# Status: Complete
# Date: 2019/08/13

# Get data
celsius = float(input('Enter the temperature in Celsius: '))

# Calculate data
farenheit = ((9/5)*celsius + 32)

# Display data
print('Degrees in Farenheit is', format(farenheit, '.2f'))
