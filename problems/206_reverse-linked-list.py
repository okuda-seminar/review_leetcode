#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        time: O(len(head))
        space: O(1)
        """
        reversed_head = None
        while head:
            cur = head
            head = head.next
            cur.next = reversed_head
            reversed_head = cur
        return reversed_head 
# @lc code=end

