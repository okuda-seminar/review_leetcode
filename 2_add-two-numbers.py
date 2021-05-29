#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        time: O(len(n))  n : max(len(l1), len(l2))
        space: O(len(n))
        """
        total = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            sum_digit = carry
            if l1:
                sum_digit += l1.val
                l1 = l1.next
            if l2:
                sum_digit += l2.val
                l2 = l2.next
            cur.next = ListNode(sum_digit % 10)
            carry = sum_digit // 10
            cur = cur.next
        return total.next
# @lc code=end

