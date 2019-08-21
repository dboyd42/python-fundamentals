#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved
# Program: Property Tax
# Description:
#     Calculates assessment value and property tax.
# Date: 2019/08/20
# Revised:
#     <revision date>

# Declare global constants
A_RATE = 0.60            # Assessment rate
P_TAX_RATE = (0.72/100)  # Property tax is $0.70/$100.00 of assessment value

def main():

    # Declare variables
    p_value = 0.00  # Property value
    a_value = 0.00  # Assessment value of property
    t_value = 0.00  # Property tax value of assessment

    # Run Program
    p_value = get_property_value()
    a_value = assess(p_value)
    t_value = tax_assessment(a_value)
    print()
    display(a_value, t_value)

# End Program

# Function get_property_value
# Description: Gets the property value from user
# Calls: none
# Parameters: none
# Returns: float p_value

def get_property_value():

    # Return values
    return float(input('Enter the property value: $'))

# End Function

# Function assess
# Description: Assess the property' value
# Calls: none
# Parameters: float p_value
# Returns: float a_value

def assess(property):

    # Return values
    return (A_RATE * property)

# End Function

# Function tax_assessment
# Description: Calculates property tax at $0.72 per $100 of assessment value
# Calls: none
# Parameters: float a_value
# Returns: property t_value

def tax_assessment(assessment):

    # Return values
    return (P_TAX_RATE * assessment)

# End Function

# Function display
# Description: Displays the assessment value and property tax
# Calls: none
# Parameters:
#       float a_value
#       float t_value
# Returns: none

def display(a_value, t_value):

    # Return values
    print('Property Totals:')
    print('===========================')
    print('Assessment Value: $', format(a_value, ',.2f'), sep='')
    print('Property Tax    : $', format(t_value, ',.2f'), sep='')

# End Function

# Call the main function
main()

