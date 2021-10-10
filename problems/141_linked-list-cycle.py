#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        time: O(len(head))
        space: O(1)
        """
        if not head:
            return False

        fast_node = head
        slow_node = head
        while fast_node and fast_node.next:
            fast_node = fast_node.next.next
            slow_node = slow_node.next
            if fast_node == slow_node:
                return True

        return False
# @lc code=end

