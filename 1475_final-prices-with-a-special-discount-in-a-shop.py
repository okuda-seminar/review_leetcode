class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ret = []
        for i in range(len(prices)):
            if i == len(prices) - 1:
                ret.append(prices[-1])
                break
            for j in range(i+1, len(prices)):
                if prices[i] >= prices[j]:
                    ret.append(prices[i]-prices[j])
                    break
            if i+1 != len(ret):
                ret.append(prices[i])
        return ret
