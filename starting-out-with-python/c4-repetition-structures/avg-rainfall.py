#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved
# Program: Average Rainfall
# Description: Calculates average rainfall over a period of years.
# Status: Complete
# Date: 2019/08/19

# Declare variables
nMonths = 12
nYears = 0
rainfall = 0.00       # in inches
total_rainfall = 0.00 # in inches

# Get rainfall data
nYears = int(input('Enter the number of years: '))

print('\nEnter the Rainfall (inches)')
print('===========================')
for year in range(nYears):
    print(' YEAR', year+1, '| ')
    for data in range(nMonths):
        total_rainfall += float(input('\t| Month ' + str(data+1) + ': '))
print('============================')

# Calculate average rainfall
total_nMonths = (nYears * nMonths)
avg_rainfall = (total_rainfall / total_nMonths)

# Display totals
print('\nTotals')
print('======')
print('Months  :', total_nMonths)
print('Rainfall:', format(total_rainfall, ',.2f'), 'inches')
print('\nAverages')
print('========')
print('Rainfall:', format(avg_rainfall, ',.2f'), 'inches')
