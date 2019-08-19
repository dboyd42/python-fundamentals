#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved

# Program: Tip, Tax, and Total
# Description: This program calculates the total amount of a meal purchased at
#              a restaurant.
# Status: Complete
# Date: 2019/08/13

# Declare Variables
tip = 0.18
sales_tax = 0.07

# Get food charge
food_charge = float(input('Enter charge for food: $'))

# Calculate tip, tax, and total
meal_tip = (food_charge * tip)
meal_tax = (food_charge * sales_tax)
total = (food_charge + meal_tip + meal_tax)

# Dfood_chargeisplay amounts
print('\nTotals')
print('===================')
print('Food Charge: $', format(food_charge, ',.2f'), sep='')
print('Meal Tip   : $', format(meal_tip, ',.2f'), sep='')
print('Meal Tax   : $', format(meal_tax, ',.2f'), sep='')
print('Total      : $', format(total, ',.2f'), sep='')
