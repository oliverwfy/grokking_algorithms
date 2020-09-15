# Recursion

"""
recursion contains two cases
base case      -- when the function does not call itself
recursive case -- when the function call itself

D&C (divide & conquer) is a well-known recursive technique

Tips for recursion:
1. Find the base case, usually an empty array or only with one element.
2. According to D&C, come up with a recursive case, which consecutively calls itself until reach the base case.
3. ALl function calls go onto the call stack, concisely, LIFO (last-in-first-out).

"""


# countdown from a nature number to 0
def countdown(integer):
    if integer >= 0:
        print(integer)
        countdown(integer - 1)


# Exercise
# 4.1 Write out the code for the earlier sum function.
# 4.2 Write a recursive function to count the number of items in a list.
# 4.3 Find the maximum number in a list.
# 4.4 Come up with the base case and recursive case for binary search?


def sum_list(target_list):
    if target_list:
        return target_list[0] + sum(target_list[1:])
    else:
        return 0


def len_of_list(target_list):
    if target_list:
        return 1 + len_of_list(target_list[1:])
    else:
        return 0


def find_max(target_list):
    if len(target_list) == 2:
        return target_list[0] if target_list[0] > target_list[1] else target_list[1]
    sub_max = find_max(target_list[1:])
    return target_list[0] if target_list[0] > sub_max else sub_max
