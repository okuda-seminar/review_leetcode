Q[942]. DI String Match

n : s.length
time : O(n)
space : O(n)

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        '''compute perm
        Args:
            s(str):string consist of 'I' or 'D' (1 <= len(s) <= 10^5)
        Returns:
            List[int]: perm (perm[i] < perm[i+1] if s[i] == 'I',
                             perm[i] > perm[i+1] if s[i] == 'D')
        '''
        if not s:
            return []

        perm = []
        left = 0
        right = len(s)
        for i in range(len(s)):
            if s[i] == 'I':
                perm.append(left)
                left += 1
            else:
                perm.append(right)
                right -= 1

        perm.append(left)
        return perm
