#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved
# Program: Calories from Fat and Carbohydrates
# Description:
#     Calculates calories that result from fat and carbohydrates
# Date: 2019/08/20
# Revised:
#     <revision date>

# Declare global constants

def main():

    # Declare & init variables
    fat = kcals_fat()    # units in kcals
    carbs = kcals_carbs()  # units in kcals

    # Display calulations
    print()
    display(fat, carbs)

# End Program

# Function kcals_fat
# Description: Calculates calories from fat
# Calls: none
# Parameters: none
# Returns: int fat

def kcals_fat():

    # Declare and init local variables
    fat = int(input('Enter number of fat   grams consumed in a day: '))

    # Return values
    return (fat*9)

# End Function

# Function kcals_carbs
# Description: Calculates calories from carbs
# Calls: none
# Parameters: none
# Returns: int carbs

def kcals_carbs():

    # Declare and init local variables
    carbs = int(input('Enter number of carbs grams consumed in a day: '))

    # Return values
    return (carbs*4)

# End Function

# Function display
# Description: Displays the calories from fat and carbs
# Calls: none
# Parameters:
#   int fat
#   int carbs
# Returns: none

def display(fat, carbs):

    print('Calories from fat  :', fat, 'calories')
    print('Calories from carbs:', carbs, 'calories')

# End Function

# Call the main function
main()
