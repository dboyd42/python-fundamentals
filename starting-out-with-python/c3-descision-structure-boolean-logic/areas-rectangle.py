#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved

# Program: Areas of Rectangles
# Description: Calculates length and width of two rectangles and outputs which
#              rectangle has the greater area.
# Status: Complete
# Date: 2019/08/13

# Declare variables
#rectangle1
#rectangle2

# Get dimensions
rect1_width = float(input('Enter rectangle 1\'s width: '))
rect1_length = float(input('Enter rectangle 1\'s length: '))
rect2_width = float(input('Enter rectangle 2\'s width: '))
rect2_length = float(input('Enter rectangle 2\'s length: '))

# Calculate area
rect1_area = (rect1_width * rect1_length)
rect2_area = (rect2_width * rect2_length)

# Determine which rect has greater area & output result
print()
if rect1_area == rect2_area:
    print('Rectangles have equal areas.')
elif rect1_area > rect2_area:
    print('Rectangle 1 has a greater area.')
else:
    print('Rectangle 2 has a greater area.')
