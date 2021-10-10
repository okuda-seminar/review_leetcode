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
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        time: O(S) S: sum of the all node
        space: O(S)
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
        """
        if not l1:
            cur_node.next = l2
        else:
            cur_node.next = l1
        """
        cur_node.next = l1 if not l2 else l2
        return head.next
        
# @lc code=end

