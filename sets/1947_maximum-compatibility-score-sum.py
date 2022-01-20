'''
Q[1947]. Maximum Compatibility Score Sum
'''

# n = len(students[i])
# m = len(students)
# time : O(n!)
# space : O(n)


from typing import List


class Solution:

    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        '''Return the sum of compatibility score
        Args:
            students(List[List[int]]): the array of the array of integers (1 <= len(students) <= 8, 1 <= len(students[i]) <= 8)
            mentors(List[List[int]]): the array of the array of integers (1 <= len(mentors) <= 8, 1 <= len(mentors[i]) <= 8)
        Returns:
            int: the sum of compatibility score
        '''
        if not students:
            raise ValueError('students should not be empty')

        if not mentors:
            raise ValueError('mentors should not be empty')

        self.n = len(students)
        self.m = len(students[0])
        self.students = students
        self.mentors = mentors

        return max(0, self.backtracking(0, set(), 0))

    def backtracking(self, idx: int, visited: set, comp_score_sum: int) -> int:
        '''backtrack
        Args:
            idx(int): index
            visited (set): visited index
            comp_score_sum: the sum of compatibility score
        '''
        if idx == self.n:
            return comp_score_sum

        max_comp_sum = float(-inf)

        for i, mentor in enumerate(self.mentors):
            if i in visited:
                continue

            comp_score = sum(int(a == b) for a, b in zip(self.students[idx], mentor))
            visited.add(i)
            comp_score_sum += comp_score

            max_comp_sum = max(max_comp_sum, self.backtracking(idx + 1, visited, comp_score_sum))
            visited.remove(i)
            comp_score_sum -= comp_score

        return max_comp_sum
