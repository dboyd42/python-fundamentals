#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved
# Program: squared-list
# Description:
#     This program to accepts a list then prints another list with the cubes of
#     the elements of first list.
# Date: 2019/10/06
# Revised:
#     <revision date>

# list libraries used

# Declare global constants

def main():

    # Declare variables
    roots = 10
    size = roots+1
    rootls = []
    squaredls = []

    # Create a list of numbers
    for i in range(size):
        rootls.append(i)

    # Square rootls
    for i in range(size):
        squared_num = i*i
        squaredls.append(squared_num)

    # Print lists
    print("Root\t| Square")
    print("================")
    for i in range(size):
        print(rootls[i], "\t|", squaredls[i])

# End Program
main()

