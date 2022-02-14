'''
Q[1963]. Minimum Number of Swaps to Make the String Balanced
'''

# brute-force solution
# n = len(s)
# time : O(n)
# space : O(1)


class Solution:
    def minSwaps(self, s: str) -> int:
        '''Return minimum number of swaps to make the string balanced
        Args:
            s(str): string consist of parenthesis (2 <= len(s) <= 10**6)
        Returns:
            int: minimum number of swaps to make the string balanced
        '''
        if not s:
            raise ValueError('s length should be [2, 10**6]')

        left = 0
        right = len(s) - 1
        s_list = list(s)
        is_left_swap = is_right_swap = False
        left_count = right_count = swap_num = 0

        while left < right:
            if s_list[left] == '[':
                left_count += 1
                left += 1
                continue

            if s_list[right] == ']':
                right_count += 1
                right -= 1
                continue

            if s_list[left] ==']':
                if left_count == 0:
                    is_left_swap = True
                else:
                    left += 1
                    left_count -= 1

            if s_list[right] == '[':
                if right_count == 0:
                    is_right_swap = True
                else:
                    right -= 1
                    right_count -= 1

            if is_left_swap and is_right_swap:
                s_list[left], s_list[right] = s_list[right], s_list[left]

                is_left_swap = False
                is_right_swap = False

                swap_num += 1
                left += 1
                right -= 1
                left_count += 1
                right_count += 1

        return swap_num


# time : O(n)
# space : O(1)


class Solution:
    def minSwaps(self, s: str) -> int:
        extra_close = close = 0
        
        for char in s:
            if char == "[":
                close -= 1
            else:
                close += 1
            extra_close = max(close, extra_close)
            
        return (extra_close + 1) // 2
