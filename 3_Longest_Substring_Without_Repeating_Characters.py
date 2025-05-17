class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = []
        l = []
        for i in range(len(s)):
            if a==[]:
                a.append(s[i])
            elif s[i] not in a:
                a.append(s[i])
            elif s[i] in a:
                b = a.index(s[i])
                l.append(len(a))
                a = a[b+1:]
                a.append(s[i])
        l.append(len(a))
        return max(l)
