# This code solves the problem of finding the minimum number of operations needed
# to transform a given number n into 1 using three possible operations

import math

n = int(input())

# number of operations required for getting 0, 1, 2,.. , n
# list where each index i holds the minimum number of operations needed to transform the number i into 1.
num_operations = [0, 0] + [math.inf] * (n - 1)

for i in range(2, n + 1):
    temp1, temp2, temp3 = [math.inf] * 3

    temp1 = num_operations[i - 1] + 1
    if i % 2 == 0:
        temp2 = num_operations[i // 2] + 1
    if i % 3 == 0:
        temp3 = num_operations[i // 3] + 1
    min_ops = min(
        temp1, temp2, temp3
    )  # holds the minimum value among the three operations' costs,
    num_operations[i] = min_ops  # and this value is stored in num_operations[i].


print(num_operations[n])

# This second part is a backtracking process to reconstruct the sequence of numbers that leads to the minimum operations.
# Backtracking the numbers leading to n
nums = [n]
while n != 1:  # loop continues until n becomes 1.
    # Inside the loop, it checks which operation was responsible for reaching the current value of n with the minimum operations.
    # It then updates n and appends the corresponding number to the nums list.
    if n % 3 == 0 and num_operations[n] - 1 == num_operations[n // 3]:
        nums += [n // 3]
        n = n // 3
    elif n % 2 == 0 and num_operations[n] - 1 == num_operations[n // 2]:
        nums += [n // 2]
        n = n // 2
    else:
        nums += [n - 1]
        n = n - 1

print(" ".join([str(i) for i in nums][::-1]))
