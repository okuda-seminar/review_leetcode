import numpy as np
class Solution:
    def sumZero(self, n: int) -> List[int]:
        ret = np.arange(-(n//2), n//2+1).tolist()
        if n % 2 == 0:
            ret.remove(0)
        return ret
