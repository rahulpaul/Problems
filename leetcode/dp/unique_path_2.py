"""https://leetcode.com/problems/unique-paths-ii/

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        grid = [[None for _ in range(n)] for _ in range(m)]
        
        x = m-1
        y = n-1
        grid[x][y] = 0 if obstacleGrid[x][y] == 1 else 1
        
        if grid[x][y] == 0:
            return 0
        
        x = m-1
        for y in range(n-2, -1, -1):
            has_obstacle = 1 == obstacleGrid[x][y]
            grid[x][y] = 0 if has_obstacle else grid[x][y+1]
        
        y = n-1
        for x in range(m-2, -1, -1):
            has_obstacle = 1 == obstacleGrid[x][y]
            grid[x][y] = 0 if has_obstacle else grid[x+1][y]
        
        for x in range(m-2, -1, -1):
            for y in range(n-2, -1, -1):
                has_obstacle = obstacleGrid[x][y] == 1
                grid[x][y] = 0 if has_obstacle else (grid[x+1][y] + grid[x][y+1])
        
        return grid[0][0]
        