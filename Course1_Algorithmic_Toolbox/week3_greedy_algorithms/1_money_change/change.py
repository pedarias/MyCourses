# Compute the minimum number of coins needed to change the given value
# into coins with denominations 1, 5, and 10
n = int(input())
count = 0
for i in [10, 5, 1]:
    if n >= i:
        q = n // i
        count += q
        n = n % i
        if n == 0:
            print(count)
            quit()
