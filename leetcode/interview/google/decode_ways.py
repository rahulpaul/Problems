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
    
    if s[i] == '0':
        return 0
    
    if i == len(s) - 1:
        return 1

    if i in memo:
        return memo[i]

    n = 0
    n += decode(s, i + 1, memo)
    
    v = int(f'{s[i]}{s[i+1]}')
    if 10 <= v <= 26:
        n += decode(s, i + 2, memo)

    memo[i] = n
    return n

"""

memo = {1: [BF, Z], 2: [F]}

 s = "226"
 i = 0

 c1 = 2
 v1 = B

 decodings_ = [BBF, BZ]

 c2 = 22
 v2 = V
 decodings = [BBF, BZ, VF]

    i = 1
    c1 = 2
    v1 = B

    decodings_ = [BF]
    c2 = 26
    v2 = Z

    decodings_ = [BF, Z]

        i = 2
        c1 = 6
        v1 = F

"""

def decodings(s: str, i: int, memo: Dict[int, List[str]]):
    if i >= len(s):
        return ['']

    c1 = int(s[i])
    if c1 == 0:
        return []
    
    if i in memo:
        return memo[i]

    v1 = CHARS[c1]

    if i == len(s) - 1:
        memo[i] = [v1]
        return memo[i]

    _decodings = [f'{v1}{x}' for x in decodings(s, i+1, memo)]

    c2 = int(s[i:i+2])
    if 10 <= c2 <= 26:
        v2 = CHARS[c2]
        _decodings.extend([f'{v2}{x}' for x in decodings(s, i+2, memo)])
    
    memo[i] = _decodings
    return _decodings


class Solution:
    def numDecodings(self, s: str) -> int:
        return decode(s, 0, {})
    
    def decodings(self, s: str) -> List[str]:
        return decodings(s, 0, {})
        


def main():
    assert Solution().numDecodings("226") == 3
    assert Solution().numDecodings("2326") == 4

    assert len(Solution().decodings("226")) == 3
    assert len(Solution().decodings("2326")) == 4


if __name__ == '__main__':
    main()

