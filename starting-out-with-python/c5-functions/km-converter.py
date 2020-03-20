#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved
# Program: Kilometer Converter
# Description: Converts km to miles.
# Status: Complete
# Date: 2019/08/19

# Global Constants
KM_P_MI = 0.6213712

def main():
    # Get the kilometers
    km = float(input('Enter the number of kilometers: '))

    # Get the miles of the km
    mi = km_to_mi(km)

    # Display the km
    print(format(km, ',.2f'), 'km =', format(mi, ',.2f'), 'miles')

def km_to_mi(km):
    return (km * KM_P_MI)

# Call the main function
main()
