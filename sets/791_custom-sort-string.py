'''
Q[791]. Custom Sort String
'''

# n = len(s)
# m = len(order)
# time : O(n * m)
# space : O(n)

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        '''Sort s in order of order
        Args:
            order(str): string consist of lowercase (1 <= len(order) <= 26)
            s(str): string consist of lowercase (1 <= len(s) <= 200)
        Returns:
            str: sorted s in order of order
        '''
        if not order:
            raise ValueError('order length should be [1, 26]')

        if not s:
            raise ValueErorr('s length should be [1, 200]')

        s_list = list(s)
        order_idx = 0
        custom_sort_string = ''

        while swap_idx < len(order):
            if order[order_idx] in s_list:
                custom_sort_string += s_list.pop(s_list.index(order[order_idx]))
            else:
                order_idx += 1
                continue

        if s_list:
            custom_sort_string += ''.join(s_list)

        return custom_sort_string
