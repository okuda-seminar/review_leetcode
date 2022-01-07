"""
stack
time = O(n)
space = O(n)
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = [('(', 1, 0)]
        output = []
        while stack:
            parenthes, left, right = stack.pop()
            if len(parenthes) == 2 * n:
                output.append(parenthes)
                continue
            if right < left:
                stack.append((parenthes+')', left, right+1))
            if left < n:
                stack.append((parenthes+'(', left+1, right))
        return output