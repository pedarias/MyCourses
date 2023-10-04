# The problem is defined as finding the length of the longest subsequence that is common to both given sequences, X and Y.
# A subsequence is a sequence that appears in the same order but not necessarily contiguous in both sequences.


def longestsub(X, Y, m, n):  # X,Y: The first/second sequence of length m,n.
    l = list()
    for i in range(m + 1):  # create a 2D list of dimensions (m+1) x (n+1).
        l.append(
            [None] * (n + 1)
        )  # The extra "+1" is used to accommodate the base cases (i.e., i=0 or j=0).
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:  # base case
                l[i][j] = 0
            elif (
                X[i - 1] == Y[j - 1]
            ):  # This checks if the elements at positions (i-1) in sequence X and (j-1) in sequence Y are equal.
                l[i][j] = (
                    l[i - 1][j - 1] + 1
                )  # If yes, the value in the current cell is set to the value diagonally above it (i-1, j-1) plus 1
            else:
                l[i][j] = max(
                    l[i - 1][j], l[i][j - 1]
                )  # If not, the value in the current cell is set to the maximum value between the cell directly above it (i-1, j) and the cell directly to the left (i, j-1).
    return l[m][n]


a = int(input())
X = list(map(int, input().split(" ", a)))
b = int(input())
Y = list(map(int, input().split(" ", b)))
print(longestsub(X, Y, a, b))

# This code uses dynamic programming to solve the LCS problem by building a 2D table and filling it based on the comparison of elements in the given sequences X and Y.
