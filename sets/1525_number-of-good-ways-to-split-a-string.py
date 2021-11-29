'''
Q[1525]. Number of Good Ways to Split a String
'''

# n = len(s)
# time : O(n)
# space : O(n)


class Solution:
    def numSplits(self, s: str) -> int:
        '''Return the number of good splits
        Args:
            s(str): strings (1 <= len(s) <= 10**5)
        Returns:
            int : the number of good splits
        '''
        if not s:
            raise ValueError('s length should be [1, 10**5]')

        n = len(s)
        
        distinct_letters = []
        count_distinct_letters = [0 for _ in range(n - 1)]
        count_distinct_letters[0] = 1
        distinct_letters.append(s[0])
        
        for i in range(1, n - 1):
            if s[i] in distinct_letters:
                count_distinct_letters[i] = count_distinct_letters[i - 1]
            else:
                distinct_letters.append(s[i])
                count_distinct_letters[i] = count_distinct_letters[i - 1] + 1
                
        num_splits = 0

        distinct_letters = []
        back_count = 0
        for i in range(n - 1, 0, -1):
            if s[i] not in distinct_letters:
                distinct_letters.append(s[i])
                back_count += 1
            
            if back_count == count_distinct_letters[i - 1]:
                num_splits += 1
                
        return num_splits
