'''
Q[894]. All Possible Full Binary Trees
'''

# n = n
# m = the number of possible tree
# time : O(n ** 2)
# space : O(n * m)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        '''Return  a list of all possible full binary trees with n nodes
        Args:
            n(int): integer(1 <= n <= 20)
        Returns:
            List[TreeNode]:  a list of all possible full binary trees with n nodes
        '''
        if n % 2 == 0:
            return []

        self.memo = {}
        return self.tree(n)

    def recursion(self, n: int) -> List[TreeNode]:
        '''Return  a list of all possible full binary trees with n nodes
        Args:
            n(int): integer
        Returns:
            List[TreeNode]:  a list of all possible full binary trees with n nodes
        '''
        if n in self.memo:
            return self.memo[n]

        if n == 1:
            self.memo[n] = [TreeNode(0)]
            return self.memo[n]

        possible_tree= []

        for i in range(1, n, 2):
            left = self.recursion(i)
            right = self.recursion(n - 1 - i)
            for l in left:
                for r in right:
                    possible_tree.append(TreeNode(0, l, r))
        self.memo[n] = possible_tree
        return self.memo[n]
