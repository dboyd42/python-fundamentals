#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved
# Program: Sales Tax Program Refractored
# Description: This program calculates the state and county tax from an
#              inputted purchase then displays the amount, taxes, and total of
#              the sale.
# Notes: This program is from C2: 'sales-tax.py' and is redesigned for
#        functions.
# Status: Complete
# Date: 2019/08/19

###################
### Global Vars ###
###################
STATE_TAX = 0.05
COUNTY_TAX = 0.025

############
### main ###
############
def main():
    purchase = get_amt()
    # Declare & initiate variables
    # &&
    # calculate taxes
    '''
    Yes, I know this is bad programming, but I wanted to know if I could do it
                              --and YES, I can
    '''
    purchase_state_tax, purchase_county_tax, total_sales_tax, total \
        = calculate(purchase)
    # Display totals
    display(purchase, purchase_state_tax, purchase_county_tax, \
            total_sales_tax, total)

##################
### get amount ###
##################
def get_amt():
    # Get amount of a purchase
    return float(input('Enter the amount of a purchase: $'))

#################
### calculate ###
#################
def calculate(purchase):
    # Calculate taxes and total
    purchase_state_tax = (purchase * STATE_TAX)
    purchase_county_tax = (purchase * COUNTY_TAX)
    total_sales_tax = (purchase_county_tax + purchase_state_tax)
    total = (purchase + total_sales_tax)
    return purchase_state_tax, purchase_county_tax, total_sales_tax, total

###############
### display ###
###############
def display(purchase, purchase_state_tax, purchase_county_tax, \
            total_sales_tax, total):
    # Display totals
    print('\nTotals')
    print('=========================')
    print('Purchase Amount: $', format(purchase, '6,.2f'), sep='')
    print('State Tax      : $', format(purchase_state_tax, '6,.2f'), sep='')
    print('Country Tax    : $', format(purchase_county_tax, '6,.2f'), sep='')
    print('Total Sales Tax: $', format(total_sales_tax, '6,.2f'), sep='')
    print('Total          : $', format(total, '6,.2f'), sep='')

##########################
### Call the main function
main()
