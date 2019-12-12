#!/us/bin/env python

"""
查询括号是否合法
"""

def isValid(self, s):
    stack = []
    paren_map = {')': '(', ']': '[', '}': '{'}
    for c in s:
        if c not in paren_map:
            stack.append(c)
        elif not stack or paren_map[c] != stack.pop():
            return False

    return not stack