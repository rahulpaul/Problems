import sys
from typing import NamedTuple


class Entry(NamedTuple):
    price: int
    index: int


def compute_min_loss(prices):
    sorted_price_entries = [Entry(p, i) for i, p in enumerate(prices)]
    sorted_price_entries.sort()

    min_loss = sys.maxsize
    for index, entry in enumerate(sorted_price_entries):
        buy_price, buy_index = entry
        for i in range(index - 1, -1, -1):
            sell_price, sell_index = sorted_price_entries[i]
            if sell_index > buy_index:
                loss = -1 * (sell_price - buy_price)
                min_loss = min(loss, min_loss)
                break
    return min_loss


def main():
    _ = input()
    prices = [int(x) for x in input().split(' ')]
    print(compute_min_loss(prices))


if __name__ == '__main__':
    print(compute_min_loss([5, 10, 3]))
