#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque


""" 
n = len(head)
time: O(n)
space: O(n)
"""
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """Judge palindrome
        Args:
            head(Optional[ListNode])
        Returns:
            bool: return True if head is palindrome
        """
        if not head:
            return True
        
        queue = deque()
        while head:
            queue.append(head.val)
            head = head.next
        
        while 2 <= len(queue):
            if queue.popleft() != queue.pop():
                return False
        
        return True
# @lc code=end

