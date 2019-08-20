#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved
# Program: Automobile Costs
# Description: 
# 	Gets and displays monthly automobile costs 
# Date: 2019/08/20
# Revised: 
# 	<revision date> 

# Declare global constants
NAME = 0
AMOUNT = 1

def main():

    # Declare variables
    costs = [ ["loan", 0.00], ["insurance", 0.00], ["gas", 0.00], 
              ["oil", 0.00], ["tires", 0.00], ["maintenance", 0.00], 
              ["total", 0.00] ]

    # Run program
    get_costs(costs)
    print()
    display_costs(costs)

# End Program

# Function get_costs
# Description:
#	    Gets the montly costs from the user
# Calls:
#	    None
# Parameters:
#	    costs []
# Returns:
#	    None

def get_costs(costs):

    # Declare variables
    total = 0.00
    
    # Fill in costs list
    for i in range(len(costs)):
        if (i < len(costs)-1):
            # Get costs from user
            costs[i][AMOUNT] = float(input('Enter the amount for the '+ costs[i][NAME] + ': $'))
            # Accumulate costs
            total += costs[i][AMOUNT]
        else:    
            # Total costs
            costs[i][AMOUNT] = total

# End Function

# Function display_costs
# Description:
#	    Displays the montly costs and total
# Calls:
#	    None
# Parameters:
#	    costs[]
# Returns:
#	    None

def display_costs(costs):
    
    # Declare variables
    width = 9  # string format

    print('Monthly Charges')
    print('===============')
    for i in range(len(costs)):
        if (len(costs[i][NAME]) < width):
            print(costs[i][NAME], '\t\t: $', format(costs[i][AMOUNT], \
                  ',.2f'), sep='')
        else:
            print(costs[i][NAME], '\t: $', format(costs[i][AMOUNT], \
                  ',.2f'), sep='')

# End Function

# Call main Function
main()
