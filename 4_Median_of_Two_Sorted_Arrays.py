class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        med = 0.0
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1)%2==0:
            a = len(nums1)//2
            med = (nums1[a]+nums1[a-1])/2.0
        else:
            med = nums1[len(nums1)//2]
        return med
