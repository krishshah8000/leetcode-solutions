class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        c=0
        l = len(s)
        for i in range(l):
            for j in range(i+1,l+1):
                x = s[i:j]
                if x == x[::-1]:
                    c+=1

        return c