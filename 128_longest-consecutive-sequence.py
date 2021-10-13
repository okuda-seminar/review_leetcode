#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # use sorting
        """
        time: O(nlongn)
        space: O(1)

        if not nums:
            return 0

        nums.sort()
        print(nums)
        corr_len = 1
        max_len = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                corr_len += 1
            elif nums[i] != nums[i - 1]:
                max_len = max(corr_len, max_len)
                corr_len = 1
        return max(corr_len, max_len)
        """

        # use set
        """
        time: O(n)
        space: O(n)
        """
        if not nums:
            return 0

        nums = set(nums)
        max_len = 1
        for num in nums:
            corr_len = 1
            if not num - 1 in nums:
                curr_num = num

                while curr_num + 1 in nums:
                    corr_len += 1
                    curr_num += 1

                max_len = max(corr_len, max_len)

        return max_len

        # use UnionFind
        """
        time: O(n^2)
        space: O(n)

        if not nums:
            return 0

        uf = UnionFind()
        for num in nums:
            uf.add(num)
        return uf.maxSize()

class UnionFind:
    def __init__(self):
        self.par = {} #親
        self.rank = {} #根の深さ

    #xの属する木の根を求める
    def find(self, x: int) -> int:
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    #xとyの属する集合のマージ
    def unite(self, x: int, y: int) -> None:
        x = self.find(x)
        y = self.find(y)
        if x != y:
            self.par[x] = y
            self.rank[y] += self.rank[x]

    #xを集合に加える
    def add(self, x: int) -> None:
        if x in self.par:
            return
        self.par[x] = x
        self.rank[x] = 1
        if x - 1 in self.par:
            self.unite(x, x - 1)
        if x + 1 in self.par:
            self.unite(x, x + 1)

    #最大の根の深さを調べる
    def maxSize(self) -> int:
        return max(self.rank.values(), default=0)
            """
# @lc code=end
