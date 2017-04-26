import sys
from bisect import bisect_right


####################################################################
#########################Problem Statement##########################
####################################################################

"""
Given a word w, rearrange the letters of w to construct another word in such a way that it is lexicographically greater than w.
In case of multiple possible answers, find the lexicographically smallest one among them.

Input Format

The first line of input contains n, the number of test cases. Each of the next n lines contains w.

Constraints:
Will contain only lower-case English letters.

Output Format

For each testcase, output a string lexicographically bigger than w in a separate line.
In case of multiple possible answers, print the lexicographically smallest one, and if no answer exists, print no answer.

Sample Input

5
ab
bb
hefg
dhck
dkhc
Sample Output

ba
no answer
hegf
dhkc
hcdk
"""


def solve(seq):
    if len(seq) <= 1:
        raise ValueError

    right_segment = list()
    for i in range(len(seq) - 1, -1, -1):
        pivot_item = seq[i]
        try:
            index = find_gt_index(right_segment, pivot_item)
            pivot_item, right_segment[index] = right_segment[index], pivot_item
            solution = ''.join((seq[:i], pivot_item, ''.join(right_segment)))
            return solution
        except ValueError:
            # there are no items to the right of i that is gt seq[i]
            # move seq[i] to the end
            right_segment.append(pivot_item)
    raise ValueError


def find_gt_index(a, x):
    """Find leftmost index that contains a value greater than x"""
    i = bisect_right(a, x)
    if i < len(a):
        return i
    raise ValueError


def print_solution(seq):
    try:
        print(solve(seq))
    except ValueError:
        print('no answer')


if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())
    for _ in range(n):
        seq = sys.stdin.readline().rstrip()
        print_solution(seq)
