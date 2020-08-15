""" https://leetcode.com/problems/unique-binary-search-trees-ii/

Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
 

Constraints:

0 <= n <= 8
"""
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    
def solve(i: int, j: int) -> List[TreeNode]:
    if i > j:
        return []
    if i == j:
        return [TreeNode(val=i)]
    
    result = []
    for x in range(i, j+1):
        left_subtrees = solve(i, x-1)
        right_subtrees = solve(x+1, j)
        if not left_subtrees:
            for node in right_subtrees:
                root = TreeNode(val=x)
                root.right = node
                result.append(root)
        elif not right_subtrees:
            for node in left_subtrees:
                root = TreeNode(val=x)
                root.left = node
                result.append(root)
        else:
            for left_root in left_subtrees:
                for right_root in right_subtrees:
                    root = TreeNode(val=x)
                    root.left = left_root
                    root.right = right_root
                    result.append(root)
    return result        


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        return solve(1, n)
        
        