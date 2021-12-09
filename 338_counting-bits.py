class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        time: O(n)
        space: O(n)
        """
        count_1_list = []
        for i in range(2):
            count_1_list.append(i)
            if n == i:
                return count_1_list

        for i in range(2, n + 1):
            if i % 2 == 0:
                count_1_list.append(count_1_list[i // 2])
            else:
                count_1_list.append(count_1_list[i - 1] + 1)
        return count_1_list