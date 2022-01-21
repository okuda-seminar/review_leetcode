#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
n = len(head)
time: O(n)
space: O(n)
"""
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        """Return reorder the list
        Args:
            head(Optional[ListNode]): the head of a singly linked-list
        """
        if head and head.next and head.next.next:
            head = self.reorder(head)
    
    def reorder(self, node: Optional[ListNode]) -> Optional[ListNode]:
        """Return reorder the list
        Args:
            head(Optional[ListNode]): the head of a singly linked-list
        Returns:
            reorder the list
        """
        if not node or not node.next or not node.next.next:
            return node
        
        prev = cur = node
        while cur.next:
            prev = cur
            cur = cur.next
        next_node = node.next
        node.next = cur
        prev.next = None
        cur.next = self.reorder(next_node)
        return node
# @lc code=end
