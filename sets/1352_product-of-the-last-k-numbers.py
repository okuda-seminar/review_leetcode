#
# @lc app=leetcode id=1352 lang=python3
#
# [1352] Product of the Last K Numbers
#

# @lc code=start
class ProductOfNumbers:

    def __init__(self):
        """Initialize data structure
        """
        self.product = [1]

    def add(self, num: int) -> None:
        """Appends the integer num to the stream

        Args:
            x(int): integer
        """
        if num == 0:
            self.product = [1]
        else: 
            self.product.append(self.product[-1] * num)

    def getProduct(self, k: int) -> int:
        """Return the product

        Args:
            k(int): integer

        Returns:
            int: the product of the last k numbers in the current list
        """
        if len(self.product) <= k:
            return 0
        
        return self.product[-1] // self.product[-(k+1)]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
# @lc code=end
