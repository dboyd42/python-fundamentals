#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved
# Program: Pattern Hashtags
# Description: Creates a standing ladder border of hashtags
# Status: Complete
# Date: 2019/08/19

# Declare variables
rows = 7

# Loop and display pattern
for i in range(rows):
    print('#', end='')
    for j in range(i+1):
        print(' ', end='')
    print('#')

