#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        time: O(len(headA)+len(headB))
        space: O(len(headA)+len(headB))
        """
        if not headA or not headB:
            return None

        copy_headA = headA
        copy_headB = headB
        len_headA = 0
        len_headB = 0
        while copy_headA:
            len_headA += 1
            copy_headA = copy_headA.next
        while copy_headB:
            len_headB += 1
            copy_headB = copy_headB.next
        if len_headA < len_headB:
            for diff in range(len_headB - len_headA):
                headB = headB.next
        if len_headB < len_headA:
            for diff in range(len_headA - len_headB):
                headA = headA.next
        while headA:
            if headA == headB:
                return headA

            headA = headA.next
            headB = headB.next

# @lc code=end

