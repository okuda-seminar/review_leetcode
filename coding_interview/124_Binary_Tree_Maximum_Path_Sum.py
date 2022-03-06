"""
Find the maximum length of the path under the condition that a node passes only once.
N : the number of vertex
M : the number of branch
time complexity : O(N + M)
space complexity : O(1)
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_path = float("-inf")
        self.get_max_path(root)
        return self.max_path

    def get_max_path(self, node: TreeNode):
        if node is None:
            return 0

        gain_on_left = self.get_max_path(node.left)
        gain_on_right = self.get_max_path(node.right)		
        current_max_path = gain_on_left + gain_on_right
        self.max_path = max(self.max_path, current_max_path)
        return max(gain_on_left, gain_on_right) + 1

"""
Find the maximum sum of the node under the condition that a node passes only once.
N : the number of vertex
M : the number of branch
time complexity : O(N + M)
space complexity : O(1)
"""
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_path = float("-inf")
        self.get_max_gain(root)
        return self.max_path
    
    def get_max_gain(self, node: TreeNode) -> int:
        if node is None:
            return 0

        gain_on_left = max(self.get_max_gain(node.left), 0)
        gain_on_right = max(self.get_max_gain(node.right), 0)		
        current_max_path = node.val + gain_on_left + gain_on_right
        self.max_path = max(self.max_path, current_max_path)
        return max(gain_on_left, gain_on_right) + node.val
