#
# @lc app=leetcode id=1290 lang=python3
#
# [1290] Convert Binary Number in a Linked List to Integer
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        """convert binary number to integer

        Args:
            head(ListNode): a reference node to a singly-linked list

        Returns:
            int: the decimal value of the number in the linked list
        """
        """
        time complexity: O(n)
        space complexity: O(1)
        """
        """
        if not head:
            return None
        
        ans = head.val
        while head.next:
            ans = ans * 2 + head.next.val
            head = head.next
        return ans
        """
        # use Bit Manipulation
        """
        time complexity: O(n)
        space complexity: O(1)
        """
        if not head:
            return None
        
        ans = head.val
        while head.next:
            ans = ans << 1 | head.next.val
            head = head.next
        return ans
# @lc code=end
