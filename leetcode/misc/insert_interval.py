""" https://leetcode.com/problems/insert-interval/

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""

from typing import *


def _search(intervals: List[Tuple[int, int]], value: int, i: int, j: int) -> int:
    if i > j:
        return None
    mid = (i + j) // 2
    interval = intervals[mid]
    if interval[0] <= value <= interval[1]:
        return mid
    
    if value < interval[0]:
        return _search(intervals, value, i, mid-1)
    else:
        return _search(intervals, value, mid+1, j)


def _pre_process(intervals: List[Tuple[int, int]], prefix, suffix) -> List[Tuple[int, int, bool]]:
    x1, x2 = intervals[0]
    output = [prefix, (x1, x2, True)]
    for i in range(1, len(intervals)):
        last_x1, last_x2 = intervals[i-1]
        x1, x2 = intervals[i]
        if last_x2 < x1:
            output.append((last_x2+1, x1-1, False))
        output.append((x1, x2, True))
    
    output.append(suffix)
    return output
        


def _insert(intervals: List[Tuple[int, int]], new_interval: Tuple[int, int]) -> List[Tuple[int, int]]:
    x1, x2 = new_interval
    
    prefix = float('-inf'), intervals[0][0] - 1, False
    suffix = intervals[-1][1] + 1, float('inf'), False
    intervals = _pre_process(intervals, prefix, suffix)
    n = len(intervals)
    
    i1 = _search(intervals, x1, 0, n-1)
    i2 = _search(intervals, x2, 0, n-1)
    
    output_part1 = []
    output_part2 = []
    p1 = p2 = None
    for i in range(n):
        int_x1, int_x2, is_real = intervals[i]
        if i < i1:
            if is_real:
                output_part1.append((int_x1, int_x2))
            continue
        
        if i == i1:
            p1 = int_x1 if is_real else x1
        
        if i1 < i < i2:
            continue
        
        if i == i2:
            p2 = int_x2 if is_real else x2
            continue
        
        if i > i2:
            if is_real:
                output_part2.append((int_x1, int_x2))
    
    return output_part1 + [(p1, p2)] + output_part2
    



class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        return _insert(intervals, newInterval)


def main():
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    output = Solution().insert(intervals, newInterval)
    print(f'output = {output}')
    assert output == [(1,5),(6,9)]

    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    output = Solution().insert(intervals, newInterval)
    print(f'output = {output}')
    assert output == [(1,2),(3,10),(12,16)]


if __name__ == "__main__":
    main()
