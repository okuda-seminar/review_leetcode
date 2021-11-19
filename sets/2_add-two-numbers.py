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
"""
n = max(len(l1), len(l2))
time: O(n)
space: O(n)
"""
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """Add two numbers

        Args:
            l1(Optional[ListNode]): non-empty linked lists representing two non-negative integers
            l2(Optional[ListNode]): non-empty linked lists representing two non-negative integers
        
        Returns:
            Optional[ListNode]: sum of the two numbers
        """
        ans = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            sum_num = 0
            if l1:
                sum_num += l1.val
                l1 = l1.next
            if l2:
                sum_num += l2.val
                l2 = l2.next
            sum_num += carry
            cur.next = ListNode(sum_num % 10)
            carry = sum_num // 10
            cur = cur.next

        return ans.next


# use recursion
"""
n = max(len(l1), len(l2))
time: O(n)
space: O(n)
"""
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """Add two numbers

        Args:
            l1(Optional[ListNode]): non-empty linked lists representing two non-negative integers
            l2(Optional[ListNode]): non-empty linked lists representing two non-negative integers
        
        Returns:
            Optional[ListNode]: sum of the two numbers
        """
        sum_num = l1.val + l2.val
        cur_num = sum_num % 10
        carry = sum_num // 10
        ans = ListNode(cur_num)
        if l1.next or l2.next or carry:
            """
            l1 = l1.next if l1.next else ListNode(0)
            l2 = l2.next if l2.next else ListNode(0)
            l1.val += tenth
            answer.next = self.addTwoNumbers(l1, l2)  
            """
            if l1.next:
                l1 = l1.next
            else:
                l1 = ListNode(0)
            if l2.next:
                l2 = l2.next
            else:
                l2 = ListNode(0)
            l1.val += carry
            ans.next = self.addTwoNumbers(l1, l2)

        return ans
# @lc code=end
