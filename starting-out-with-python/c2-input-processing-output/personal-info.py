#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved
# Updated: 2019/10/06
# A program that display personal information

name    = input('Name    : ')
address = input('Address : ')
city    = input('City    : ')
state   = input('State   : ')
zipCode = input('Zip Code: ')
ph_num  = input('Phone Number : ')
major   = input('College Major: ')

print('\nPersonal Information')
print('--------------------')
print('Name           : ', name)
print('Address        : ', address)
print('City, State ZIP:  ', city, ', ', state, ' ', zipCode, sep='')
print('Phone Number   : ', ph_num)
print('College Major  : ', major)
