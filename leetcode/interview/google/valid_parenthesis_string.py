""" https://leetcode.com/problems/3sum/

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
"""

from typing import *

"""

0 1 2 3 4 5 6 7 8 9 10 11
( ( ( ( ( ( * * * * ) ( ) ) )  )  )

( ( ( ( ( ( ) ( ) ( ) ( ) ) ) ) )

1,1
2,2
3,3
4,4
5,5
6,6
5,7
4,8
3,9
2,10
1,9
2,10
1,9
0,8
0,7
0,6
0,5

               -5  -4  -5 -4 -3 -2 -1

6 -> [-5, ]
"""



OPEN_BRACKET = "("
CLOSE_BRACKET = ")"


def check_valid(s: str, i: int, bal: int):
    if bal < 0:
        return False

    if i >= len(s):
        return True

    while i < len(s):
        c = s[i]
        if c == OPEN_BRACKET:
            bal += 1
            i += 1
        elif c == CLOSE_BRACKET:
            bal += -1
            i += 1
            if bal < 0:
                return False
        else:
            return check_valid(s, i + 1, bal) or check_valid(s, i + 1, bal + 1) or check_valid(s, i + 1, bal - 1)

    return bal == 0


def check_valid_greedy(s: str):
    lo = hi = 0
    for c in s:
        if c == '(':
            lo += 1
            hi += 1
        elif c == ')':
            lo += -1
            hi += -1
        else:
            lo += -1
            hi += 1

        if hi < 0:
            return False

        lo = max(lo, 0)

    return lo == 0


class Solution:
    def checkValidString(self, s: str) -> bool:
        return check_valid(s, 0, 0)

def main():
    print(Solution().checkValidString("****"))
    print(Solution().checkValidString("((((((****)()))))"))
    print(Solution().checkValidString("*(("))


if __name__ == "__main__":
    main()
