import sys
from typing import List
from collections import deque, Counter


def detect_frauds(transactions: List[int], duration: int):
    mintxn, maxtxn = sys.maxsize, -1
    for txn in transactions:
        if txn < mintxn:
            mintxn = txn
        if txn > maxtxn:
            maxtxn = txn

    bin_size = 1
    min_window = mintxn // bin_size
    max_window = maxtxn // bin_size

    bin_count = max_window - min_window + 1
    bin_list: List[Counter] = [Counter() for _ in range(bin_count)]
    bin_item_counts = [0 for _ in range(bin_count)]

    history = deque()

    c = ((duration + 1) // 2, ) if duration % 2 != 0 else (duration//2, duration//2 + 1)
    fraud_count = 0

    for txn in transactions:

        txn_bin_index = txn // bin_size - min_window

        if len(history) < duration:
            history.append(txn)
            bin_list[txn_bin_index][txn] += 1
            bin_item_counts[txn_bin_index] += 1
            continue

        value = txn / 2
        value_bin_index = value // bin_size - min_window
        left, right = 0, 0

        for index, item_count in enumerate(bin_item_counts):
            right = left + item_count
            if left < c[0] < right:
                # this bin contains the median
                if value_bin_index > index:
                    fraud_count += 1
                    break
                if value_bin_index == index:
                    # both value and median is in this bin
                    # we can't decide if fraud or not, need to compute the median
                    # print("Computing median")
                    counter = bin_list[index]
                    sorted_keys = sorted(counter.keys())
                    median = -1

                    for key in sorted_keys:
                        left += counter[key]
                        if left > c[0]:
                            median = key
                            break
                        elif left == c[0] and len(c) == 1:
                            median = key
                            break
                        elif left == c[0] and len(c) == 2:
                            next_bin_counter = bin_list[index + 1]
                            min_key = min(next_bin_counter.keys())
                            median = (key + min_key) / 2
                            break

                    if value >= median:
                        fraud_count += 1
                    break

            elif c[0] == right:
                counter = bin_list[index]
                median = -1
                if len(c) == 1:
                    median = max(counter.keys())
                elif len(c) == 2:
                    counter2 = bin_list[index + 1]
                    m1 = max(counter.keys())
                    m2 = min(counter2.keys())
                    median = (m1 + m2) / 2

                if value >= median:
                    fraud_count += 1

                break

            elif value_bin_index == index:
                break

            left = right

        # remove from history
        item_to_remove = history.popleft()
        item_to_remove_index = item_to_remove // bin_size - min_window
        bin_item_counts[item_to_remove_index] += -1
        item_to_remove_counter = bin_list[item_to_remove_index]
        item_to_remove_counter[item_to_remove] += -1

        # add to history
        history.append(txn)
        bin_list[txn_bin_index][txn] += 1
        bin_item_counts[txn_bin_index] += 1

    return fraud_count


def main():
    n, d = (int(x) for x in input().split(' '))
    transactions = [int(x) for x in input().split(' ')]
    print(detect_frauds(transactions, d))


if __name__ == "__main__":
    with open('fraud_activity.txt') as file:
        sys.stdin = file
        main()
    # print(detect_frauds([2, 3, 4, 2, 3, 6, 8, 4, 5], 5))
