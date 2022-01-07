"""
stack
n = len(s)
time = O(n)
space = O(1)
"""
class Solution:
    def isValid(self, s: str) -> bool:
        bra_dict = {')':'(', '}':'{', ']':'['}
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if not stack:
                    return False
                
                if not stack.pop() == bra_dict[char]:
                    return False
                
        return not stack