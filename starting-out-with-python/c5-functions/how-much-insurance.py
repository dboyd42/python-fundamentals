#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved
# Program: How Much Insurance?
# Description: Calculates investment amount in building insurance.
# Status: Complete
# Date: 2019/08/20

############
### Main ###
############
def main():

    # Declare vars
    replace_cost = 0.00
    invest = 0.00

    # Get cost of structure
    replace_cost = float(input('Enter the replacement cost of ' \
                   'the building: $'))

    # calulate investment amount
    invest = investment_cost(replace_cost)

    # Display amount
    print('The minimum amount of insurance for the property is $', \
          format(invest, ',.2f'), sep='')

#######################
### Investment Cost ###
#######################
def investment_cost(cost):
    # Min percent to replace structure
    insurance_rate = 0.80
    # Return insurance amount of structure
    return (cost * insurance_rate)

##########################
### Call the main function
main()
