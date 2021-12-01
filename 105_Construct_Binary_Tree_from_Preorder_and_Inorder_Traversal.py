"""
recursion
n = len(preorder)
m = len(inorder)
condition: n == m
time = O(m+n) = O(n)
space = O(n)
"""
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """build tree
        Args:
            preorder (List[int]): preorder traversal of a binary tree
            inorder (List[int]): inorder traversal of a binary tree
        Returns:
            Optional[TreeNode]: a binary tree
        """
        if preorder:
            node_val = preorder[0]
            root = TreeNode(node_val)
            node_index = inorder.index(node_val)
            root.left = self.buildTree(preorder[1:node_index+1], inorder[:node_index])
            root.right = self.buildTree(preorder[node_index+1:], inorder[node_index+1:])
            return root