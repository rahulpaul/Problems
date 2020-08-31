""" https://leetcode.com/problems/rearrange-string-k-distance-apart/

Given a non-empty string s and an integer k, rearrange the string such that the same characters are at least distance k from each other.

All input strings are given in lowercase letters. If it is not possible to rearrange the string, return an empty string "".

Example 1:

Input: s = "aabbcc", k = 3
Output: "abcabc" 
Explanation: The same letters are at least distance 3 from each other.
Example 2:

Input: s = "aaabc", k = 3
Output: "" 
Explanation: It is not possible to rearrange the string.
Example 3:

Input: s = "aaadbbcc", k = 2
Output: "abacabcd"
Explanation: The same letters are at least distance 2 from each other.
"""

import heapq
from typing import *
from collections import defaultdict


class EmptyHeap(Exception):
    pass


class MaxHeap:
    def __init__(self, func):
        self.func = func
        self.entries = []
        
    def push(self, val):
        key = -1 * self.func(val)
        heapq.heappush(self.entries, (key, val))
    
    def pop(self):
        if not self.entries:
            raise EmptyHeap()
        key, val = heapq.heappop(self.entries)
        return val
    
    def __len__(self) -> int:
        return len(self.keys)


def _char_counts(s: str) -> Dict[str, int]:
    counts = defaultdict(int)
    for char in s:
        counts[char] += 1
    return counts


def _rearrange(s: str, k: int):
    char_counts = _char_counts(s)
    items = []
    for char, count in char_counts.items():
        items.append((count, char))
        
    heap = MaxHeap(func=lambda x: x[0])
    deffered_list = []
    
    for item in items:
        heap.push(item)
    
    chars = []
    while True:
        for _ in range(k):
            try:
                count, char = heap.pop()
                chars.append(char)
        
                if count - 1 > 0:
                    deffered_list.append((count-1, char))
            except EmptyHeap:
                if deffered_list:
                    return ""
                else:
                    return ''.join(chars)
        
        for item in deffered_list:
            heap.push(item)
        
        deffered_list.clear()
        

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        return _rearrange(s, k)


def main():
    s = "aabbcc"
    k = 3
    output = _rearrange(s, k)
    print(output)
    assert output == "abcabc"

    s = "aaabc"
    k = 3
    output = _rearrange(s, k)
    print(output)
    assert output == ""

    s = "aaadbbcc"
    k = 2
    output = _rearrange(s, k)
    print(output)
    assert output in ["abacabcd", "abcadbca"]


if __name__ == "__main__":
    main()
