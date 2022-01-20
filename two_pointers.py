from typing import List


# 1. Reverse an array in place
def reverse_array(array: List[int]) -> None:
    start, end = 0, len(array) - 1
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1


"""
if __name__ == "__main__":
    array = [10, 20, 30, 40, 50]
    reverse_array(array)
    assert array == [50, 40, 30, 20, 10], "bad"
"""


# 2. Sorted an array of the squares of each number sorted 
#.   in non-decreasing order
def sorted_squares(nums: List[int]):
    n = len(nums)
    start, end = 0, n - 1
    res = [0] * n
    idx = n - 1
    while end > -1 and idx > -1:
        if abs(nums[start]) > abs(nums[end]):
            res[idx] = nums[start] * nums[start]
            start += 1
        else:
            res[idx] = nums[end] * nums[end]
            end -= 1
        idx -= 1
    return res


"""
if __name__ == "__main__":
    array = [-4, -3, 0, 1, 10]
    assert sorted_squares(array) == [0, 1, 9, 16, 100], "bad"
"""


# 3. Finding cycle in Linked list
class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None

    def __repr__(self):
        return str(self.val)


def has_cycle(root):
    if root is None or root.next is None:
        return False
    
    p1 = root
    p2 = root.next
    while p2:
        p2 = p2.next
        if p2:
            p2 = p2.next
        else:
            return False
        
        p1 = p1.next
        if p1 == p2:
            return True


"""
if __name__=="__main__":
    lt = [ListNode(item) for item in [3, 2, 0, -4]]
    root = lt[0]
    root.next = lt[1]
    lt[1].next = lt[2]
    lt[2].next = lt[3]
    lt[3].next = lt[1]
    assert has_cycle(root), "bad"
"""


# 4. Find the length of the longest substring without repeating characters
def length_of_logest_substring(s: str) -> int:
    seen = set()
    n = len(s)
    right = -1
    res = 0
    for left in range(n):
        # if s[right + 1] in seen, update left
        while right + 1 < n and s[right + 1] not in seen:
            right += 1
            seen.add(s[right])
        res = max(res, right - left + 1)
        if right == n - 1:
            break
        seen.discard(s[left])
    return res


"""
if __name__ == "__main__":
    assert length_of_logest_substring("aabcbcabc") == 3, "bad"
"""


# 5. Calculate the minimum absolute difference between the maximum and 
#    minimum number of any triplet A[i], B[j], C[k]
def minimum_absolute_difference(A: List[int], B: List[int], C: List[int]) -> int:
    i, j, k = 0, 0, 0
    l, m, n = len(A), len(B), len(C)
    min_diff = abs(max(A[i], B[j], C[k]) - min(A[i], B[j], C[k]))
    while i < l and j < m and k < n:
        curr_diff = abs(max(A[i], B[j], C[k]) - min(A[i], B[j], C[k]))
        min_diff = min(min_diff, curr_diff)
        min_term = min(A[i], B[j], C[k])
        if A[i] == min_term:
            i += 1
        elif B[j] == min_term:
            j += 1
        else:
            k += 1
    return min_diff


"""
if __name__ == "__main__":
    A = [1, 4, 5, 8, 10]
    B = [6, 9, 15]
    C = [2, 3, 6, 6]
    assert minimum_absolute_difference(A, B, C) == 1, "bad"
"""


# 6. Find two lines, which, together with the x-axis forms a container
def max_area(height):
    l = 0
    r = len(height) - 1
    max_area = 0
    while l < r:
        base = r - l
        if height[r] >= height[l]:
            h = height[l]
            l += 1
        else:
            h = height[r]
            r -= 1
        if h * base > max_area:
            max_area = h * base
    return max_area


"""
if __name__ == "__main__":
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49, "bad"
"""