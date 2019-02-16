import sys
import math
from typing import List
from collections import deque, Counter


class FraudDetector:

    def __init__(self, transactions):
        self.transactions = transactions
        self.bin_size = 20

        mintxn, maxtxn = sys.maxsize, -1
        for txn in transactions:
            if txn < mintxn:
                mintxn = txn
            if txn > maxtxn:
                maxtxn = txn

        self.min_window = int(math.floor(mintxn / self.bin_size))
        self.max_window = int(math.ceil(maxtxn / self.bin_size))

        self.bin_count = self.max_window - self.min_window + 1
        self.bin_list: List[Counter] = [Counter() for _ in range(self.bin_count)]
        self.bin_item_counts = [0 for _ in range(self.bin_count)]

        self.history = deque()

    def compute_bin_index(self, value):
        # return int(math.ceil(value / self.bin_size)) - self.min_window
        return value // self.bin_size - self.min_window

    def add_to_history(self, transaction):
        self.history.append(transaction)
        transaction_bin_index = self.compute_bin_index(transaction)
        self.bin_list[transaction_bin_index][transaction] += 1
        self.bin_item_counts[transaction_bin_index] += 1

    def pop_from_history(self):
        transaction = self.history.popleft()
        transaction_bin_index = self.compute_bin_index(transaction)
        self.bin_list[transaction_bin_index][transaction] += -1
        self.bin_item_counts[transaction_bin_index] += -1

    def detect_frauds(self, duration: int):

        c = ((duration + 1) // 2, ) if duration % 2 != 0 else (duration//2, duration//2 + 1)
        fraud_count = 0
        frauds = []

        for txn_index, txn in enumerate(self.transactions):

            if len(self.history) < duration:
                self.add_to_history(txn)
                continue

            value = txn / 2
            value_bin_index = self.compute_bin_index(value)
            left, right = 0, 0

            for index, item_count in enumerate(self.bin_item_counts):
                right = left + item_count
                if left < c[0] < right:
                    # this bin contains the median
                    if value_bin_index > index:
                        fraud_count += 1
                        frauds.append(txn_index)
                        break
                    if value_bin_index == index:
                        # both value and median is in this bin
                        # we can't decide if fraud or not, need to compute the median
                        # print("Computing median")
                        counter = self.bin_list[index]
                        sorted_keys = sorted(counter.keys())
                        median = -1

                        for key_index, key in enumerate(sorted_keys):
                            left += counter[key]
                            if left > c[0]:
                                median = key
                                break
                            elif left == c[0]:
                                if len(c) == 1:
                                    median = key
                                    break
                                elif len(c) == 2:
                                    next_key = sorted_keys[key_index + 1]
                                    median = (key + next_key) / 2
                                    break

                        if value >= median:
                            fraud_count += 1
                            frauds.append(txn_index)
                        break

                elif c[0] == right:
                    counter = self.bin_list[index]
                    median = -1
                    if len(c) == 1:
                        median = max(counter.keys())
                    elif len(c) == 2:
                        counter2 = self.bin_list[index + 1]
                        m1 = max(counter.keys())
                        m2 = min(counter2.keys())
                        median = (m1 + m2) / 2

                    if value >= median:
                        fraud_count += 1
                        frauds.append(txn_index)

                    break

                elif value_bin_index == index:
                    break

                left = right

            # remove from history
            self.pop_from_history()

            # add to history
            self.add_to_history(txn)

        # print(frauds)
        return fraud_count


def main():
    n, d = (int(x) for x in input().split(' '))
    transactions = [int(x) for x in input().split(' ')]

    fraud_detector = FraudDetector(transactions)
    print(fraud_detector.detect_frauds(d))


if __name__ == "__main__":
    with open('fraud_activity.txt') as file:
        sys.stdin = file
        main()
    # print(detect_frauds([2, 3, 4, 2, 3, 6, 8, 4, 5], 5))
