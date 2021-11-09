# n = n
# time = O(nlogn)
# space = O(n)
# done time = 30m


from collections import deque


class Solution:

    def getHappyString(self, n: int, k: int) -> str:
        happy = ['a', 'b', 'c']
        stack = deque(happy)

        while stack:
            curr_word = stack.popleft()
            if len(curr_word) == n:
                stack.append(curr_word)
                break

            for word in happy:
                if curr_word[-1] != word:
                    stack.append(curr_word + word)

        if len(stack) >= k:
            return sorted([word for word in stack if len(word) == n])[k-1]
        else:
            return ''
