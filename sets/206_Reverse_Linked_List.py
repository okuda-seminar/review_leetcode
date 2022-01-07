"""
stack
n = length of head
time = O(n)
space = O(n)
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = ans = head
        stack = []
        while curr:
            stack.append(curr.val)
            curr = curr.next
        while stack:
            ans.val = stack.pop()
            ans = ans.next
        return head
"""
recursive
n = length of head
time = O(n)
space = O(n)
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            n = curr.next
            curr.next = prev
            prev = curr
            curr = n
        return prev