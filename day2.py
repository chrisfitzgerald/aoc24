"""day2.py."""
import re

# extract data
data = open('sample.txt', 'r')

reports = []

for line in data:
    levels = re.findall(r'[0-9]+', line)
    if levels:
        reports.append([int(level) for level in levels[:5]])

data.close()

print(reports)
