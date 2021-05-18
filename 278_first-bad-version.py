# n = n
# time = O(logn)
# space = O(1)
# done time = 5m


class Solution:

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n + 1

        while left < right:
            mid = left + right >> 1
            comp = isBadVersion(mid)

            if comp:
                right = mid
            else:
                left = mid + 1

        return right
