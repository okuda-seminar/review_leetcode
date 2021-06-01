# n = node of number of root1 and root2
# time = O(n)
# space = O(n)
# done time = 20m


from collections import deque


class Solution:

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:

        def getElements(root: TreeNode, elements: List[int]) -> List[int]:
            stack = deque([root])

            while stack:
                curr_node = stack.pop()
                if curr_node is None:
                    continue
                elements.append(curr_node.val)
                stack.append(curr_node.left)
                stack.append(curr_node.right)

            return elements

        elements = getElements(root1, [])
        elements = getElements(root2, elements)
        return sorted(elements)
