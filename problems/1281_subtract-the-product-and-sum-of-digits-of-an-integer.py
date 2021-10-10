class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = str(n)
        length = len(n)
        digit = [int(n[i]) for i in range(length)]
        sum_digit = sum(digit)
        pro_digit = 1
        for i in digit:
            pro_digit *= i
        return pro_digit - sum_digit
