"""
Assignment 4: Algorithm Practice (Advanced Optional)
"""


def binary_search_position(numbers, target):
    n = len(numbers)
    beg = 0
    end = n - 1
    result = -1
    while beg <= end:
        mid = (beg + end) // 2
        if numbers[mid] <= target:
            beg = mid + 1
            result = mid
        else:
            end = mid - 1
    return result


print(binary_search_position([1, 2, 5, 6, 7], 1))  # should print 0
print(binary_search_position([1, 2, 5, 6, 7], 6))  # should print 3
