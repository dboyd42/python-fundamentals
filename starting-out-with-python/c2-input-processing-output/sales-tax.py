#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved

# Program: Sales Tax
# Description: This program calculates the state and county tax from an inputted
#              purchase then displays the amount, taxes, and total of the sale.
# Status: Complete
# Date: 2019/08/13

# Declare variables
state_tax = 0.05
county_tax = 0.025

# Get amount of a purchase
purchase = float(input('Enter the amount of a purchase: $'))

# Calculate taxes and total
purchase_state_tax = (purchase * state_tax)
purchase_county_tax = (purchase * county_tax)
total_sales_tax = (purchase_county_tax + purchase_state_tax)
total = (purchase + total_sales_tax)

# Display totals
print('\nTotals')
print('=========================')
print('Purchase Amount: ', format(purchase, ',.2f'))
print('State Tax      : ', format(purchase_state_tax, ',.2f'))
print('Country Tax    : ', format(purchase_county_tax, ',.2f'))
print('Total Sales Tax: ', format(total_sales_tax, ',.2f'))
print('Total          : ', format(total, ',.2f'))
