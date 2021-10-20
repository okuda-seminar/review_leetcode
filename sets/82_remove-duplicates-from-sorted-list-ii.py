#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """remove duplicates from sorted list

        Args:
            head(Optional[ListNode]): a sorted linked list
        
        Returns:
            Optional[ListNode]: delete all nodes which have duplicate numbers
        """
        """
        time complexity: O(len(head))
        space complexity: O(len(head))
        """
        if not head:
            return None
        
        ans = cur = ListNode(0, head)
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                dup_cur = cur.next
                while dup_cur.next and dup_cur.val == dup_cur.next.val:
                    dup_cur = dup_cur.next
                cur.next = dup_cur.next
            else:
                cur = cur.next

        return ans.next
        
# @lc code=end
