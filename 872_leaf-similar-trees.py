# V = max{node num in tree1, node num in tree2}
# time: O(V)
# space: O(V)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def traverse(leaves, n):
            if n is None:
                return
            if n.left is None and n.right is None:
                leaves.append(n.val)
                return
            traverse(leaves, n.left)
            traverse(leaves, n.right)
            
        l1, l2 = [], []
        traverse(l1, root1)
        traverse(l2, root2)
        return l1 == l2
