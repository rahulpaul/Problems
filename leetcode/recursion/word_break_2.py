"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence
where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
"""
from typing import List, Dict

from typing import *


class TrieNode:
    def __init__(self):
        self.data: Dict[str, 'TrieNode'] = {}
        self.is_word_end = False

    def add_word(self, word: str):
        node = self
        for c in word:
            if c not in node.data:
                node.data[c] = TrieNode()
            node = node.data[c]

        node.is_word_end = True

    @classmethod
    def of_words(cls, words: Iterable[str]):
        root = cls()
        for word in words:
            root.add_word(word)
        return root


    def search_prefixes(self, s: str) -> List[str]:
        prefixes = []
        trail = ''
        node = self
        for c in s:
            if node.is_word_end:
                prefixes.append(trail)
            try:
                node = node.data[c]
            except KeyError:
                break
            trail += c
        else:
            prefixes.append(s)
        return prefixes


def _break_to_words(s: str, i: int, trie: TrieNode, output: List[str], outputs: List[List[str]]):
    if i >= len(s):
        outputs.append(output)
        return

    prefixes = trie.search_prefixes(s[i:])
    if not prefixes:
        raise ValueError()

    for prefix in prefixes:
        output_new = [*output, prefix]
        try:
            _break_to_words(s, i + len(prefix), trie, output_new, outputs)
        except ValueError:
            pass


def break_to_words(s: str, words: Iterable[str]):
    trie = TrieNode.of_words(words)
    outputs = []
    _break_to_words(s, 0, trie, [], outputs)
    return [' '.join(output) for output in outputs]


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return break_to_words(s, wordDict)


def main():
    s = 'catsanddog'
    words = ["cat", "cats", "and", "sand", "dog"]

    output = Solution().wordBreak(s, words)
    print(output)

    s = "pineapplepenapple"
    words = ["apple", "pen", "applepen", "pine", "pineapple"]

    output = Solution().wordBreak(s, words)
    print(output)

    s = "catsandog"
    words = ["cats", "dog", "sand", "and", "cat"]
    output = Solution().wordBreak(s, words)
    print(output)
    

if __name__ == '__main__':
    main()


