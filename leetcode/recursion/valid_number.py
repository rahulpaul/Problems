""" https://leetcode.com/problems/valid-number/

Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. However, here is a list of characters that can be in a valid decimal number:

Numbers 0-9
Exponent - "e"
Positive/negative sign - "+"/"-"
Decimal point - "."
Of course, the context of these characters also matters in the input.
"""

_DIGITS = {str(x) for x in range(10)}
_SIGNS = {'+', '-'}
_POINT = '.'
_EXPONENT = 'e'

_ALL_ALLOWED_CHARS = {*_DIGITS, *_SIGNS, _POINT, _EXPONENT}
_NON_EXPONENTS = {*_DIGITS, *_SIGNS, _POINT}
_SIGNED_DIGITS = {*_DIGITS, *_SIGNS}
_DECIMALS = {*_DIGITS, _POINT}


def is_number(s: str, allowed_chars):
    # assumption s does not have any leading or trailing spaces
    if len(s) == 0:
        return False

    if _EXPONENT in allowed_chars:
        parts = s.split(_EXPONENT)
        if len(parts) == 1:
            return is_number(parts[0], _NON_EXPONENTS)
        elif len(parts) == 2:
            return is_number(parts[0], _NON_EXPONENTS) and is_number(parts[1], _SIGNED_DIGITS)
        else:
            return False

    if _SIGNS.issubset(allowed_chars):
        if s[0] in _SIGNS:
            return is_number(s[1:], allowed_chars - _SIGNS)
        else:
            return is_number(s, allowed_chars - _SIGNS)

    if _POINT in allowed_chars:
        parts = s.split(_POINT)
        if len(parts) == 1:
            return is_number(parts[0], _DIGITS)
        elif len(parts) == 2:
            if len(parts[1]) == 0:
                return is_number(parts[0], _DIGITS)
            else:
                return is_number(parts[0], _DIGITS) and is_number(parts[1], _DIGITS)
        else:
            return False

    return all(x in _DIGITS for x in s)


class Solution:
    def isNumber(self, s: str) -> bool:
        return is_number(s.strip(), _ALL_ALLOWED_CHARS)


def main():
    assert Solution().isNumber("0") is True
    assert Solution().isNumber("0.1") is True
    assert Solution().isNumber("abc") is False
    assert Solution().isNumber("1 a") is False
    assert Solution().isNumber("2e10") is True
    assert Solution().isNumber(" -90e3") is True
    assert Solution().isNumber(" 1e") is False
    assert Solution().isNumber("e3") is False
    assert Solution().isNumber(" 6e-1") is True
    assert Solution().isNumber("99e2.5") is False
    assert Solution().isNumber("53.5e93") is True
    assert Solution().isNumber(" --6") is False
    assert Solution().isNumber("-+3") is False
    assert Solution().isNumber("95a54e53") is False
    assert Solution().isNumber("1.2.3") is False
    assert Solution().isNumber("95e54e53") is False


if __name__ == '__main__':
    main()
