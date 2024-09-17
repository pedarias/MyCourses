# python3
n = int(input())
lst = []

for _ in range(n):
    a, b = [int(i) for i in input().split()]
    lst.append((a, b))

lst.sort(key=lambda x: x[1])

j = 0
coordinates = []  # Store the end points of non-overlapping intervals.

while j < n:  # Iterates through the sorted list of intervals
    curr = lst[j]  # Assign the current interval to curr
    while (
        j < n - 1 and curr[1] >= lst[j + 1][0]
    ):  # This nested while loop checks for overlapping intervals.j < n-1 It ensures that we're not considering the last interval, as there is no interval after it to compare with.
        j += 1  # It iterates while the current interval's end point is greater than or equal to the start point of the next interval (lst[index + 1])
    coordinates.append(curr[1])
    j += 1
print(len(coordinates))
print(" ".join([str(i) for i in coordinates]))
