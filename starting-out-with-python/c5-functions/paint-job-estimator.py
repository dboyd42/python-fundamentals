#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved
# Program: Paint Job Estimator
# Description:
#     Calculates the amount of materials and costs for a paint job.
# Date: 2019/08/21
# Revised:
#     <revision date>

# Declare global constants
PAINT = 0  # bill[] index position
LABOR = 1  # bill[] index position
TOTAL = 2  # bill[] index position
SQFT_GAL = 112  # wall_space/paint_gal (in sqft)

def main():

    # Declare variables
    area = 0.00       # area of wall space (sq ft)
    paint_cost = 0.00 # price of paint per gallon
    paint_gal = 0.00  # number of gallons of paint
    labor_hrs = 0.00  # labor hours
    # [COST of PAINT, LABOR CHARGES, TOTAL JOB COST]
    bill = [0.00, 0.00, 0.00]

    # Run program
    area = get_area()
    paint_cost = get_paint_cost()
    paint_gal = calc_gal(area)
    labor_hrs = calc_labor(area)
    calc_charges(bill, paint_cost, paint_gal, labor_hrs)
    print()
    display(bill, paint_gal, labor_hrs)

# End Program

# Function get_area()
# Description: Gets area of wall space from user
# Calls: None
# Parameters: None
# Returns: float area

def get_area():

    # Return values
    return float(input('Enter the square feet of wall space to be painted: '))

# End Function

# Function get_paint_cost()
# Description: Gets cost of paint per gallon
# Calls: None
# Parameters: None
# Returns: float paint_cost

def get_paint_cost():

    # Return values
    return float(input('Enter the cost of paint per gallon: $'))

# End Function

# Function calc_gal()
# Description:  Calculates number of gallons required
# Calls: None
# Parameters: float area
# Returns: float paint_gal

def calc_gal(area):

    # Return values
    return (area / SQFT_GAL)


# End Function

# Function calc_labor()
# Description: Calculates the hours of labor
# Calls: None
# Parameters: area
# Returns: float labor_hrs

def calc_labor(area):

    # Declare local variables
    hrs_SQFT_GAL = 8   # number of labor hours per SQFT_GAL

    # Return values
    return (hrs_SQFT_GAL *  area / SQFT_GAL)

# End Function

# Function calc_charges()
# Description: Calulates cost of paint, labor charges, and total
# Calls: None
# Parameters: list bill[], float paint_cost, float paint_gal, float labor_hrs
# Returns: None

def calc_charges(bill, paint_cost, paint_gal, labor_hrs):

    # Declare local variables
    chg_p_hour = 35.00  # labor charge per hour

    # Calculate charges
    bill[PAINT] = (paint_cost * paint_gal)
    bill[LABOR] = (labor_hrs * chg_p_hour)
    bill[TOTAL] = (bill[PAINT] + bill[LABOR])

# End Function

# Function display()
# Description: Displays charges and total
# Calls: None
# Parameters: list bill[], float paint_gal, float labor_hrs
# Returns: None

def display(bill, paint_gal, labor_hrs):

    # Declare local variables
    print('Summary')
    print('========')
    print('Paint: ', format(paint_gal, '6,.2f'), 'gallons')
    print('Labor: $', format(labor_hrs, '6,.2f'), ' hours', sep='')
    print('\nTotals')
    print('========')
    print('Paint: $', format(bill[PAINT], ',.2f'), sep='')
    print('Labor: $', format(bill[LABOR], ',.2f'), sep='')
    print('--------------')
    print('Total: $', format(bill[TOTAL], ',.2f'), sep='')

# End Function

# Call the main function
main()
