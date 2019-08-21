#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved
# Program: Stadium Seating
# Description:
#     Calculates income generated from ticket sales
# Date: 2019/08/20
# Revised:
#     <revision date>

def main():

    # Declare variables
    # Seats [Type, Price, Sold, Income]
    seats = [ ["A", 20.00, 0, 0.00], ["B", 15.00, 0, 0.00], \
              ["C", 10.00, 0, 0.00] ]
    income = 0.00  # total income from ticket sales

    # Run program
    get_sales(seats)
    income = calc_sales(seats, income)
    print()
    display(seats, income)

# End Program

def get_sales(seats):

    # Declare local variables
    name  = 0  # seats index position for type name
    sold  = 2  # seats index position for tickets sold

    # Get tickets sold
    print('\nEnter the number of tickets sold')
    print('--------------------------------')
    for type in range(len(seats)):
        seats[type][sold] = int(input('Type ' + str(seats[type][name]) + ': '))

def calc_sales(seats, income):

    # Declare local variables
    price = 1  # seats index position for ticket price
    sold  = 2  # seats index position for tickets sold
    total = 3  # seats index position for type ticket's income

    for type in range(len(seats)):
        seats[type][total] = (seats[type][price] * seats[type][sold])
        income += seats[type][total]

    return income

def display(seats, income):

    # Declare local variables
    name  = 0  # seats index position for type name
    price = 1  # seats index position for ticket price
    sold  = 2  # seats index position for tickets sold
    total = 3  # seats index position for type ticket's income

    # Display totals
    print('Totals')
    print('======')
    for type in range(len(seats)):
        print('Type ', seats[type][name], ' Total: $', \
                format(seats[type][total], ',.2f'), sep='')
    print('--------------------------------')
    print('Total Income: $', format(income, ',.2f'), sep='')

# Call the ma(in function
main()
