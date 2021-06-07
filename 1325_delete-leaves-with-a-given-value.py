# n = node num of root
# time = O(n)
# space = O(1)
# done time = 5m


class Solution:

    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if root is None:
            return None

        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        if root.left is None and root.right is None and root.val == target:
            return None

        return root
