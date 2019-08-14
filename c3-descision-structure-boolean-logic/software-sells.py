#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved
# Program: Software Sales
# Description: Displays total discount and purchase amounts.
# Status: Complete
# Date: 2019/08/14

# Declare variables
product = 99.00  # in U.S. dollars

# Get number of packages ordered
pkgs = int(input('Enter the number of packages purchased: '))

# Determine discount (if any)
if pkgs >= 10 and pkgs <= 19:
    discount_perc = 0.10
elif pkgs >= 20 and pkgs <= 49:
    discount_perc = 0.20
elif pkgs >= 50 and pkgs <= 99:
    discount_perc = 0.30
elif pkgs >= 100:
    discount_perc = 0.40
else:
    discount_perc = 0.00

# Calculate total with discount
price_wo_discount = product * pkgs
discount_amt = price_wo_discount * discount_perc
price_with_discount = price_wo_discount - discount_amt

# Display amounts
print('\nTotals')
print('==============================')
print('Discount Total     : $', format(discount_amt, ',.2f'), sep='')
print('Total with Discount: $', format(price_with_discount, ',.2f'), sep='')
print('==============================')
