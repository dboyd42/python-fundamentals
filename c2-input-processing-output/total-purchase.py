#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved

# This program asks for the price of each item, and then displays the subtotal
# of the sale, the amount of sales tax, and the total.

# Declare variables
sales_tax = 0.07

# Get the price of each item
item1 = float(input('Enter the price for item 1: $'))
item2 = float(input('Enter the price for item 2: $'))
item3 = float(input('Enter the price for item 3: $'))
item4 = float(input('Enter the price for item 4: $'))

# Calculate subtotal, sales tax total, and total
subtotal = (item1 + item2 + item3 + item4)
total_sales_tax = (subtotal * sales_tax)
total = (subtotal + total_sales_tax)

# Dispay the totals
print('\nSubtotal = $', format(subtotal, ',.2f'), sep='')
print('Amount of Sales Tax = $', format(total_sales_tax, ',.2f'), sep='')
print('Total = $', format(total, ',.2f'), sep='')
