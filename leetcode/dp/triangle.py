""" https://leetcode.com/problems/triangle/

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        cache = []
        for row in triangle:
            cache.append([None for _ in range(len(row))])
            
        cache[0][0] = triangle[0][0]
        for row_idx in range(1, len(triangle)):
            for col_idx in range(0, row_idx+1):
                if col_idx == 0:
                    cache[row_idx][col_idx] = cache[row_idx - 1][col_idx] + triangle[row_idx][col_idx]
                elif col_idx == row_idx:
                    cache[row_idx][col_idx] = cache[row_idx - 1][col_idx - 1] + triangle[row_idx][col_idx]
                else:
                    v1 = cache[row_idx - 1][col_idx] + triangle[row_idx][col_idx]
                    v2 = cache[row_idx - 1][col_idx - 1] + triangle[row_idx][col_idx]
                    cache[row_idx][col_idx] = min(v1, v2)
        
        return min(cache[-1])
            