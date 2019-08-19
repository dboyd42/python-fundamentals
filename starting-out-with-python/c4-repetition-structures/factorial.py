#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved
# Program: Factorial
# Description: Calculates the factorial of a nubmer
# Status: Complete
# Date: 2019/08/19

# Declare variables
number = 0
factorial = 1

# Get factorial of number
number = int(input('Enter a nonnegative integer: '))

# Validate user's number
if (number <= 0):
    print('Factorial must be greater than or equal to 1')
    raise SystemExit

# Calculate factorial of number
for i in range(1, number+1):
   factorial *= i

# Display factorial
print('Factorial = ', format(factorial, ',d'))
