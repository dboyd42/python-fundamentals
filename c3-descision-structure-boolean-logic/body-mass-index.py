#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved
# Program: Body Mass Index
# Description: Calculates and displays a peson's BMI.
# Status: Complete
# Date: 2019/08/14

# Get user weight & height
height = float(input('Enter your height (ins): '))
weight = float(input('Enter your weight (lbs): '))

# Calculate BMI
bmi = (weight * 703 / (height**2))

# Determine weight condition
if bmi < 18.5:
    health = "underweight"
elif bmi >= 18.5 and bmi <= 25:
    health = "optimal"
elif bmi > 25 and bmi < 30:
    health = "overweight"
elif bmi >= 30:
    health = "obese"
else:
    health = "ERROR"

# Display the user's BMI
print('Your BMI is', format(bmi, '.2f'), 'and you\'re considered', health)
