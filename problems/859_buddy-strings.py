# n = max(a.length, b.length)
# time = O(n)
# space = O(n)
# done time = 20m


class Solution:

    def buddyStrings(self, a: str, b: str) -> bool:        
        if len(a) != len(b):
            return False        

        if a == b:
            return len(set(a)) != len(b)

        diff = [(string_a, string_b) for string_a, string_b in zip(a, b) if string_a != string_b]

        return len(diff) == 2 and (diff[0] == diff[1][::-1])
