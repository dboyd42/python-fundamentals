#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved
# Program: Movie Theater Revenue
# Description: Calculates a theater's gross and net box office profit for a
#              night.
# Status: Complete
# Date: 2019/08/19

# Declare variables
movie_name = ""
adult_tkt_cost = 6.00
adult_tkt_gross = 0.00
adult_tkt_sold = 0
child_tkt_cost = 3.00
child_tkt_gross = 0.00
child_tkt_sold = 0
expenses = 0.20  # percentage
gross = 0.00
net = 0.00

# Get movie data
movie_name = input('Movie Name: ')
adult_tkt_sold = int(input('How many adult tickets were sold? '))
child_tkt_sold = int(input('How many child tickets were sold? '))

# Calculate revenue
adult_tkt_gross = (adult_tkt_sold * adult_tkt_cost)
child_tkt_gross = (child_tkt_sold * child_tkt_cost)
gross = (adult_tkt_gross + child_tkt_gross)
net = (gross * expenses)
expenses = (gross - net)

# Display sales and revenue
print()
print('Movie Name\t\t"', movie_name, '"', sep='')
print('Adult Tickets Sold:\t', adult_tkt_sold)
print('Child Tickets Sold:\t', child_tkt_sold)
print('Gross Box Office Profit: $', format(gross, '8,.2f'), sep='')
print('Net Box Office Profit:\t $', format(net, '8,.2f'), sep='')
print('Amount Paid to Movie Co: $', format(expenses, '8,.2f'), sep='')
