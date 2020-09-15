# Quick sort

"""
Average (best case) : O(n*log n).
Worst case : O(n^2).

Each level stack takes O(n) times.
Picking the first element of a sorted array needs O(n) stacks.
Picking the middle element of a sorted array needs O(log n) stacks.

"""

def quick_sort(target_array):
    if len(target_array) < 2:
        return target_array
    else:
        pivot = target_array[0]
        less_list = [i for i in target_array[1:] if i <= pivot]
        greater_list = [i for i in target_array[1:] if i > pivot]
        return quick_sort(less_list) + [pivot] + quick_sort(greater_list)


