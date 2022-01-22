"""
n : the number of node
time complexity = O(n)
space complexity = O(1)
"""
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        ret = self.dfs(root)
        return max(ret)
        
    def dfs(self, root: Optional[TreeNode]) -> tuple[int]:
        if root is None:
            return (0, 0)
        
        left = self.dfs(root.left) # left[0] : current, left[1] : prev
        right = self.dfs(root.right)# right[0] : current, right[1] : prev
        return (root.val + left[1] + right[1], max(left[0], left[1]) + max(right[0], right[1]))