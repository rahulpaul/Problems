"""https://leetcode.com/problems/bomb-enemy/

Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
Note: You can only put the bomb at an empty cell.

Example:

Input: [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
Output: 3 
Explanation: For the given grid,

0 E 0 0 
E 0 W E 
0 E 0 0

Placing a bomb at (1,1) kills 3 enemies.
"""


class CellContent:
    WALL = 'W'
    ENEMY = 'E'
    EMPTY = '0'

class Grid:
    
    def __init__(self, grid):
        self._grid = grid
        self.n_rows = len(grid)
        self.n_cols = len(grid[0])
    
    def transpose(self):
        return Grid([[self._grid[i][j] for i in range(self.n_rows)] for j in range(self.n_cols)])

    
class Solver:
    
    def solve(self, grid: Grid):
        row_result = self.rowsolve(grid._grid, grid.n_rows, grid.n_cols)
        gridT = grid.transpose()
        col_result_T = self.rowsolve(gridT._grid, gridT.n_rows, gridT.n_cols)
        col_result = Grid(col_result_T).transpose()._grid
        
        max_enemies = 0
        for i in range(grid.n_rows):
            for j in range(grid.n_cols):
                enemies = 0
                row_enemies = row_result[i][j]
                col_enemies = col_result[i][j]
                if row_enemies > 0:
                    enemies += row_enemies
                if col_enemies > 0:
                    enemies += col_enemies
                
                if enemies > max_enemies:
                    max_enemies = enemies
        return max_enemies
                
    def fill_row_counts(self, resultgrid, row_idx, ptr1, ptr2, count):
        for col_idx in range(ptr1, ptr2):
            if resultgrid[row_idx][col_idx] == 0:
                resultgrid[row_idx][col_idx] = count
    
    def rowsolve(self, grid, n_rows, n_cols):
        rowgrid = [[None for _ in range(n_cols)] for _ in range(n_rows)]
        for i in range(n_rows):
            row = grid[i]
            enemies = 0
            ptr = 0
            for j in range(n_cols):
                col = row[j]
                if col == CellContent.ENEMY:
                    enemies += 1
                    rowgrid[i][j] = -1
                elif col == CellContent.WALL:
                    self.fill_row_counts(rowgrid, i, ptr, j, enemies)
                    ptr = j+1
                    enemies = 0
                    rowgrid[i][j] = -1
                elif col == CellContent.EMPTY:
                    rowgrid[i][j] = 0
                    continue
            # check if last row was not a wall, then fill counts
            if n_cols > 0:
                if grid[i][n_cols-1] != CellContent.WALL:
                    self.fill_row_counts(rowgrid, i, ptr, n_cols, enemies)

        return rowgrid
        
    
class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        try:
            return Solver().solve(Grid(grid))
        except IndexError:
            return 0
        