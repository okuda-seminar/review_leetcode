'''
Q[451]. Sort Characters By Frequency
'''

# n = len(s)
# time : O(nlogn)
# space : O(n)


from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        '''Sort string based on the frequency
        Args:
            s(str): string (1 <= len(s) <= 5 * 10**5)
        Returns:
            str: sorted string based on the frequency
        '''
        if not s:
            raise ValueError('s length should be [1, 5 * 10**5]')

        s_count = sorted(Counter(s).items(), key=lambda x:x[1], reverse=True)
        sorted_s = []

        for k, v in s_count:
            sorted_s.append(k * v)

        return ''.join(sorted_s)


# time : O(n)
# space : O(n)


from heapq import heapify, heappop


class Solution:
    def frequencySort(self, s: str) -> str:
        frequency = {}
        for char in s:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1

        frequency_heap = []
        for key, val in frequency.items():
            frequency_heap.append((-val, key))
        heapify(frequency_heap)

        sorted_s = []
        while len(frequency_heap) > 0:
            freq, char = heappop(frequency_heap)
            sorted_s.append(-freq * char)

        return ''.join(sorted_s)
