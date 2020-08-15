""" https://leetcode.com/problems/minimum-path-sum/

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""

from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        s_grid = [[None for _ in range(n)] for _ in range(m)]
        
        s_grid[m-1][n-1] = grid[m-1][n-1]
        
        y = n-1
        for x in range(m-2, -1, -1):
            s_grid[x][y] = s_grid[x+1][y] + grid[x][y]
        
        x = m-1
        for y in range(n-2, -1, -1):
            s_grid[x][y] = s_grid[x][y+1] + grid[x][y]
        
        for x in range(m-2, -1, -1):
            for y in range(n-2, -1, -1):
                s_grid[x][y] = grid[x][y] + min(s_grid[x+1][y], s_grid[x][y+1])
        
        return s_grid[0][0]
        