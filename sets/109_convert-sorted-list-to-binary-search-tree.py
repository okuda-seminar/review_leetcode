#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        """Function to convert head to a height balanced BST
        Args:
            head(Optional[ListNode]): singly linked list
        Returns:
            Optional[TreeNode]: a height balanced BST.
        """
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        
        cur = head
        slow = head
        fast = head

        while fast and fast.next:
            pre = slow
            fast = fast.next.next
            slow = slow.next
        pre.next = None
        ans = TreeNode(slow.val)
        ans.left = self.sortedListToBST(cur)
        ans.right = self.sortedListToBST(slow.next)
        return ans
# @lc code=end

