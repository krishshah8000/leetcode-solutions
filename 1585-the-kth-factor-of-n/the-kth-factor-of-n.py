class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        factor = []
        for i in range(1,n+1):
            if n%i==0:
                factor.append(i)

        if k<=len(factor):
            return factor[k-1]

        return -1