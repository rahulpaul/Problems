""" https://leetcode.com/problems/maximal-rectangle/

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
"""

from typing import List, Any


class Data:
    ONE = '1'
    ZERO = '0'


class DataGrid:
    def __init__(self, data: List[List[Any]]):
        self.data = data
        
    @classmethod
    def of(cls, nrows: int, ncols: int):
        data = [[None for _ in range(ncols)] for _ in range(nrows)]
        return cls(data)
    
    @property
    def nrows(self):
        return len(self.data)
    
    @property
    def ncols(self):
        return len(self.data[0])
    
    def get(self, i: int, j: int):
        return self.data[i][j]
    
    def set(self, i: int, j: int, value: Any):
        self.data[i][j] = value


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        matrix = DataGrid(matrix)
        width_grid = DataGrid.of(matrix.nrows, matrix.ncols)
        for i in range(matrix.nrows):
            width = 0
            for j in range(matrix.ncols):
                val = matrix.get(i, j)
                if val == Data.ONE:
                    width += 1
                elif val == Data.ZERO:
                    width = 0
                else:
                    raise Exception(f"unexpected data {val}")
                
                width_grid.set(i, j, width)
        
        area_grid = DataGrid.of(matrix.nrows, matrix.ncols)
        for i in range(matrix.nrows):
            max_area = 0
            for j in range(matrix.ncols):
                min_width = width_grid.get(i, j)
                height = 1
                max_area = min_width*height
                for k in range(i-1, -1, -1):
                    width = width_grid.get(k, j)
                    if width == 0:
                        break
                        
                    height += 1
                    min_width = min(width, min_width)
                    area = min_width * height
                    max_area = max(area, max_area)
                
                area_grid.set(i, j, max_area)
        
        return max([max(row) for row in area_grid.data])
