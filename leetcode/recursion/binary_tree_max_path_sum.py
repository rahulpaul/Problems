""" https://leetcode.com/problems/binary-tree-maximum-path-sum/

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""


from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def _max_gain(node: TreeNode) -> Tuple[int, int]:
	if not node:
		return 0, 0
	
	left_max_gains = _max_gain(node.left)
	right_max_gains = _max_gain(node.right)
	
	this_max_gain_as_child = node.val + max(left_max_gains[0], right_max_gains[0])
	this_max_gain_as_root = node.val + left_max_gains[0] + right_max_gains[0]
	overall_max_gain = max(left_max_gains[1], right_max_gains[1], this_max_gain_as_root, this_max_gain_as_child)
	
	return this_max_gain_as_child, overall_max_gain


def max_gain(root: TreeNode) -> int:
    return _max_gain(root)[1]
