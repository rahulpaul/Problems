""" https://leetcode.com/problems/word-ladder-ii/

Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, 
such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

"""

from collections import defaultdict
from typing import List, Dict, Set


class _TransformationTrail:
    def __init__(self, seq: List[str], words_used: Set[str]):
        self.seq = seq
        self.words_used = words_used
    
    def new_trail_with_word(self, word: str):
        seq = [*self.seq, word]
        used = {*self.words_used, word}
        return _TransformationTrail(seq, used)
        
    def contains(self, word) -> bool:
        return word in self.words_used
    
    def __len__(self):
        return len(self.seq)


def _is_transformable(word1, word2):
    _diff = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            _diff += 1
        if _diff > 1:
            return False
    return _diff == 1


def _transform_word_list(word_list, n) -> Dict[str, List[str]]:
    word_to_list = defaultdict(list)
    word_list = [word for word in word_list if len(word) == n]
    for word1 in word_list:
        for word2 in word_list:
            if _is_transformable(word1, word2):
                word_to_list[word1].append(word2)
    return word_to_list


class Solver:
    def __init__(self, word_list: List[str], n: int):
        self.min_length = None
        self.solutions = []
        self.word_to_transformations = _transform_word_list(word_list, n)
    
    def add_solution(self, trail: _TransformationTrail):
        if self.min_length is None:
            self.min_length = len(trail)
            
        if self.min_length == len(trail):
            self.solutions.append(trail.seq)
        elif self.min_length > len(trail):
            self.min_length = len(trail)
            self.solutions.clear()
            self.solutions.append(trail.seq)
        
    def solve(self, begin_word: str, end_word: str, trail: _TransformationTrail):
        if begin_word == end_word:
            self.add_solution(trail)
            return
        
        if (self.min_length is not None) and (len(trail) >= self.min_length):
            return
        
        possible_transformations = self.word_to_transformations[begin_word]
        for word in possible_transformations:
            if not trail.contains(word):
                new_trail = trail.new_trail_with_word(word)
                self.solve(word, end_word, new_trail)


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        
        if len(beginWord) != len(endWord):
            return []
        
        n = len(beginWord)
        solver = Solver([*wordList, beginWord], n)
        solver.solve(beginWord, endWord, _TransformationTrail([beginWord], {beginWord}))
        return solver.solutions
        
