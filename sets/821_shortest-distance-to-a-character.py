Q[821]. Shortest Distance to a Character

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        '''compute the distance between s[i] and c
        Args:
            s(str): string consist of lowercase (1 <= len(s) <= 10^4)
            c(str): standard string
        Returns:
            List[int]: the distance between s[i] and c
        '''
        if not s or not c:
            return []

        standard_idx = []
        for i in range(len(s)):
            if s[i] == c:
                standard_idx.append(i)
        
        # n = len(s)
        # time : O(n^2)
        # space : O(n)
        ans = []
        for i in range(len(s)):
            ans.append(min([abs(a - i) for a in standard_idx]))

        return ans

        # n = len(s)
        # time : O(n)
        # space : O(n)
        ans = [0] * len(s)
        idx = 0
        for i in range(len(s)):
            if i < standard_idx[0]:
                ans[i] = standard_idx[0] - i
            elif i > standard_idx[-1]:
                ans[i] = i - standard_idx[-1]
            elif i == standard_idx[idx]:
                idx += 1
            else:
                ans[i] = min(standard_idx[idx] - i, i - standard_idx[idx - 1])
        return ans
