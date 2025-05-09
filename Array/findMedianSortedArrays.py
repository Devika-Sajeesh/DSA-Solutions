class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Combine both arrays and sort them
        nums3 = nums1 + nums2
        nums3.sort()

        # If the combined list length is odd, return the middle element
        if len(nums3) % 2 == 1:
            return nums3[len(nums3) // 2]
        else:
            # If the length is even, return the average of the two middle elements
            mid = len(nums3) // 2
            return (nums3[mid - 1] + nums3[mid]) / 2.0
