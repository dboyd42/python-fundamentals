#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved
# Program: Pattern Stars
# Description: Loops an upside-down triangle of stars
# Status: Complete
# Date: 2019/08/19

# Declare variables
rows = 7

# Calculate and display pattern
for i in range(rows, 0, -1):
    for j in range(i):
        print('*', end='')
    print()
