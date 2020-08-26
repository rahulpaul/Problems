from typing import List, Set
from collections import deque


def _decode_order(words: List[str], i: int, orders: List[str]):
    if len(words) < 2:
        # no ordering can be detected
        return
    letter_to_words = {}
    for word in words:
        if len(word) <= i:
            continue

        letter = word[i]
        if letter not in letter_to_words:
            letter_to_words[letter] = [word]
        else:
            letter_to_words[letter].append(word)

    order_ = letter_to_words.keys()

    if len(order_) > 1:
        orders.append(''.join(order_))

    for words in letter_to_words.values():
        _decode_order(words, i + 1, orders)


def _break_into_pairs(orders: List[str]) -> Set[str]:
    pairs = set()
    for order_ in orders:
        for i in range(len(order_) - 1):
            pairs.add(order_[i: i + 2])
    return pairs


def _get_predecessor(pair, pairs):
    c = pair[0]
    for p in pairs:
        if p[1] == c:
            return p


def _get_successor(pair, pairs):
    c = pair[1]
    for p in pairs:
        if p[0] == c:
            return p


def decode_order(words):
    orders = []
    _decode_order(words, 0, orders)

    # break up into tuples
    pairs = _break_into_pairs(orders)
    p = next(iter(pairs))

    ordered_pairs = deque([p])
    while True:
        p = _get_predecessor(p, pairs)
        if p:
            ordered_pairs.appendleft(p)
        else:
            break
        

    p = ordered_pairs[-1]
    while p:
        p = _get_successor(p, pairs)
        if p:
            ordered_pairs.append(p)
        else:
            break

    output = [p[0] for p in ordered_pairs]
    output.append(ordered_pairs[-1][1])
    return ''.join(output)


def main():
    input_ = ["wrt", "wrf", "er", "ett", "rftt"]
    print(decode_order(input_))


if __name__ == "__main__":
    main()

