'''
Problem :
Given the root of an n-ary tree, return the postorder traversal of its nodes' values.
Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

Answer :
'''
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:        
        '''Store val postorder
        Args:
            root(Node): root have children
        Returns:
            List[int]: list of postorder val
        '''
        '''DFS : O(V) # V : the number of nodes

        self.res = []
        def node_traversal(root):
            if root is None:
                return
            
            for children in root.children:
                node_traversal(children)
                
            self.res.append(root.val)
            return
        
        node_traversal(root)
        return self.res
        '''

        '''BFS : O(V) # V : the number of nodes

        from collections import deque

        if root is None:
            return None
        
        stack = deque([root])
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            
            for children in node.children:
                stack.append(children)
            
        return res[::-1]
        '''
