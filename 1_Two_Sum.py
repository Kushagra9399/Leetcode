class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = []
        for i in range(len(nums)-1):
            if target-nums[i] in nums[i+1:]:
                return [i, nums[i+1:].index(target-nums[i])+i+1]
