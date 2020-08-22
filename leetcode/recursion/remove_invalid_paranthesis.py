""" https://leetcode.com/problems/remove-invalid-parentheses/

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]

"""

from dataclasses import dataclass
from typing import Optional, Set

OPEN_BRACKET = '('
CLOSE_BRACKET = ')'


@dataclass
class _Result:
    removal_count: Optional[int]
    valids: Set[str]
    

def add_expr(best: _Result, expr: str, removal_count: int):
    if best.removal_count is None:
        best.removal_count = removal_count
        best.valids.add(''.join(expr))
    elif best.removal_count == removal_count:
        best.valids.add(''.join(expr))
    elif best.removal_count > removal_count:
        best.valids.clear()
        best.removal_count = removal_count
        best.valids.add(''.join(expr))

        
def _valid_expressions(s: str, start: int, expression: List[str], open_count: int, close_count: int, removal_count: int, result: _Result):
    if start >= len(s):
        if open_count == close_count:
            add_expr(result, expression, removal_count)
        return
    
    c = s[start]
    if c == OPEN_BRACKET:
        # take the bracket
        _valid_expressions(s, start+1, [*expression, c], open_count+1, close_count, removal_count, result)
        
        # exclude
        _valid_expressions(s, start+1, [*expression], open_count, close_count, removal_count+1, result)
    elif c == CLOSE_BRACKET:
        # take the bracket
        if close_count < open_count:
            _valid_expressions(s, start+1, [*expression, c], open_count, close_count+1, removal_count, result)
        
        # exclude
        _valid_expressions(s, start+1, [*expression], open_count, close_count, removal_count+1, result)
    else:
        _valid_expressions(s, start+1, [*expression, c], open_count, close_count, removal_count, result)
        


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        result = _Result(removal_count=None, valids=set())
        _valid_expressions(s, 0, [], 0, 0, 0, result)
        return list(result.valids)
            
