#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved

# Program: Money Counting Game
# Description: A change-counting game that gets the user to enter the number of
#              coins required to make exactly one dollar.
# Status: Complete
# Date: 2019/08/14

# Display Game Instructions
print('\nMoney Counting Game')
print('\nEnter the number of pennies, nickels, dimes, and quarters.  If the' \
      'total value of the coins entered is equal to $1, YOU WIN!!!\n')

# Get data
pennies = int(input('Enter the number of pennies : '))
nickels = int(input('Enter the number of nickels : '))
dimes = int(input('Enter the number of dimes   : '))
quarters = int(input('Enter the number of quarters: '))

# Calculate totals
total_pennies = pennies
total_nickels = 5 * nickels
total_dimes = 10 * dimes
total_quarters = 25 * quarters
total_change = total_pennies + total_nickels + total_dimes + total_quarters

# Determine amount to one dollar
if total_change == 100:
    message = "You Win!"
elif total_change > 100:
    message = "You entered an amount entered greater than one dollar!"
elif total_change < 100:
    message = "You entered an amount entered less than one dollar!"

# Display results
print()
print(message)
