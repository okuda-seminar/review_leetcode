'''
Q[1884]. Egg Drop With 2 Eggs and N Floors
'''

# time : O(n**2)
# space : O(n)


class Solution:
    def twoEggDrop(self, n: int) -> int:
        '''Returns the minimum number of moves that you need to
           determine with certainty what the value of f is
        Args:
            n(int): the number of floors (1 <= n <= 1000)
        Returns:
            int: the minimum number of moves that you need
                 to determine with certainty what the value of f is
        '''
        if not n:
            raise ValueError('n lenght should be [1, 1000]')

        min_move_nums = [float(inf)] * (n + 1)
        min_move_nums[0] = 1
        min_move_nums[1] = 1

        for i in range(2, n + 1):
            for j in range(1, i):
                min_move_nums[i] = min(min_move_nums[i], 1 + max(j - 1, min_move_nums[i - j]))

        return min_move_nums[-1]


# time : O(n)
# space : O(1)


class Solution:
    def twoEggDrop(self, n: int) -> int:
        min_move_num = 1

        while n > 0:
            n -= min_move_num
            min_move_num += 1

        return min_move_num - 1
