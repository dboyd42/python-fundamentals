#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved

# Program: Stock Transaction Program
# Description: This program processeses a specific stock transactions
# Status: Incomplete
# Date: 2019/08/13

# Declare variables
nShares = 2000
stock_cost_pShare = 40.00
broker_commission = 0.03

sold_shares = 2000
sold_cost_pShare = 42.75
#broker_commision = 0.03

# Calculate data
total_stock_cost = (nShares * stock_cost_pShare)
total_buying_comm = ( total_stock_cost * broker_commision)

# Display data
print('\nTotals')
print('===================')
print('Stock Purchase   : $', format(total_stock_cost, '.2f'))
print('Broker Commission: $', format(total_buying_comm, '.2f'))
print('Stock Sold Price : $', format('.2f'))
print('Broker Commission: $', format('.2f'))
print('Net Pay          : $', format('.2f'))
