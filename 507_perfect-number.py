# n = num
# time = O(logn)
# space = O(logn)
# done time = 10m


class Solution:

    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False

        divisors = [1]
        div = 2
        while div ** 2 < num:
            if num % div == 0:
                divisors.append(div)
                if div != num // div:
                    divisors.append(num // div)
            div += 1

        return num == sum(divisors)
