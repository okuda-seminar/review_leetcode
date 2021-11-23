'''
Q[1625]. Lexicographically Smallest String After Applying Operations
'''


# n = len(s)
# time : O(n**2)
# space : O(n)


from collections import deque


class Solution:

    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        '''Return the smallest number after adding or rotating
        Args:
            s(str): string (2 <= len(s) <= 100)
            a(int): number to add (1 <= a <= 9)
            b(int): number to rotate (1 <= b <= len(s) - 1)
        Returns:
            str: the smallest number after adding or rotating
        '''
        if not s:
            raise ValueError('s length should be [2, 100]')

        if len(s) % 2 != 0:
            raise ValueError('s length should be even')

        stack = deque([list(s)])
        min_num = s
        s_dict = {s : True}

        while stack:
            cur_num = stack.pop()
            rotate_num = cur_num[-b:] + cur_num[:-b]
            add_num = []
            for i in reversed(range(len(cur_num))):
                if i % 2 == 1:
                    cur_num[i] = int(cur_num[i]) + a
                    if cur_num[i] > 9:
                        cur_num[i] -= 10
                add_num.append(str(cur_num[i]))

            add_num = add_num[::-1]
            add_num = ''.join(add_num)
            rotate_num = ''.join(rotate_num)
            min_num = min(min_num, add_num, rotate_num)

            if add_num not in s_dict:
                s_dict[add_num] = True
                stack.append(list(add_num))
            if rotate_num not in s_dict:
                s_dict[rotate_num] = True
                stack.append(list(rotate_num))
            else:
                continue

        return min_num


# time : O(n**2)
# space : O(n)


class Solution:

    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        self.stack = set()
        self.a = a
        self.b = b
        self.dfs(s)
        return min(self.stack)

    def dfs(self, s: str) -> None:
        '''Traversing strings
        Args:
            s(str): string
        '''
        if s in self.stack:
            return None

        self.stack.add(s)
        self.dfs(s[-self.b:] + s[:-self.b])
        self.dfs("".join([str((int(s[i]) + self.a*(i % 2)) % 10) for i in range(len(s))]))
