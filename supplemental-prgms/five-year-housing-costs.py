#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved
# Program: Five Year Housing Costs
# Description: Determines best valued housing by calculating housing costs
#              after a five-year period.
# Status: Complete
# Date: 2019/08/19

# Declare variables
best_index = 0
best_value = 0.00
time_period = 5
ann_fuel_cost = []
five_year_cost = []
init_cost = []
tax_rate = []

# Get user data
houses = int(input('Enter the number of houses to compare: '))

for i in range(houses):
    print('\nHouse #', i+1, sep='')
    print('--------')
    init_cost.append(float(input('Initial Cost' + '\t: $')))
    ann_fuel_cost.append(float(input('Annual Fuel Cost' + ': $')))
    tax_rate.append(float(input('Tax Rate' + '\t: ')))

# Calculate the housing costs
for i in range(houses):
    year_sum = (init_cost[i] + ann_fuel_cost[i])

    # Loop through the years for running annual totals
    for year in range(time_period):
        year_rate = (year_sum * tax_rate[i])
        year_total = (year_sum + year_rate)
        year_sum = (year_total + ann_fuel_cost[i])

    # Append the 5 year total cost
    five_year_cost.append(year_total)

# Determine which house is cheaper
best_value = five_year_cost[0]
for i in range(houses):
    if (best_value > five_year_cost[i]):
        best_index = i
        best_value = five_year_cost[i]

# Display the house cost after five years
print()
print('Total Cost After a Five-Year Period')
print('===================================')
for i in range(houses):
    print('House #', str(i+1), ': $', format(five_year_cost[i], ',.2f'), \
            sep='')

# Display house of best value
print()
print('Best Valued House After a Five-Year Period')
print('==========================================')
print('House #', best_index+1, ' at $', format(best_value, ',.2f'), sep='')
