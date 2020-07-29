"""
Given a string, find the length of the longest substring without repeating characters.

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3.

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

from typing import List, Dict


class CharAlreadyExists(Exception):
    pass


class Result:
    
    def __init__(self):
        self.chars: List[str] = list()
        self.data: Dict[str, int] = dict()
    
    @classmethod
    def from_sequence(cls, seq: List[str]):
        inst = cls()
        for ch in seq:
            inst.add_char(ch)
        return inst
    
    def add_char(self, c: str):
        if c in self.data:
            raise CharAlreadyExists()
        
        self.data[c] = len(self.chars)
        self.chars.append(c)
        
    def get_sequence_from(self, c: str):
        index = self.data[c]
        return ''.join(x for x in self.chars[index+1:])
    
    def __len__(self):
        return len(self.chars)


class Solution:
    
    def __init__(self):
        self.best_result = None
    
    def update_result_if_required(self, result):
        if len(self.best_result) < len(result):
            self.best_result = result
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        self.best_result = result = Result()
        for ch in s:
            try:
                result.add_char(ch)
            except CharAlreadyExists:
                self.update_result_if_required(result)
                
                right_seq = result.get_sequence_from(ch)
                result = Result.from_sequence(right_seq)
                result.add_char(ch)
        
        self.update_result_if_required(result)
        return len(self.best_result)
                
            
        