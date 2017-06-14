import sys
from contextlib import contextmanager


####################################################################
#########################Problem Statement##########################
####################################################################


"""
Given an array with  elements, can you sort this array in ascending order using only one of the following operations?

1) Swap two elements.
2) Reverse one sub-segment.

Input Format 
The first line contains a single integer, , which indicates the size of the array. 
The next line contains  integers separated by spaces.

n  
d1 d2 ... dn  
Constraints 
 
  
All  are distinct.

Output Format 
1. If the array is already sorted, output yes on the first line. You do not need to output anything else.

If you can sort this array using one single operation (from the two permitted operations) then output yes on the first line and then:

a. If you can sort the array by swapping  and , output swap l r in the second line.  and  are the indices of the elements to be swapped, assuming that the array is indexed from  to .

b. Else if it is possible to sort the array by reversing the segment , output reverse l r in the second line. and  are the indices of the first and last elements of the subsequence to be reversed, assuming that the array is indexed from  to .

 represents the sub-sequence of the array, beginning at index  and ending at index , both inclusive.

If an array can be sorted by either swapping or reversing, stick to the swap-based method.

2. If you cannot sort the array in either of the above ways, output no in the first line.


Sample Input #1

2  
4 2  

Sample Output #1

yes  
swap 1 2

Sample Input #2

3
3 1 2

Sample Output #2

no

Sample Input #3

6
1 5 4 3 2 6

Sample Output #3

yes
reverse 2 5


Explanation 
For #1, you can both swap(1, 2) and reverse(1, 2), but if you can sort the array using swap, output swap only. 
For #2, it is impossible to sort by one single operation (among those permitted). 
For #3, you can reverse the sub-array d[2...5] = "5 4 3 2", then the array becomes sorted.
"""


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
