""" https://leetcode.com/problems/max-points-on-a-line/
"""

import sys
from typing import List
from collections import defaultdict


def slope(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    
    if dx == 0:
        return sys.maxsize
    else:
        return round(dy / dx, 5)


def max_points(points):
    n = len(points)
    result = defaultdict(list)
    for i in range(n):
        for j in range(i+1, n):
            slope_ = slope(points[i], points[j])
            result[(i, slope_)].append(j)
    
    for value in result.values():
        n_ponits = 1 + len(value)
    
    return 1 + max(len(value) for value in result.values())


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        return max_points(points)


def main():
    assert max_points([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]) == 4
    assert max_points([[1,1],[2,2],[3,3]]) == 3


if __name__ == "__main__":
    main()
