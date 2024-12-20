"""
day1.py.

This code is to solve the first challenge of the Advent of Code 2024
"""

import re

# extract data from file
data = open('day1_data.txt', 'r')
row1 = []
row2 = []

# extract digits and sort in lists
for line in data:
    first_digit = re.findall(r'^[0-9]{1,5}', line)
    if first_digit:
        row1.append(int(first_digit[0]))

    second_digit = re.findall(r'[0-9]{1,5}$', line)
    if second_digit:
        row2.append(int(second_digit[0]))

# sort the stanky lists
row1.sort()
row2.sort()

# look for the difference in values between the sorted lists

difference = [abs(a - b) for a, b in zip(row1, row2)]

# sum the total to get the value
answer = sum(difference)

print(answer)
