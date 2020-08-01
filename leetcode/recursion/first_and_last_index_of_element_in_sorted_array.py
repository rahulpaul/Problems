""" Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].


Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

"""

from typing import List, Tuple


def solve(nums: List[int], target: int, i: int, j: int) -> Tuple[int, int]:
    min_idx, max_idx = None, None
    if i<= j:
        mid_idx = (i+j) // 2
        if nums[mid_idx] > target:
            # only search left
            min_idx, max_idx = solve(nums, target, i, mid_idx-1)
        elif nums[mid_idx] < target:
            # only search right
            min_idx, max_idx = solve(nums, target, mid_idx+1, j)
        else:
            # seach both left and right
            min_idx, max_idx = mid_idx, mid_idx

            idx, _ = solve(nums, target, i, mid_idx-1)
            if idx is not None:
                min_idx = idx

            _, idx = solve(nums, target, mid_idx+1, j)
            if idx is not None:
                max_idx = idx
    
    return min_idx, max_idx



class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_idx, right_idx = solve(nums, target, 0, len(nums)-1)
        if left_idx is None and right_idx is None:
            return -1, -1
        return left_idx, right_idx