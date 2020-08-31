""" https://leetcode.com/problems/sliding-window-median/

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Your job is to output the median array for each window in the original array.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
Therefore, return the median sliding window as [1,-1,-1,3,5,6].

Note:
You may assume k is always valid, ie: k is always smaller than input array's size for non-empty array.
Answers within 10^-5 of the actual value will be accepted as correct.
"""

from typing import *
from sortedcontainers import SortedList


def _get_median(left: SortedList, right: SortedList) -> float:
    if len(left) < len(right):
        return right[0]
    if len(left) > len(right):
        return left[-1]
    return (left[-1] + right[0]) / 2


def _remove_and_add(remove_val, add_val, left, right):
    try:
        left.remove(remove_val)
    except ValueError:
        right.remove(remove_val)

    _add_value(add_val, left, right)


def _add_value(val, left: SortedList, right: SortedList):
    median = _get_median(left, right)
    if len(left) < len(right):
        # need to add val to left
        if val <= median:
            left.add(val)
        else:
            val2 = right[0]
            right.remove(val2)
            left.add(val2)
            right.add(val)
    elif len(left) > len(right):
        # need to add val to right
        if val >= median:
            right.add(val)
        else:
            val2 = left[-1]
            left.remove(val2)
            right.add(val2)
            left.add(val)
    else:
        # can add in either
        if val <= median:
            left.add(val)
        else:
            right.add(val)


def sliding_median(nums: List[int], k: int) -> List[float]:
    left = SortedList()
    right = SortedList()

    left.add(nums[0])

    for i in range(1, k):
        _add_value(nums[i], left, right)

    medians = [_get_median(left, right)]

    for i in range(k, len(nums)):
        remove_val = nums[i - k]
        add_val = nums[i]
        _remove_and_add(remove_val, add_val, left, right)
        medians.append(_get_median(left, right))

    return medians


def main():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    output = sliding_median(nums, k)
    print(output)
    expected = [1., -1., -1., 3., 5., 6.]
    assert output == expected


if __name__ == "__main__":
    main()
