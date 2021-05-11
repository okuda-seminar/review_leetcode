# n = s.length
# time = O(nlogn)
# space = O(n)
# done time = 15m


class Solution:

    def repeatedSubstringPattern(self, s: str) -> bool:
        def make_divisors(n):
            lower_divisors, upper_divisors = [], []
            divisor = 1
            while divisor * divisor <= n:
                if n % divisor == 0:
                    lower_divisors.append(i)
                    if divisor != n // divisor:
                        upper_divisors.append(n//divisor)
                divisor += 1
            return lower_divisors + upper_divisors[::-1]

        N = len(s)
        divs = make_divisors(N)

        for d in divs:
            if d == N:
                return False
            if s[: d] * (N // d) == s:
                return True
