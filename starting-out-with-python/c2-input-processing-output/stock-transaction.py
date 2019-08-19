#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved

# Program: Stock Transaction Program
# Description: This program processeses a specific stock transactions
# Status: Complete
# Date: 2019/08/13

# Declare variables
nShares = 2000
stock_cost_pShare = 40.00
broker_commission = 0.03
sold_shares = 2000
sold_cost_pShare = 42.75

# Calculate data
# Buying totals
total_stock_cost = (nShares * stock_cost_pShare)
commBuyCost = (total_stock_cost * broker_commission)
total_buying_cost = (total_stock_cost + commBuyCost)

# Selling totals
total_sold_price = (nShares * sold_cost_pShare)
commSellCost = (total_sold_price * broker_commission)
total_sell_cost = (total_stock_cost - commSellCost)

# Decide if profit or loss
if (total_sell_cost > total_buying_cost):
    margin = "profit"
else:
    margin = "loss"

# Display data
print('\nTotals')
print('===================')
print('Stock Purchase     : $', format(total_stock_cost, '.2f'))
print('Broker Commission  : $', format(commBuyCost, '.2f'))
print('                     -----------')
print('Total Purchase     : $', format(total_buying_cost, '.2f'))
print()
print('Stock Selling Price: $', format(total_sold_price, '.2f'))
print('Broker Commission  : $', format(commSellCost, '.2f'))
print('                     -----------')
print('Total Selling Price: $', format(total_sell_cost, '.2f'))
print()
print('Transaction made a', margin, 'in sells.')
