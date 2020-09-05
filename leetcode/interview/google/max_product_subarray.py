""" https://leetcode.com/problems/maximum-product-subarray/

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

from typing import * 


def max_product(nums: List[int]) -> int:
    output_max: List[Optional[int]] = [None for _ in range(len(nums))]
    output_min: List[Optional[int]] = [None for _ in range(len(nums))]
    for i in range(len(nums)-1, -1, -1):
        if i == len(nums) - 1:
            output_max[i] = output_min[i] = nums[i]
        else:
            output_max[i] = max(nums[i], nums[i] * output_max[i+1], nums[i] * output_min[i+1])
            output_min[i] = min(nums[i], nums[i] * output_max[i+1], nums[i] * output_min[i+1])
    return max(output_max)


def main():
    assert max_product([2,3,-2,4]) == 6
    assert max_product([-2,0,-1]) == 0

    val = max_product([-2, 1, -1])
    print(val)
    assert val == 2


if __name__ == "__main__":
    main()
