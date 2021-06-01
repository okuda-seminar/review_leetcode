# n = preorder.length
# time = O(n)
# space = O(n)
# done time = 10m


class Solution:

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        def insert(root, val):
            if root is None:
                return TreeNode(val)

            if val < root.val:
                root.left = insert(root.left, val)
            else:
                root.right = insert(root.right, val)
            return root

        root = TreeNode(preorder[0])
        for i in range(1, len(preorder)):
            root = insert(root, preorder[i])

        return root
