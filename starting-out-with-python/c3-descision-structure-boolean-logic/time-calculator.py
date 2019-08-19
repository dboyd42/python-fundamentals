#!/usr/bin/env python3
# Copyright 2019 David Boyd, all rights reserved
# Program: Time Calculator
# Description: Converts seconds to mins, hours, days.
# Status: Complete
# Date: 2019/08/14

# Declare variables
sec_in_mins = 60
sec_in_hours = 3600
sec_in_days = 86400

# Get number of seconds
usr_sec = int(input('Enter number of seconds: '))

# Determine seconds to units conversions
if usr_sec >= sec_in_mins and usr_sec < sec_in_hours:
    unit = "minute(s)"
    time = usr_sec / sec_in_mins
elif usr_sec >= sec_in_hours and usr_sec < sec_in_days:
    unit = "hour(s)"
    time = usr_sec / sec_in_hours
elif usr_sec >= sec_in_days:
    unit = "day(s)"
    time = usr_sec / sec_in_days

# Display the number of units in that time
print('There are', format(time, '.2f'), unit, 'in', usr_sec, 'seconds')
