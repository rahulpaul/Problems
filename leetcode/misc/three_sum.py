""" https://leetcode.com/problems/3sum/

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
"""

from typing import *


def find_pairs(nums: List[int], lo: int, target: int) -> List[Tuple[int, int]]:
    """Assumption: nums is a sorted list"""
    hi = len(nums) - 1
    pairs = []
    while lo < hi:
        s = nums[lo] + nums[hi]
        if s == target:
            pairs.append((nums[lo], nums[hi]))
            lo += 1
            while lo < hi and nums[lo] == nums[lo-1]:
                lo += 1

        if s < target:
            lo += 1
        else:
            hi += -1
    return pairs


def three_sum_zero_with_pointers(nums: List[int]):
    output = []
    nums.sort()
    last_a = None
    for i in range(len(nums) - 1):
        a = nums[i]
        if a >= 0:
            break

        if a == last_a:
            continue

        pairs = find_pairs(nums, lo=i + 1, target=-a)
        for b, c in pairs:
            output.append((a, b, c))

        last_a = a

    return output


def main():
    nums = [-1, 0, 1, 2, -1, -4]
    expected = [(-1,-1,2), (-1,0,1)]
    actual = three_sum_zero_with_pointers(nums)
    print(actual)
    assert actual == expected

    nums = [-15,-10,-5,-5,3,5,5,10,12]
    expected = [(-15,3,12),(-15,5,10),(-10,5,5),(-5,-5,10)]
    actual = three_sum_zero_with_pointers(nums)
    print(actual)
    assert actual == expected


if __name__ == "__main__":
    main()
