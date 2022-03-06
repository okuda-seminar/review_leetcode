"""
recursion
n = length of head
time = O(min(n, log n))
space = O(n)
"""
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        """sorted list convert to binary search tree
        Args:
            head (ListNode) : sorted in sacending order
        Returns:
            TreeNode : binary search tree
        Examples:
            sortedListToBST([-10,-3,0,5,9]) <- [0,-3,9,-10,null,5]
        """
        arr = []
        node = head
        while node:
            arr.append(node.val)
            node = node.next
        return self.construct(arr, 0, len(arr) - 1)
        
    def construct(self, arr: list, start: int, end: int):
        if start <= end:
            mid = (start + end) // 2
            node = TreeNode(arr[mid])
            node.left = self.construct(arr, start, mid - 1)
            node.right = self.construct(arr, mid + 1, end)
            return node

"""
divide and conquare
n = length of head
time = O(n)
space = O(1)
"""
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        """sorted list convert to binary search tree
        Args:
            head (ListNode) : sorted in sacending order
        Returns:
            TreeNode : binary search tree
        Examples:
            sortedListToBST([-10,-3,0,5,9]) <- [0,-3,9,-10,null,5]
        """
        if not head:
            return None
        
        if not head.next:
            return TreeNode(head.val)
        
        slow = head
        fast = head.next
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if prev:
            prev.next = None
        else:
            head = None
        node = TreeNode(slow.val)
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(slow.next)
        return node