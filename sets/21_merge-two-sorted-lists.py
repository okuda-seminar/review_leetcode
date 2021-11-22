#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""
V : the number of the all nodd
time: O(V)
space: O(V)
"""
class Solution:
    def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Merge two sorted linked lists
        
        Args:
            l1(ListNode): sorted linked list
            l2(ListNode): sorted linked list

        Returns:
            ListNode: merge two sorted linked lists
        """
        head = ListNode(0)
        cur_node = head
        while l1 and l2:
            if l1.val <= l2.val:
                cur_node.next = ListNode(l1.val)
                l1 = l1.next
            else:
                cur_node.next = ListNode(l2.val)
                l2 = l2.next
            cur_node = cur_node.next
        
        cur_node.next = l1 if not l2 else l2

        return head.next


"""
V : the number of the all nodd
time: O(V)
space: O(V)
"""
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Merge two sorted linked lists
        
        Args:
            l1(ListNode): sorted linked list
            l2(ListNode): sorted linked list

        Returns:
            ListNode: merge two sorted linked lists
        """
        if not l1:
            return l2
        
        elif not l2:
            return l1
        
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
# @lc code=end
