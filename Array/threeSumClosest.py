class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()  # Sort the array to use two-pointer technique
        closest_sum = float('inf')  # Initialize closest_sum to infinity
        
        for i in range(len(nums) - 2):  # Loop through the array (up to the 3rd last element)
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate elements to avoid checking the same triplet
            
            left, right = i + 1, len(nums) - 1  # Two pointers
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # If the current sum is closer to the target, update closest_sum
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                if current_sum < target:
                    left += 1  # Move left pointer to the right to increase the sum
                elif current_sum > target:
                    right -= 1  # Move right pointer to the left to decrease the sum
                else:
                    # If the sum is exactly equal to the target, we can return it immediately
                    return current_sum
        
        return closest_sum  # Return the closest sum after checking all possible triplets
