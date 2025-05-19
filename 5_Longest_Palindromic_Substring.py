class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def Palindrome(a):
            return a==a[::-1]
        if len(s)<=1:
            return s
        m = s[0]
        n = 1
        for i in range(len(s)):
            for j in range(len(s)-1,i,-1):
                c = s[i:j+1]
                if len(c)<n:
                    break
                if Palindrome(c)==True:
                    if len(c) > n:
                        m = c
                        n = len(c)
                        break
        return m
