# n = words.length <= 50
# m = pattern.length <= 20
# time = O(nm^2)
# space = O(n)
# done time = 20m

from collections import defaultdict


class Solution:

    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def check(word: str, pattern: str) -> bool:
            check_str = defaultdict(str)
            for i in range(len(pattern)):
                if not check_str[pattern[i]]:
                    check_str[pattern[i]] = word[i]
                if check_str[pattern[i]] != word[i] or\
                        list(check_str.values()).count(word[i]) > 1:
                    return False

            return True

        return [word for word in words if check(word, pattern)]
