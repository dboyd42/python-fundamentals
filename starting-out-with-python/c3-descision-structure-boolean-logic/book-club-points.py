#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved
# Program: Book Club Points
# Description: Displays the number of points awarded based on book purchases.
# Status: Complete
# Date: 2019/08/14

# Get number of books purchased
books = int(input('Enter the number of purchased books: '))

# Determine award points
if books == 2 or books == 3:
    points = 5
elif books == 4 or books == 5:
    points = 15
elif books == 6 or books == 7:
    points = 30
elif books >= 8:
    points = 60
else:
    points = 0

# Display points
print('Number of points awarded:', points)
