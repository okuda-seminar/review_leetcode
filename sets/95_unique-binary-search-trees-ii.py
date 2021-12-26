#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
time: O(n^3)
space: O(n^2)
"""
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        """Function to return structurally unique BST's
        Args:
            n(int): integer
        Returns:
            List[Optional[TreeNode]]: all the structurally unique BST's
        """
        if not n:
            return []

        dp = [[None] * (n + 1) for _ in range(n + 1)]
        for k in range(n):
            for i in range(1, n - k + 1):
                start, end = i, i + k
                if start == end:
                    dp[start][end] = [TreeNode(start)]
                else:
                    res = []
                    
                    for right_node in dp[start + 1][end]:
                        root = TreeNode(start)
                        root.right = right_node
                        res.append(root)
                    for left_node in dp[start][end - 1]:
                        root = TreeNode(end)
                        root.left = left_node
                        res.append(root)
                    for idx in range(start + 1,end):
                        for left_node in dp[start][idx - 1]:
                            for right_node in dp[idx + 1][end]:
                                root = TreeNode(idx)
                                root.left, root.right = left_node, right_node
                                res.append(root)
                                
                    dp[start][end] = res

        return dp[1][n]
# @lc code=end
