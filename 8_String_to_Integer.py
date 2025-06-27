class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        start = 0
        valid = [' ','+','-',"1",'2','3','4','5','6','7','8','9','0']
        for i in s:
            if i in valid:
                if i==" ":
                    start += 1
                else:
                    break
            else:
                return 0
        pos = 1
        digit = ["1",'2','3','4','5','6','7','8','9','0']
        if start==len(s):
            return 0
        if s[start]=="-":
            pos = -1
            start += 1
        elif s[start]=="+":
            start += 1
        num = "0"
        if start==len(s):
            return 0
        for i in range(start,len(s)):
            if s[i] not in digit:
                break
            else:
                num += s[i]
        num = int(num)*pos
        if num >= 2**31 -1:
            return 2**31 - 1
        elif num <= -2**31:
            return -2**31
        else:
            return num