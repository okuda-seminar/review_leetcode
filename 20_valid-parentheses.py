#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        """
        time: O(len(s))
        space: O(len(s))
        """
        stack = deque()
        brackets_dict = {")" : "(" , "}" : "{" , "]" : "[", }
        for char in s:
            if char in brackets_dict.values():
                stack.append(char)
            elif char in brackets_dict.keys():
                if not stack or brackets_dict[char] != stack.pop():
                    return False
            else:
                return False
        return not stack

# @lc code=end

