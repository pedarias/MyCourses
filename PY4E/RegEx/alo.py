import re

file = open("py4e-data.dr-chuck.net_regex_sum_1841321.txt", "r")

numlist = list()
for line in file:
    line = line.rstrip()
    # In here out all numbers as a list
    line_values = re.findall("[0-9]+", line)
    if len(line_values) > 0:
        numlist = numlist + line_values
sum = 0
for value in numlist:
    sum = sum + int(value)

print(f"In file total of the number list is {sum}")
