# n = sequence.length
# time = O(n^2)
# space  = O(1)
# done time = 15m


class Solution:

    def maxRepeating(self, sequence: str, word: str) -> int:
        count = 0
        concatenation_word = word
        while concatenation_word in sequence:
            concatenation_word += word
            count += 1
        return count
