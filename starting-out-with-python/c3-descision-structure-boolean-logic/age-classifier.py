#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved

# Program: Age Classifier
# Description: Classifies a person's age group based off their age range.
# Status: Incomplete
# Date: 2019/08/13

# Declare variables


# Get data
age = float(input('Enter a person\'s age: '))

# Determine age group
if age <= 1:
    group = 'infant'
elif age > 1 and age < 13:
    group = 'child'
elif age >= 13 and age < 20:
    group = 'teenager'
elif age >= 20:
    group = 'adult'
else:
    print('How\'d you get here?!')

# Display age group
print('Person\'s age group is:', group)
