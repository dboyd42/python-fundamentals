#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved
# Program: Budget Analysis
# Description: Budgets a user-defined amount and gets expenses to determine if
#              user is over/under budget.
# Status: InComplete
# Date: 2019/08/14

# Declare variables
budget = float(input('Enter the amount for your month\'s budget: $'))
expenses = 0.00
choice = 'y'

# Get expenses
while (choice == 'y') or (choice == 'yes'):
    nTransactions = int(input('Enter the number of transactions ' \
                    'for the month: '))
    print("Enter '0' to quit")
    for x in range(nTransactions):
        temp = float(input('Enter expense #' + str(x+1) + ': $'))
        if (temp == 0):
            break
        else:
            expenses += temp
    choice = input('Enter another transaction? [y/n]: ').lower()

# Calculate over/under budget
if (expenses > budget):
    statement = "over budget"
elif (expenses < budget):
    statement = "under budget"
else:
    statement = "break even"

# Display
print('=====================================')
print('Your expenses are', statement)
print('=====================================')
