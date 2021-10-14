'''
Question:
Given a string s, reverse the order of characters in each word within a sentence
while still preserving whitespace and initial word order.

Answer:
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        '''Reverse word while preserving whitespace
        Args:
            s(str): string consist of ASCII characters
        Returns:
            str: reverse word while preserving whitespace
        '''
        # easy solution : O(n) # n = s.length
        if not s:
            return ''

        return ' '.join([w[::-1] for w in s.split()])

        # two pointers : O(n) # n = s.length
        if not s:
            return ''
        
        space_idx = []
        s_list = list(s)
        space_idx = [i for i in range(len(s_list)) if s[i] == ' ']
        space_idx.append(len(s_list))
        space_reverse_idx = space_idx[::-1]
        left = 0
        while space_reverse_idx:
            idx = space_reverse_idx.pop()
            right = idx - 1
            while left < right:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
            left = idx + 1
                
        return ''.join(s_list)
