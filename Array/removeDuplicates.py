class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        # Initialize a pointer to track the position of the unique elements
        unique_index = 1
        
        # Start from the second element and compare with the previous one
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[unique_index] = nums[i]
                unique_index += 1
        
        return unique_index  # Return the number of unique elements
