'''
Q[762]. Prime Number of Set Bits in Binary Representation

n = right - left
time : O(n)
space : O(1)
'''
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        '''count the number of a prime number of set bits
        Args:
            left(int): intger
            right(int): integer
            (1 <= left <= right <= 10 ** 6, 0 <= right - left <= 10 ** 4)
        Returns:
            int: the number of a prime number of set bits
        '''
        if not left or not right:
            raise ValueError('left and right should be [1, 10 ** 6]')

        prime_num = 0
        for i in range(left, right + 1):
            count_one = str(bin(i)).count('1')
            prime_num += self.is_prime(count_one)

        return prime_num


    def is_prime(self, num: int): -> int:
        '''determine whether num is prime number
        Args:
            num(int): integer
        Returns:
            int: 1 if num is prime number, 0 if num is not prime number
        '''
        if num == 1:
            return 0

        divisor = 0
        for i in range(2, num + 1):
            if num % i == 0:
                divisor += 1

        if divisor == 1:
            return 1

        return 0


#n = right - left
#time : O(n)
#space : O(1)
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        prime_list = [2, 3, 5, 7, 11, 13, 17, 19]
        prime_num = 0
        for i in range(left, right + 1):
            count_one = str(bin(i)).count('1')
            if count_one in prime_list:
                prime_num += 1

        return prime_num
