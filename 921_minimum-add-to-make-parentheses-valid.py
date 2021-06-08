# n = s.length
# time = O(n)
# space = O(1)
# done time = 5,


class Solution:

    def minAddToMakeValid(self, s: str) -> int:
        left = 0
        add_parentheses_count = 0

        for par in s:
            if par == "(":
                left += 1
                add_parentheses_count += 1
            else:
                if left > 0:
                    add_parentheses_count -= 1
                    left -= 1
                else:
                    add_parentheses_count += 1

        return add_parentheses_count
