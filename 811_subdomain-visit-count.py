# N = len(nums)
# M = len(domain)
# time: O(NM)
# space: O(NM)

from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ret = defaultdict(int)
        for domain in cpdomains:
            count, domain = domain.split()
            count = int(count)
            frags = domain.split('.')
            for i in range(len(frags)):
                ret[".".join(frags[i:])] += count

        return ["{} {}".format(ct, dom) for dom, ct in ret.items()]
