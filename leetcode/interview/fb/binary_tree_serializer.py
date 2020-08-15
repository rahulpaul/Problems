import json
from enum import Enum
from queue import SimpleQueue


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class NodeMarker(Enum):
    LEFT = 0
    RIGHT = 1


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        """
        current_row = 0
        serialized = []
        q = SimpleQueue()
        q.put((root, current_row))
        while not q.empty():
            node, row = q.get()
            if current_row != row:
                serialized.append(None)
                current_row = row

            serialized.append(self._serialized_node(node))

            if self._has_left(node):
                q.put((node.left, row + 1))

            if self._has_right(node):
                q.put((node.right, row + 1))

        return json.dumps(serialized)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        """
        serialized = json.loads(data)
        last_row_iter = None
        next_row = []
        root = None
        for item in serialized:
            if item is not None:
                val, has_left, has_right = item
                has_left = has_left == '1'
                has_right = has_right == '1'
                node = TreeNode(val)
                if root is None:
                    root = node
                if has_left:
                    next_row.append((node, NodeMarker.LEFT))
                if has_right:
                    next_row.append((node, NodeMarker.RIGHT))

                if last_row_iter is not None:
                    parent, marker = next(last_row_iter)
                    if marker == NodeMarker.LEFT:
                        parent.left = node
                    else:
                        parent.right = node

            else:
                last_row_iter = iter(next_row)
                next_row = []

        return root

    def _has_left(self, node):
        return node.left is not None

    def _has_right(self, node):
        return node.right is not None

    def _serialized_node(self, node):
        bool_str = lambda bv: '1' if bv else '0'
        return [node.val, bool_str(self._has_left(node)), bool_str(self._has_right(node))]



def main():
    root_copy = root = TreeNode(1)
    l = TreeNode(2)
    r = TreeNode(3)
    root.left = l
    root.right = r
    root = r
    l = TreeNode(4)
    r = TreeNode(5)
    root.left = l
    root.right = r

    codec = Codec()
    data = codec.serialize(root_copy)
    root = codec.deserialize(data)

    assert root.left.val == 2
    assert root.right.val == 3

    root = root.right
    assert root.left.val == 4
    assert root.right.val == 5


if __name__ == '__main__':
    main()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))