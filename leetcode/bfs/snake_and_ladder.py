""" https://leetcode.com/problems/snakes-and-ladders/
"""

from typing import *
from queue import SimpleQueue


class Position:
    
    def __init__(self, current: int, trail: List[int]):
        self.current = current
        self.trail = trail
    
    def __str__(self):
        return ' -> '.join([*list(map(str, self.trail)), self.current])
    
    def n_moves(self):
        return len(self.trail)


class Board:
    
    def __init__(self, board: List[List[int]]):
        self.board = board
        self.N = len(board[0])
        self.end = self.N * self.N
    
    def get_value(self, position: int) -> int:
        i = (position - 1) % self.N
        j = (position - 1) // self.N
        row_index = self.N - j - 1
        col_index = i
        row = self.board[row_index]
        return row[col_index]

    def get_possible_next_moves(self, position: Position) -> List[Position]:
        positions = []
        trail = [*position.trail, position.current]
        for i in range(1, 7):
            n = position.current + i
            if n > self.end:
                break
                
            value = self.get_value(n)
            if value == -1:
                new_pos = Position(n, trail)
            else:
                new_pos = Position(value, trail)
            positions.append(new_pos)
        
        return positions
                

def solve(board: List[List[int]]):
    b = Board(board)
    start_position = Position(1, trail=[])
    q = SimpleQueue()
    visited = set()
    
    q.put(start_position)
    visited.add(start_position.current)
    
    while not q.empty():
        pos = q.get()
        next_positions = b.get_possible_next_moves(pos)
        for next_pos in next_positions:
            if next_pos.current in visited:
                continue
            if next_pos.current == b.end:
                return next_pos.n_moves()
            q.put(next_pos)
            visited.add(next_pos.current)
    
    return -1
    

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        return solve(board)


def main():
    board = [
        [-1,-1,19,10,-1],
        [2,-1,-1,6,-1],
        [-1,17,-1,19,-1],
        [25,-1,20,-1,-1],
        [-1,-1,-1,-1,15]
    ]

    print(Solution().snakesAndLadders(board))


if __name__ == '__main__':
    main()
