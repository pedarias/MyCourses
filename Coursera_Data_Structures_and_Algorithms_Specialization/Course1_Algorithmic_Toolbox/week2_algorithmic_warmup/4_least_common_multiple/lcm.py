# Python3

a, b = [int(i) for i in input().split()]


def euclid_gcd(a, b):
    if b == 0:
        return a
    c = a % b
    return euclid_gcd(b, c)


# This step ensures that the euclid_gcd function is called with the greater value as the first argument to avoid negative values during the calculation.
if a > b:
    gcd = euclid_gcd(a, b)
else:
    gcd = euclid_gcd(b, a)

print(a * b // gcd)
