#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved
# Program: Bug Collector
# Description: Keeps a running total number of bugs collected during 5 days.
# Status: Complete
# Date: 2019/08/14

# Declare variables
bugs = 0

# Get number of bugs for each day
for x in range(5):
    stringx = str(x+1)
    days_total = int(input('Enter number of bugs collected for day ' \
            + stringx + ': '))
    bugs += days_total

# Display total number of bugs
print('Total number of bugs collected: ', bugs)
