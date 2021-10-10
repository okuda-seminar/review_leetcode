# n = test.length
# time = O(n)
# space = O(n)
# done time = 20m


class Solution:

    def reorderSpaces(self, text: str) -> str:
        num_spaces = Counter(text)[' ']
        words = text.split()
        num_places = len(words) - 1

        if num_places == 0:
            return words[0] + ' '*num_spaces

        num_continuous_space = 0

        while (num_continuous_space + 1) * num_places <= num_spaces:
            num_continuous_space += 1

        return (' ' * num_continuous_space).join(words) + ' ' * (num_spaces - num_continuous_space*num_places)
