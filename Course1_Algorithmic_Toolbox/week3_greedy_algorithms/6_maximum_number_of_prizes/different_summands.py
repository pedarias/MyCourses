# python3
n = int(input())
if n == 1:
    print(1)
    print(1)
    quit()
W = n
prizes = []
for i in range(1, n):
    if W > 2 * i:
        prizes.append(i)
        W -= i
    else:
        prizes.append(W)
        break

print(len(prizes))
print(" ".join([str(i) for i in prizes]))

# EXAMPLE n=10. The code follows a strategy where it first allocates the smallest possible value (1)
# and then assigns the rest of the value (9) to the next available prize while considering the constraints.
