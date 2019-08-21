#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved
# Program: Stadium Seating
# Description:
#     Calculates income generated from ticket sales
# Date: 2019/08/20
# Revised:
#     <revision date>

# Declare global variables
NAME  = 0  # seats index position for type NAME
PRICE = 1  # seats index position for ticket PRICE
SOLD  = 2  # seats index position for tickets SOLD
TOTAL = 3  # seats index position for type ticket's income

def main():

    # Declare variables
    # Seats [Type, PRICE, SOLD, TOTAL]
    seats = [ ["A", 20.00, 0, 0.00], ["B", 15.00, 0, 0.00], \
              ["C", 10.00, 0, 0.00] ]
    income = 0.00  # TOTAL income from ticket sales

    # Run program
    get_sales(seats)
    income = calc_sales(seats, income)
    print()
    display(seats, income)

# End Program

def get_sales(seats):

    # Get tickets SOLD
    print('\nEnter the number of tickets SOLD')
    print('--------------------------------')
    for type in range(len(seats)):
        seats[type][SOLD] = int(input('Class ' + str(seats[type][NAME]) + ': '))

def calc_sales(seats, income):

    # Calculate ticket sale & accumulate income
    for type in range(len(seats)):
        seats[type][TOTAL] = (seats[type][PRICE] * seats[type][SOLD])
        income += seats[type][TOTAL]

    return income

def display(seats, income):

    # Display TOTALs
    print('Totals')
    print('==============')
    for type in range(len(seats)):
        print('Class ', seats[type][NAME], ' Total: $', \
                format(seats[type][TOTAL], ',.2f'), sep='')
    print('--------------------------------')
    print('Total Income:  $', format(income, ',.2f'), sep='')

# Call the main function
main()
