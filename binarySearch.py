# Binary search
"""
O(log n)
Binary search is only used for a sorted list,
and needs [log n + 1] operations.
[] is an operation of truncation ( e.g., [2.4] = 2 )

"""
sample_list = [1, 3, 5, 7, 9]


def binary_search(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1
    idx = None

    while low <= high:
        mid = (low + high) // 2
        mid_value = sorted_list[mid]
        if mid_value == target:
            idx = mid
            break
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1
    return idx


print(binary_search(sample_list, 5))

