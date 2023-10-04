# Uses python3


def fib_last(n):
    f = [0, 1]
    for i in range(2, n + 1):
        f.append((f[i - 1] + f[i - 2]) % 10) #The %10 operation is performed to keep only the last digit of the calculated Fibonacci number. Since the problem requires finding the last digit
    return f[n]


# Encontrar o último dígito do n-ésimo número na sequência de Fibonacci.
n = int(input())
print(fib_last(n))
