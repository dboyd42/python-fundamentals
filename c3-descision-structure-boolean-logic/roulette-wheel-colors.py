#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved

# Program: Roulette Wheel Colors
# Description: Displays the pocket color based off the roulette wheel number.
# Status: Complete
# Date: 2019/08/14

# Declare variables
valid = True

# Get user number
num = int(input('Enter a pocket number (0-36): '))

# Determine coland
if num == 0:
    pocket = "green"
elif num >= 1 and num <= 10:
    if num%2==0:
        pocket = "black"
    else:
        pocket = "red"
elif num >= 11 and num <= 18:
    if num%2==0:
        pocket = "red"
    else:
        pocket = "black"
elif num >= 19 and num <= 28:
    if num%2==0:
        pocket = "black"
    else:
        pocket = "red"
elif num >= 29 and num <= 36:
    if num%2==0:
        pocket = "red"
    else:
        pocket = "black"
else:
    valid = False
    err_message = "INVALID NUMBER!"

# Display pocket color
if valid:
    print('Pocket color is', pocket)
else:
    print(err_message)
