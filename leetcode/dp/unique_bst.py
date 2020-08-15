"""https://leetcode.com/problems/unique-binary-search-trees/


Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
 

Constraints:

1 <= n <= 19
"""
from typing import Dict


class Solver:
    
    def __init__(self):
        self.cache: Dict[int, int] = {}
        self.cache[0] = 1
            

    def solve(self, start: int, end: int) -> int:
        print(f'{start}-{end}')
        key = end - start
        
        if key in self.cache:
            return self.cache[key]
        
        _sum = 0
        for i in range(start, end + 1):
            # root = i
            left_subtree = 1 if i == start else self.solve(start, i-1)
            right_subtree = 1 if i == end else self.solve(i+1, end)
            _sum += left_subtree * right_subtree
        
        self.cache[key] = _sum
        return _sum
            


class Solution:
    def numTrees(self, n: int) -> int:
        return Solver().solve(1, n)


if __name__ == '__main__':
    Solver().solve(1, 3)