#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """remove n-th node from end of list

        Args:
            head(Optional[ListNode]): Linked list
            n(int): integer
        
        Returns:
            Optional[ListNode]: remove n-th node from end of list
        """
        """
        time complexity: O(len(head))
        space complexity: O(len(head))
        """
        if not head:
            return None

        cur = head
        len_head = 0

        while cur:
            len_head += 1
            cur = cur.next

        idx = len_head - n
        cur = head

        if idx == 0:
            return head.next

        else:
            while 1 < idx:
                cur = cur.next
                idx -= 1
            cur.next = cur.next.next
        return head
# @lc code=end
