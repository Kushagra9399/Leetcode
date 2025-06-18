class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = False
        if x < 0:
            neg = True
        if neg:
            x = int(str(x)[1:][::-1])*-1
        else:
            x = int(str(x)[::-1])
        if x > 2**31 -1 or x < -2**31:
            return 0
        return x
