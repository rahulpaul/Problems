"""https://leetcode.com/problems/sum-root-to-leaf-numbers/
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
def compute_number(trail: List[int]) -> int:
    result = 0
    for n in trail:
        result = result * 10 + n
    return result

def solve(node: TreeNode, trail: List[int]) -> int:
    if node is None:
        return 0
    
    new_trail = [*trail, node.val]
    if node.left is None and node.right is None:
        return compute_number(new_trail)
    
    sum_left, sum_right = 0, 0
    if node.left is not None:
        sum_left = solve(node.left, new_trail)
    if node.right is not None:
        sum_right = solve(node.right, new_trail)
    
    return sum_left + sum_right

        
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        return solve(root, [])
        