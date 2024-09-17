import math

global newList
newList = []


def binary_search_rec(input_keys, i, low, high):
    if low > high:
        return newList.append(-1)

    # Finding the mid using floor division
    mid = low + ((high - low) // 2)

    # Target value is present at the middle of the array
    if input_keys[mid] == i:
        return newList.append(mid)

    # Target value is present in the low subarray
    elif input_keys[mid - 1] < i < input_keys[mid]:
        return newList.append(-1)

    elif i < input_keys[mid]:
        return binary_search_rec(input_keys, i, low, mid - 1)

    # Target value is present in the high subarray
    else:
        return binary_search_rec(input_keys, i, mid + 1, high)


def binary_search(input_keys, input_queries):
    for i in input_queries:
        binary_search_rec(input_keys, i, 0, len(input_keys) - 1)
    for i in newList:
        print(i)


# input_keys=[1,5,8,12,13]
# input_queries = [8, 1, 23, 1, 11]

# binary_search(input_keys,input_queries)


if __name__ == "__main__":
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    binary_search(input_keys, input_queries)
