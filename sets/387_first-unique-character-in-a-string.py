#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
from collections import Counter, deque


class Solution:
    def firstUniqChar(self, s: str) -> int:
        """return non-repeating character in s
        
        Args:
            s(str): string
        
        Returns:
            int: non-repeating character in s
        """
        # use conter
        """
        time: O(n)
        space: O(n)
        n : len(s)
        """
        """
        s_counter = Counter(s)
        for i in range(len(s)):
            if s_counter[s[i]] == 1:
                return i

        return -1
        """

        # use queue
        """
        time: O(n)
        space: O(n)
        n : len(s)
        """
        first_idx_dict = {}
        stack = deque()
        for idx, char in enumerate(s):
            if char in first_idx_dict:
                first_idx_dict[char] = -1
            else: 
                first_idx_dict[char] = idx
                stack.append(char)

        while stack:
            first_idx_char = stack.popleft()
            if first_idx_dict[first_idx_char] != -1:
                return first_idx_dict[first_idx_char]

        return -1
# @lc code=end
