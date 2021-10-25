#
# @lc app=leetcode id=1721 lang=python3
#
# [1721] Swapping Nodes in a Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """swapping nodes in a linked list
        
        Args:
            head(Optional[ListNode]): a linked list
            k(int): integer
        
        Returns:
            Optional[ListNode]: the head of the linked list after swapping the values
        """
        """
        time complexity: O(len(head))
        space complexity: O(len(head))
        """
        if not head:
            return None

        first_pointer = head
        while 1 < k:
            first_pointer = first_pointer.next
            k -= 1
        beginning_kth_listnode = first_pointer
        end_kth_listnode = head

        while first_pointer.next:
            first_pointer = first_pointer.next
            end_kth_listnode = end_kth_listnode.next

        beginning_kth_listnode.val, end_kth_listnode.val = end_kth_listnode.val, beginning_kth_listnode.val
        return head
# @lc code=end
