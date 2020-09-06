""" https://leetcode.com/problems/string-transforms-into-another-string/

Given two strings str1 and str2 of the same length, determine whether you can transform str1 into str2 by doing zero or more conversions.

In one conversion you can convert all occurrences of one character in str1 to any other lowercase English character.

Return true if and only if you can transform str1 into str2.

 

Example 1:

Input: str1 = "aabcc", str2 = "ccdee"
Output: true
Explanation: Convert 'c' to 'e' then 'b' to 'd' then 'a' to 'c'. Note that the order of conversions matter.
Example 2:

Input: str1 = "leetcode", str2 = "codeleet"
Output: false
Explanation: There is no way to transform str1 to str2.
"""

import random
import collections


def get_random_char():
    return chr(ord('a') + random.randint(0, 25))

    
def replace_cyclic_mappings(mappings):
    result = []
    for c1, c2_list in mappings.items():
        for c2 in c2_list:
            if (c2 in mappings) and (c1 in mappings[c2]):
                result.append((c1, c2))
                
    
    for tuple_ in result:
        c1, c2 = tuple_
        r = get_random_char()
        while r in tuple_:
            r = get_random_char()
        
        mappings[c1].add(r)
        if r not in mappings:
            mappings[r] = {c2}
        else:
            mappings[r].add(c2)
                
    
def get_map_options(str1: str, str2: str):
    # select first mismatch
    n = len(str1)
    options = {}
    for i in range(n):
        c1 = str1[i]
        c2 = str2[i]
        
        if c1 != c2:
            # replace c1 with c2
            if c1 not in options:
                options[c1] = {c2}
            else:
                options[c1].add(c2)
    
    replace_cyclic_mappings(options)
    return options
    
def can_convert(str1: str, str2: str) -> bool:
    if str1 == str2:
        return True
    
    q = collections.deque()
    visited = {str1}
    q.append(str1)
    
    while len(q) > 0:
        s = q.popleft()
        options = get_map_options(s, str2)
        for c_old, c_new_set in options.items():
            for c_new in c_new_set:
                s_new = s.replace(c_old, c_new)
                if s_new == str2:
                    return True
                if s_new not in visited:
                    print(s_new)
                    visited.add(s_new)
                    q.append(s_new)
    
    return False


def main():
    # s1 = "abcdefghijklmnopqrstuvwxyz"
    # s2 = "bcdefghijklmnopqrstuvwxyza"

    # s1 = "ab"
    # s2 = "ba"

    # s1 = "aabcc"
    # s2 = "ccdee"

    s1 = "aa"
    s2 = "bc"

    print(can_convert(s1, s2))


if __name__ == "__main__":
    main()
