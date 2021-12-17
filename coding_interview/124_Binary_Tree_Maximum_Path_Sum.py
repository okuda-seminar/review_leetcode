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
        max_path = float("-inf")
        def get_max_gain(node):
            nonlocal max_path
            if node is None:
                return 0

            gain_on_left = get_max_gain(node.left)
            gain_on_right = get_max_gain(node.right)		
            current_max_path = gain_on_left + gain_on_right
            max_path = max(max_path, current_max_path)

            return max(gain_on_left, gain_on_right) + 1
        
        
        get_max_gain(root)
        return max_path		
"""
Find the maximum sum of the node under the condition that a node passes only once.
N : the number of vertex
M : the number of branch
time complexity : O(N + M)
space complexity : O(1)
"""
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_path = float("-inf")
        def get_max_gain(node):
            nonlocal max_path
            if node is None:
                return 0
            
            
            gain_on_left = max(get_max_gain(node.left), 0)
            gain_on_right = max(get_max_gain(node.right), 0)		
            current_max_path = node.val + gain_on_left + gain_on_right
            max_path = max(max_path, current_max_path)

            return max(gain_on_left, gain_on_right) + node.val
        
        
        get_max_gain(root)
        return max_path