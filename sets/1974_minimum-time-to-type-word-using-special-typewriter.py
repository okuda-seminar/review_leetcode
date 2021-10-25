'''
Q[1974]. Minimum Time to Type Word Using Special Typewriter

n = len(word)
time : O(n)
space : O(n)
'''

class Solution:
    def minTimeToType(self, word: str) -> int:
        '''compute the minimum seconds of type out the characters in word
        Args:
            word(str): string consist of alphabet a to z (1 <= len(word) <= 100)
        Returns:
            int: the minimum seconds of type out the characters in word 
        '''
        if not word:
            raise ValueError('word should be [1, 100]')
        
        cur_place = ord('a')
        min_time_to_type = 0
        alphabet_num = 26

        for char in word:
            next_place = ord(char)
            diff = abs(next_place - cur_place)

            if diff > alphabet_num // 2:
                diff = alphabet_num - diff

            min_time_to_type += diff + 1
            cur_place = next_place
        
        return min_time_to_type
