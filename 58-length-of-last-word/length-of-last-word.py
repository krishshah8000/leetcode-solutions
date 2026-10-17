class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        x = s[::-1].strip()
        c=0
        for i in x:
            if i == " ":
                break
            else:
                c+=1
        return c