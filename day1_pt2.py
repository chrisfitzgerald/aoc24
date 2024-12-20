import re

# sampe data
data = open('day1_p2_data.txt', 'r').read() 

# extract digits and sort in lists
row1 = []
row2 = []
for line in data.split('\n'):
    first_digit = re.findall(r'^[0-9]{1,5}', line)
    if first_digit:
        row1.append(int(first_digit[0]))

    second_digit = re.findall(r'[0-9]{1,5}$', line)
    if second_digit:
        row2.append(int(second_digit[0]))

# count the number of times digit from row1 is repeated in row2 for each digit in row1 and store in a new list
count = [row2.count(i) * i for i in row1]

# sum the total to get the value
sum_count = sum(count)

#print value to console
print(sum_count)