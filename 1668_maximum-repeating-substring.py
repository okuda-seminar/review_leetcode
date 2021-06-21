# n = sequence.length = 100
# time = O(nlogn)
# space  = O(1)
# done time = 15m


class Solution:

    def maxRepeating(self, sequence: str, word: str) -> int:
        if word not in sequence:
            return 0

        left = 0
        right = len(sequence) // len(word) + 1

        while 1 < right - left:
            mid = (left + right + 1) >> 1
            if word * mid in sequence:
                left = mid
            else:
                right = mid

        return left
