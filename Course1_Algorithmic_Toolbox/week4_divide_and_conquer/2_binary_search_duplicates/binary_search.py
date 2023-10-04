import math

global newList
newList = []


def binary_search_rec(input_keys, i, low, high):
    # if low > high:
    #   return newList.append(-1)
    mid = low + ((high - low) // 2)
    if input_keys[mid] == i and input_keys[mid - 1] != i:
        return newList.append(mid)
    elif input_keys[mid] == i and input_keys[mid - 1] == i:
        while input_keys[mid - 1] == i:
            mid = mid - 1
        return newList.append(mid)
    elif input_keys[mid - 1] < i < input_keys[mid]:
        return newList.append(-1)
    elif i < input_keys[mid]:
        return binary_search_rec(input_keys, i, low, mid - 1)
    elif i > input_keys[mid]:
        return binary_search_rec(input_keys, i, mid + 1, high)


def binary_search(input_keys, input_queries):
    for i in input_queries:
        binary_search_rec(input_keys, i, 0, len(input_keys) - 1)
    for i in newList:
        print(i)


input_keys = [2, 4, 4, 4, 7, 7, 9]
input_queries = [9, 4, 5, 2]

binary_search(input_keys, input_queries)

"""
if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    binary_search(input_keys, input_queries)

"""
