# n = sentence.length
# time = O(n)
# space = O(1)
from collections import Counter
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        """
        Args:
            sentence: str: the sentence is consist of the English alphabet, 1 <= sentence.length <= 1000 or less
        Returns:
            bool: the sentence include all letter of the English alphabet
        """
        if len(sentence) == 0:
            raise ValueError("sentence is one or more")
        if len(sentence) > 1000:
            raise ValueError("sentence is one hundred or less")
        return len(Counter(sentence)) == 26

# n = sentence.length
# time = O(n)
# space = O(1)
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        """
        Args:
            sentence: str: the sentence is consist of the English alphabet, 1 <= sentence.length <= 1000 or less
        Returns:
            bool: the sentence include all letter of the English alphabet
        """
        if len(sentence) == 0:
            raise ValueError("sentence is one or more")
        if len(sentence) > 1000:
            raise ValueError("sentence is one hundred or less")
        return len(set(sentence)) == 26