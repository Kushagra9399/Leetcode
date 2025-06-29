class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        c = 0
        left = 0
        right = len(height)-1
        diff = len(height)-1
        while left < right:
            if height[left] < height[right]:
                area = (diff)*height[left]
                c = max(c, area)
                left += 1
            else:
                area = (diff)*height[right]
                c = max(c, area)
                right -= 1
            diff -= 1
        return c