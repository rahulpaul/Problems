""" https://leetcode.com/problems/decode-ways/

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""
from typing import *


CHARS = {i + 1: chr(ord('A') + i) for i in range(26)}


def decode(s: str, i: int, memo: Dict[int, int]):
    if i >= len(s):
        return 1

    if i in memo:
        return memo[i]

    n = 0
    n += decode(s, i + 1, memo)

    if i + 1 < len(s):
        v = int(f'{s[i]}{s[i+1]}')
        if 10 <= v <= 26:
            n += decode(s, i + 2, memo)

    memo[i] = n
    return n


class Solution:
    def numDecodings(self, s: str) -> int:
        return decode(s, 0, {})


def main():
    assert Solution().numDecodings("226") == 3
    assert Solution().numDecodings("2326") == 4


if __name__ == '__main__':
    main()

