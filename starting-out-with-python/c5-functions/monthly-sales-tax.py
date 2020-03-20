#!/usr/bin/env python3
# Copyright 2020 David Boyd, all rights reserved
# Program: monthly-sales-tax.py
# Description:
#   A retail compay must file monthly sales tax report listing the total sales
#   for the month, and the amount of state and county sales tax collected.  The
#   state sales tax rate is 5 percent and the county sales tax rate is 2.5
#   percent.  Write a program that asks the user to enter the total sales for
#   the month.  From this figure, the application should calculate and display
#   the following
#       - the amount of county sales tax
#       - the amount of state sales tax
#       - the total sales tax (county plus state)
# Date: 2020-03-20
# Revised:

# Global Variables
STATE_SALES_TAX = 0.05      # 5%
COUNTY_SALES_TAX = 0.025    # 2.5%

###
### main()
###
def main():

    # Get monthly sales
    month_sales = get_monthly_sales()
    # Calculate all sales tax
    state, county, total = calc_sales_tax(month_sales)
    # Display totals
    print()
    display_totals(state, county, total)


###
### Calculate [All] Sales Tax
###
def calc_sales_tax(monthly_sales):

    total_state_sales_tax = monthly_sales * STATE_SALES_TAX
    total_county_sales_tax = monthly_sales * COUNTY_SALES_TAX
    total_sales_tax = total_state_sales_tax + total_county_sales_tax
    return total_sales_tax, total_county_sales_tax, total_sales_tax

###
### Display Results
###
def display_totals(state, county, total):

    print("Monthly Tax")
    print("============================")
    print('Total State Tax : $', format(state, ',.2f'), sep='')
    print('Total County Tax: $', format(county, ',.2f'), sep='')
    print('Total Sales Tax : $', format(total, ',.2f'), sep='')

###
### Get Monthly Sales
###
def get_monthly_sales():

    return float(input("Enter the total sales for the month: $"))

###
### Run Program
###
main()

