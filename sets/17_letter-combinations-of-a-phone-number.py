#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
from collections import deque


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """Function to return all possible letter
        Args:
            digits(str): string
        Returns:
            List[str]: all possible letter
        """
        if not digits:
            return []

        char_num = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        queue = deque()
        for char in char_num[digits[0]]:
            queue.append(char)
        idx = 1
        
        while queue:
            if idx == len(digits):
                break

            n = len(queue)
            for _ in range(n):
                cur = queue.popleft()
                for char in char_num[digits[idx]]:
                    cur_sentence = cur + char
                    queue.append(cur_sentence)
            idx += 1

        return list(queue)
# @lc code=end
