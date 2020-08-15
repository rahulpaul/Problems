"""https://leetcode.com/problems/unique-paths/

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28

"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        table = [[None for _ in range(n)] for _ in range(m)]
        
        x = m-1
        for y in range(n):
            table[x][y] = 1
        
        y = n-1
        for x in range(m):
            table[x][y] = 1
        
        for x in range(m-2, -1, -1):
            for y in range(n-2, -1, -1):
                table[x][y] = table[x+1][y] + table[x][y+1]
        
        return table[0][0]
