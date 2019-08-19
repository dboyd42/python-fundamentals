#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved
# Program: Pennies for Pay
# Description: Calculates amount of money over a period of time if salary is
#              initiates at one penny per day then doubles each day.
# Status: Complete
# Date: 2019/08/19

# Declare variables
days = 0
daily_pay = 0.01  # initial pay
salary = 0.00

# Get number of days
days = int(input('Enter the number of days: '))

# Calculate & daily salary
for i in range(1, days+1):
    if (i > 1):
        daily_pay *= 2
        salary += daily_pay
    print('Day', i, ' = $', format(daily_pay, ',.2f'), sep='')

# Display ending salary
print('\nTotal salary is $', format(salary, ',.2f'), sep='')
