#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """swap every two adjacent nodes 
        
        Args:
            head(Optional[ListNode]): a linked list

        Returns:
            Optional[ListNode]: swap every two adjacent nodes 
        """
        """
        time complexity: O(len(head))
        space complexity: O(len(head))
        """
        if not head or not head.next:
            return head

        ans = cur = ListNode(0, head)
        while cur.next and cur.next.next:
            first = cur.next
            second = cur.next.next
            cur.next = second
            first.next = second.next
            second.next = first
            cur = cur.next.next
        return ans.next
# @lc code=end

