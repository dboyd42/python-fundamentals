#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved

# Program: Hotdog Cookout Calculator
# Description: Determines the number of packages of hot dog buns needed with
#              the minimum amount of leftovers.
# Status: Complete
# Date: 2019/08/13

import math  # used for ceil (rounding up)

# Declare variables
hotdogs_per_pkg = 10
buns_per_pkg = 8

# Get data
nPeople = int(input('Enter the number of people attending the cookout: '))
nHotdog = int(input('Enter the number of hotdogs each person will eat: '))

# Calculate minimum number of needed hotdogs (assume 1 hotdog per bun)
min_nHotdogs = (nPeople * nHotdog)

# Determine number hotdog & bun packages needed
needed_hotdog_pkgs = math.ceil(min_nHotdogs / hotdogs_per_pkg)
needed_bun_pkgs = math.ceil(min_nHotdogs / buns_per_pkg)

# Determine total number of hotdogs & buns
total_nHotdogs = (needed_hotdog_pkgs * hotdogs_per_pkg)
total_nBuns = (needed_bun_pkgs * buns_per_pkg)

# Determine leftover hotdogs & buns
leftOver_hotdogs = (total_nHotdogs - min_nHotdogs)
leftOver_buns = (total_nBuns - min_nHotdogs)


# Display data
print()
print('===================================================')
print('Minimum number of packages of hot dogs required:', needed_hotdog_pkgs)
print('Minimum number of packages of hot buns required:', needed_bun_pkgs)
print('Number of hot dogs that will be left over      :', leftOver_hotdogs)
print('Number of hot buns that will be left over      :', leftOver_buns)
print('===================================================')
