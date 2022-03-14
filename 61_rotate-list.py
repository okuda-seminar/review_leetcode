#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
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
space: O(1)
"""
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """Function to rotate linked list
        Args:
            head(Optional[ListNode]): linked list
            k(int): integer
        Returns:
            Optional[ListNode]: rotated linked list
        """
        if not head:
            return None

        cur = head
        len_head = 0
        while cur:
            cur = cur.next
            len_head += 1
        
        k = k % len_head
        if k == 0:
            return head

        fast = slow = head
        while k:
            fast = fast.next
            k -= 1
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        ret = slow.next
        slow.next = None
        fast.next = head
        return ret
# @lc code=end
