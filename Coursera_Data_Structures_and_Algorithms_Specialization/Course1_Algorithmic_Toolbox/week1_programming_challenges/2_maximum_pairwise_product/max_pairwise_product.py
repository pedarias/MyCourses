def max_pairwise_fast(n, a):
    max_index1 = 0
    max_index2 = 0
    for i in range(n):
        if a[i] > max_index1:
            max_index2 = max_index1
            max_index1 = a[i]
        elif a[i] > max_index2:
            max_index2 = a[i]
    return max_index1 * max_index2


if __name__ == "__main__":
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_fast(input_n, input_numbers))
