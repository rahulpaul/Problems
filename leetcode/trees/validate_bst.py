from typing import Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class InvalidBST(Exception):
    pass


def validate(node: TreeNode) -> Tuple[int, int]:
    if node is None:
        return None, None
    
    
    left_min, left_max = None, None
    right_min, right_max = None, None
    
    if node.left is not None:
        left_min, left_max = validate(node.left)
    if node.right is not None:
        right_min, right_max = validate(node.right)
    
    if left_max is not None and left_max >= node.val:
        raise InvalidBST()
    if right_min is not None and right_min <= node.val:
        raise InvalidBST()
    
    node_min = left_min if left_min is not None else node.val
    node_max = right_max if right_max is not None else node.val
    
    return node_min, node_max

        
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        try:
            validate(root)
            return True
        except InvalidBST:
            return False
        