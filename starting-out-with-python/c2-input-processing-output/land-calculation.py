#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved

# This program asks the user to enter the total square feet in a tact of land
# and calculates the numbe of acres in the tract.

# Declare variables
ft_per_Acre = 43560

# Get total square feet in tract of land
land_feet = float(input('Enter the total square feet in tract of land: '))

# Calculate the number of acres in the tract
users_acres = (land_feet / ft_per_Acre)

# Display user's total acres
print('Total acres in land tract = ', format(users_acres, ',.2f'))
