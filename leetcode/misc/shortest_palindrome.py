""" https://leetcode.com/problems/shortest-palindrome/

Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

Example 1:

Input: "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: "abcd"
Output: "dcbabcd"
"""

def is_palindrome(s: str, offset: int) -> bool:
    n = len(s)
    p1 = 0
    p2 = n-1-offset
    
    while p1 < p2:
        if s[p1] == s[p2]:
            p1 += 1
            p2 += -1
        else:
            break
    
    return p1 >= p2

def shortest_palindrome(s: str) -> str:
    for offset in range(len(s)):
        if is_palindrome(s, offset):
            break
    
    palindrome = ''.join(reversed(s[len(s) - offset: len(s)])) + s
    print(palindrome)
    return palindrome


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        return shortest_palindrome(s)


def main():
    assert shortest_palindrome("aacecaaa") == "aaacecaaa"
    assert shortest_palindrome("abcd") == "dcbabcd"


if __name__ == "__main__":
    main()

"""
offset in [0, 1, 2]

offset = 2

|
abcd
 |

"""