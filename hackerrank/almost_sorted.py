import sys
from contextlib import contextmanager


def solve(array):
    if len(array) < 2:
        # array has only one element, its already sorted
        return 'yes', None

    diff_array = [array[i + 1] - array[i] for i in range(0, len(array) - 1)]
    negative_diff_indices = [i for i, x in enumerate(diff_array) if x < 0]
    # print(diff_array)
    # print(negative_diff_indices)

    if len(negative_diff_indices) == 0:
        # array is already sorted
        # print('case 1')
        return 'yes', None
    elif len(negative_diff_indices) == 1:
        # check swap
        # print('case 2')
        x1, x2 = negative_diff_indices[0], negative_diff_indices[0] + 1
        with swap(array, x1, x2):
            if is_sorted(array, x1 - 1, x2 + 1):
                return 'yes', ('swap', x1, x2)
    elif len(negative_diff_indices) == 2:
        # check with swap
        # print('case 3')
        x1, x2 = negative_diff_indices[0], negative_diff_indices[1] + 1
        with swap(array, x1, x2):
            if is_sorted(array, x1 - 1, x1 + 1) and is_sorted(array, x2 - 1, x2 + 1):
                return 'yes', ('swap', x1, x2)
    else:
        # check with reverse
        # print('case 4')
        if negative_diff_indices == list(range(negative_diff_indices[0], negative_diff_indices[0] + len(negative_diff_indices))):
            x1, x2 = negative_diff_indices[0], negative_diff_indices[-1] + 1
            with reverse_subsequence(array, x1, x2):
                if is_sorted(array, x1 - 1, x2 + 1):
                    return 'yes', ('reverse', x1, x2)

    return 'no', None


def is_sorted(array, low, high):
    """Check if the sunsequence of the array from low to high is sorted, both inclusive"""
    low = max(0, low)
    high = min(len(array) - 1, high)
    diff_sign = [array[i + 1] - array[i] > 0 for i in range(low, high)]
    return all(diff_sign)


@contextmanager
def swap(array, i, j):

    def _swap():
        array[i], array[j] = array[j], array[i]

    try:
        _swap()
        yield
    finally:
        _swap()


@contextmanager
def reverse_subsequence(array, i, j):
    try:
        original = array[i:j + 1]
        array[i:j + 1] = list(reversed(original))
        yield
    finally:
        array[i:j + 1] = original


if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())
    inputarray = [int(x) for x in sys.stdin.readline().rstrip().split()]
    bool_result, result = solve(inputarray)
    print(bool_result)
    if result:
        operation, x1, x2 = result
        print(operation, x1 + 1, x2 + 1)
