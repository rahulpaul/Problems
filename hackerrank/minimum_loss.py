class Node:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def walk_inorder(self):
        if self.left:
            yield from self.left.walk_inorder()
        yield self.data
        if self.right:
            yield from self.right.walk_inorder()


def add_data(root: Node, data):
    if root is None:
        return Node(data)
    if data == root.data:
        # data is already present in the tree, no need to add
        return root

    if data < root.data:
        root.left = add_data(root.left, data)

    if data > root.data:
        root.right = add_data(root.right, data)

    return root


def compute_min_loss(prices):
    min_loss = {}
    prices_bst: Node = None
    for sell_year, sell_price in enumerate(prices):
        if prices_bst:
            for buy_price in prices_bst.walk_inorder():
                if buy_price < sell_price:
                    continue
                min_loss[sell_year] = -1 * (sell_price - buy_price)
                break

        prices_bst = add_data(prices_bst, sell_price)

    return min(min_loss.values())


def main():
    n = input()
    prices = [int(x) for x in input().split(' ')]
    print(compute_min_loss(prices))


if __name__ == '__main__':
    print(compute_min_loss([5, 10, 3]))
