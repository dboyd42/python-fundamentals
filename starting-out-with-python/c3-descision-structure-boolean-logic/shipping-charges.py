#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved
# Program: Shipping Charges
# Description: Gets package weight and displays shipping charges.
# Status: Complete
# Date: 2019/08/14

# Declare variables
valid = True

# Get package weight
usr_pkg_wt = float(input('Enter the weight of your package: '))

# Determine cost rate per pound
if usr_pkg_wt > 0 and usr_pkg_wt <= 2:
    rate = 1.50
elif usr_pkg_wt > 2 and usr_pkg_wt <= 6:
    rate = 3.00
elif usr_pkg_wt > 6 and usr_pkg_wt <= 10:
    rate = 4.00
elif usr_pkg_wt > 10:
    rate = 4.75
else:
    valid = False
    rate = 0.00

# Calculate shipping charges
shipping_chg = usr_pkg_wt * rate

# Display shipping charge
if valid:
    print('Total shipping charge: $', format(shipping_chg, ',.2f'))
else:
    print('Invalid weight')
