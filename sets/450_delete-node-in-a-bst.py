#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """Delete the node with the given key in the BST
        Args:
            root(TreeNode): BST
            key(int): integer
        Returns:
            TreeNode: the root node reference (possibly updated) of the BS
        """
        if not root:
            return None
        
        if key<root.val:
            root.left = self.deleteNode(root.left,key)

        elif key>root.val:
            root.right = self.deleteNode(root.right,key)

        elif root.val == key:
            if not root.left and not root.right:
                return None
            
            elif not root.left:
                return root.right
            
            elif not root.right:
                return root.left
            
            else:
                tmp = root.left
                while tmp.right:
                    tmp = tmp.right
                root.val = tmp.val
                root.left = self.deleteNode(root.left, root.val)
        return root
# @lc code=end
