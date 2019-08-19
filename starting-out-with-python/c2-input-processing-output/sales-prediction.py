#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved

# A company has determined that its annual profit ist typically 23 percent of
# total sales.  This program asks the user to enter the projected amount of
# total sales, and then displays the profit that will be made from that amount.

# Declare variables
annual_profit_perc = 0.23  # predicted annual profit percentage

# Get projected amount of total sales
total_sales = float(input('Enter the projected amount of total sales: $'))

# Calculate profit
gross_sales = (annual_profit_perc * total_sales)

# Display the predicted profit
print('Profit from total sales: $', format(gross_sales, '.2f'), sep='')
