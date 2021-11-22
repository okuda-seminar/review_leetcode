'''
Q[1807]. Evaluate the Bracket Pairs of a String
'''

# n = len(s)
# time : O(n)
# space : O(n)


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        '''Replace key
        Args:
            s(str): string
            knowledge(List[List[str]]): 2D string array (knowledge[i] = [key, value])
        Returns:
            str: replaced string
        '''
        if not s:
            raise ValueError('s length should be [1, 10**5]')

        knowledge_dict = {x[0] : x[1] for x in knowledge}
        stack = []
        replaced_s = []
        is_in_parenthesis = False

        for c in s:
            if not is_in_parenthesis:
                if c == '(':
                    is_in_parenthesis = True
                    continue

                replaced_s.append(c)
            else:
                stack.append(c)
                if c == ')':
                    key = ''.join(stack)[:-1]
                    replaced_s.append(knowledge_dict.get(key, '?'))
                    stack.clear()
                    is_in_parenthesis = False

        return ''.join(replaced_s)
