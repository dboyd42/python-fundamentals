#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved

# Program: Color Mixer
# Description: Processes primary colors to secondary colors.
# Status: Complete
# Date: 2019/08/13

# Declare variables

# Get user colors
print('Primary colors choices: "red", "blue", "yellow"')
prim1 = input('Enter first primary color: ')
prim2 = input('Enter second primary color: ')

# Determine colors
if prim1 == "red" and prim2 == "blue":
    mixed_color = "purple"
elif prim1 == "blue" and prim2 == "red":
    mixed_color = "purple"
elif prim1 == "red" and prim2 == "yellow":
    mixed_color = "orange"
elif prim1 == "yellow" and prim2 == "red":
    mixed_color = "orange"
elif prim1 == "yellow" and prim2 == "blue":
    mixed_color = "green"
elif prim1 == "blue" and prim2 == "yellow":
    mixed_color = "green"
elif prim1 == prim2:
    mixed_color = prim1
else:
    mixed_color = "INVALID --NOT FROM PRIMARY COLOR CHOICES"

# Display data
print('Your mixed color is', mixed_color)
