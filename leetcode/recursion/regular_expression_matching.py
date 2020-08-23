""" https://leetcode.com/problems/regular-expression-matching/

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""

def is_match(s: str, p: str, ps=0, pp=0) -> bool:
    if ps >= len(s) and pp >= len(p):
        return True
    
    if ps >= len(s):
        return False
    
    if pp >= len(p):
        return False
    
    if s[ps] == p[pp] or p[pp] == '.':
        return is_match(s, p, ps+1, pp+1)
    
    if p[pp] =='*':
        # cases:
        # 1. no repeataion case
        # 2. repeatation
        
        if p[pp-1] == s[ps] or p[pp-1] == '.':
            return is_match(s, p, ps+1, pp) or is_match(s, p, ps, pp+1) or is_match(s, p, ps+1, pp+1)
        else:
            return is_match(s, p, ps, pp+1)
    
    if pp+1 < len(p) and p[pp+1] == '*':
        # no repeatation case
        return is_match(s, p, ps, pp+2)
    
    return False


def main():
    s = "aa"
    p = "a"
    assert not is_match(s, p)

    s = "aa"
    p = "a*"
    assert is_match(s, p)

    s = "ab"
    p = ".*"
    assert is_match(s, p)

    s = "aab"
    p = "c*a*b"
    assert is_match(s, p)

    s = "mississippi"
    p = "mis*is*p*."
    assert not is_match(s, p)


if __name__ == "__main__":
    main()
