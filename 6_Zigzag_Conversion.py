class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        l = ["" for _ in range(numRows)]
        if numRows==2:
            for i in range(len(s)):
                if i%2==0:
                    l[0] += s[i]
                else:
                    l[1] += s[i]
            return "".join(l)
        rev = False
        idx = 0
        for i in s:
            if rev==False:
                l[idx] += i
                idx += 1
                if idx == numRows:
                    rev = True
                    idx = numRows - 2
            else:
                l[idx] += i
                idx -= 1
                if idx == 0:
                    rev = False
        return "".join(l)
