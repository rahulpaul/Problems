""" https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/

Given an array of integers arr and an integer target.

You have to find two non-overlapping sub-arrays of arr each with sum equal target. There can be multiple answers so you have to find an answer where the sum of the lengths of the two sub-arrays is minimum.

Return the minimum sum of the lengths of the two required sub-arrays, or return -1 if you cannot find such two sub-arrays.



Example 1:

Input: arr = [3,2,2,4,3], target = 3
Output: 2
Explanation: Only two sub-arrays have sum = 3 ([3] and [3]). The sum of their lengths is 2.
Example 2:

Input: arr = [7,3,4,7], target = 7
Output: 2
Explanation: Although we have three non-overlapping sub-arrays of sum = 7 ([7], [3,4] and [7]), but we will choose the first and third sub-arrays as the sum of their lengths is 2.
Example 3:

Input: arr = [4,3,2,6,2,3,4], target = 6
Output: -1
Explanation: We have only one sub-array of sum = 6.
Example 4:

Input: arr = [5,5,4,4,5], target = 3
Output: -1
Explanation: We cannot find a sub-array of sum = 3.
Example 5:

Input: arr = [3,1,1,1,5,1,2,1], target = 3
Output: 3
Explanation: Note that sub-arrays [1,2] and [2,1] cannot be an answer because they overlap.
"""
from typing import *


"""
arr = [3,2,1,1,1,3], target = 3

{
    3: 0,
    5: 1,
    6: 2,
    7: 3,
    8: 4,
    11: 5

}


"""

def find_subarrays(arr: List[int], target: int):
    cumsum = 0
    cumsum_to_index = {0: -1}
    subarrays = []
    for i, num in enumerate(arr):
        cumsum += num
        cumsum_to_index[cumsum] = i

        if num == target:
            subarrays.append((i, i))
        else:
            v = cumsum - target
            if v in cumsum_to_index:
                subarrays.append((cumsum_to_index[v]+1, i))

    return subarrays


def is_overlapping(int1: Tuple[int, int], int2: Tuple[int, int]) -> bool:
    return int1[1] >= int2[0]


def interval_size(interval: Tuple[int, int]) -> int:
    return interval[1] - interval[0] + 1


def find_min_non_overlapping_intervals(intervals: List[Tuple[int, int]]) -> int:
    n = len(intervals)
    interval_sizes = [interval_size(interval) for interval in intervals]
    index_to_min_interval_size = min_mapping(interval_sizes)
    output = None
    for i in range(n - 1):
        int1 = intervals[i]
        for j in range(i + 1, n):
            int2 = intervals[j]
            if not is_overlapping(int1, int2):
                # find min interval
                min_ = index_to_min_interval_size[j]
                total = interval_size(int1) + min_
                if output is None or output > total:
                    output = total
                break

    return output if output is not None else -1


def min_mapping(arr: List[int]):
    output = {}
    current_min = None
    for i in range(len(arr)-1, -1, -1):
        val = arr[i]
        if current_min is None or current_min > val:
            current_min = val
        output[i] = current_min
    return output


from typing import *

MAX = 2**31 - 1


def min_sum_of_lengths_using_sliding_window(arr: List[int], target: int) -> int:
    n = len(arr)
    presum = 0  # prefix sum
    left = 0
    min_lens = [MAX] * n
    min_len = MAX
    ans = MAX
    for right in range(n):
        presum += arr[right]
        while presum > target:
            presum -= arr[left]
            left += 1

        if presum == target:
            curr_len = right - left + 1
            min_len = min(min_len, curr_len)
            if left > 0 and min_lens[left-1] != MAX:
                ans = min(ans, curr_len + min_lens[left-1])

        min_lens[right] = min_len
    
    return -1 if ans == MAX else ans 


def min_sum_of_lengths_using_intervals(arr: List[int], target: int) -> int:
    intervals = find_subarrays(arr, target)
    return find_min_non_overlapping_intervals(intervals)

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        # return min_sum_of_lengths_using_intervals(arr, target)
        return min_sum_of_lengths_using_sliding_window(arr, target)


def main():
    arr = [3,2,1,1,1,3]
    target = 3
    assert Solution().minSumOfLengths(arr, target) == 2

    arr = [3, 1, 1, 1, 5, 1, 2, 1]
    target = 3
    assert Solution().minSumOfLengths(arr, target) == 3

    arr = [5, 5, 4, 4, 5]
    target = 3
    assert Solution().minSumOfLengths(arr, target) == -1

    arr = [4, 3, 2, 6, 2, 3, 4]
    target = 6
    assert Solution().minSumOfLengths(arr, target) == -1

    arr = [7, 3, 4, 7]
    target = 7
    assert Solution().minSumOfLengths(arr, target) == 2

    arr = [3, 2, 2, 4, 3]
    target = 3
    assert Solution().minSumOfLengths(arr, target) == 2



if __name__ == '__main__':
    main()
