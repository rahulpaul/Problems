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


class TrieNode:

    def __init__(self):
        self.children: Dict[str, 'TrieNode'] = dict()
        self.end_of_word = False

    @classmethod
    def of_words(cls, words: List[str]):
        root = cls()
        for word in words:
            root.add_word(word)
        return root

    def add_word(self, word: str):
        current = self
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]

        current.end_of_word = True

    def prefix_search(self, s):
        words = []

        current = self
        for i in range(len(s)):
            if current.end_of_word:
                words.append(s[:i])

            c = s[i]
            if c not in current.children:
                break

            current = current.children[c]
        else:
            if current.end_of_word:
                words.append(s)
        return words


def _word_break(s: str, root: TrieNode, sentence: List[str]):
    if len(s) == 0:
        return [sentence]

    sentences = []
    prefixes = root.prefix_search(s)

    for prefix in prefixes:
        sentences.extend(_word_break(s[len(prefix):], root, [*sentence, prefix]))

    return sentences


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        root = TrieNode.of_words(wordDict)
        sentences = _word_break(s, root, [])
        return [' '.join(sentence) for sentence in sentences]


def main():
    # s = 'catsanddog'
    # words = ["cat","cats","and","sand","dog"]

    s = "pineapplepenapple"
    words = ["apple", "pen", "applepen", "pine", "pineapple"]

    output = Solution().wordBreak(s, words)
    print(output)


if __name__ == '__main__':
    main()


