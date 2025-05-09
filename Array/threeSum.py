class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array to easily skip duplicates
        result = []  # To store the triplets
        
        for i in range(len(nums) - 2):  # Iterate through the array
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate elements for the first element
            
            left, right = i + 1, len(nums) - 1  # Set up two pointers
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for the second and third numbers in the triplet
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1  # We need a larger sum
                else:
                    right -= 1  # We need a smaller sum
        
        return result
