# n = sentence.length
# time = O(n)
# space = O(1)
from collections import Counter
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        """
        Args:
            sentence: str: the sentence is consist of the English alphabet, 1 <= sentence.length <= 1000
        Returns:
            bool: the sentence include all letter of the English alphabet
        """
        length_low = 1
        length_high = 1000
        num_alphabet = 26
        if len(sentence) < length_low or length_high < len(sentence):
            raise ValueError("sentence length is one or more and one thousand or less")
        return len(Counter(sentence)) == num_alphabet

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
        length_low = 1
        length_high = 1000
        num_alphabet = 26
        if len(sentence) < length_low or length_high < len(sentence):
            raise ValueError("sentence length is one or more and one thousand or less")
        return len(set(sentence)) == num_alphabet