"""https://leetcode.com/problems/find-largest-value-in-each-tree-row/
"""


from queue import SimpleQueue


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solve(node):
    row_to_max_value = {}
    dfs_solve(node, 0, row_to_max_value)
    return row_to_max_value.values()
    


def dfs_solve(node, depth, row_to_max_value):
    if node is None:
        return
    
    if depth not in row_to_max_value or row_to_max_value[depth] < node.val:
        row_to_max_value[depth] = node.val
        
    dfs_solve(node.left, depth+1, row_to_max_value)
    dfs_solve(node.right, depth+1, row_to_max_value)

    
def bfs_solve(root):
    if root is None:
        return []
    
    row_to_max_value = {}
    q = SimpleQueue()
    q.put((root, 0))
    
    while not q.empty():
        node, depth = q.get()
        if depth not in row_to_max_value or row_to_max_value[depth] < node.val:
            row_to_max_value[depth] = node.val
        
        if node.left is not None:
            q.put((node.left, depth+1))
        
        if node.right is not None:
            q.put((node.right, depth+1))
    
    return row_to_max_value.values()

    
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        return solve(root)
        # return bfs_solve(root)
        