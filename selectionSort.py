# Selection sort
"""
O(n^2)

"""

sample_array = [5, 3, 6, 2, 10]


def find_min(array):
    min_val = array[0]
    min_idx = 0
    for i in range(1, len(array)):
        if array[i] < min_val:
            min_val = array[i]
            min_idx = i
    return min_idx


def selection_sort(array):
    sorted_array = []
    for i in range(len(array)):
        idx = find_min(array)
        sorted_array.append(array.pop(idx))
    return sorted_array


print(selection_sort(sample_array))
