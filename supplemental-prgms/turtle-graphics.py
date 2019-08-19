#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved
# Program: Turtle Graphics
# Description: Draws various objects
# Notes: Linux requires Tkinter: apt install python3-tk
# Status: Complete
# Date: 2019/08/19

import turtle

# Square
for x in range(4):
    turtle.forward(100)
    turtle.right(90)

# Octagon
for x in range(8):
    turtle.forward(100)
    turtle.right(45)

# Designs
nCircles = 36  # num of cirlces to draw
radius = 100   # radius of each circle
angle = 10     # angle to turn

for x in range(nCircles):
    turtle.circle(radius)
    turtle.left(angle)

# Starburst
start_x = -200  # starting x coordinate
start_y = 0     # starting y coordinate
nLines = 36     # number of lines to draw
line_len = 400  # length of each line
angle = 170     # angle to turn

turtle.hideturtle()
turtle.penup()
turtle.goto(start_x, start_y)
turtle.pendown()

for x in range(nLines):
    turtle.forward(line_len)
    turtle.left(angle)

# Pause program
exit = input('Press ENTER to quit')
