'''
Q[1190]. Reverse Substrings Between Each Pair of Parentheses
'''

# n = len(s)
# m = the number of parentheses
# time : O(n * m)
# space : O(n)


class Solution:

    def reverseParentheses(self, s: str) -> str:
        '''Reverse string between parentheses
        Args:
            s(str): string (0 <= len(s) <= 2000)
        Returns:
            str: reversed string between parentheses
        '''
        if not s:
            return ''

        while '(' in s:
            for i in reversed(range(len(s))):
                if s[i] == ')':
                    j = i
                elif s[i] == '(':
                    ans = s[i+1:j][::-1]
                    break

            s = s[:i] + ans + s[j+1:]
        return s
