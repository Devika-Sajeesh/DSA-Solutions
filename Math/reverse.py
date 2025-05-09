class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Handle negative numbers by tracking the sign
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        # Reverse the digits
        reversed_x = int(str(x)[::-1])
        
        # Restore the sign
        reversed_x *= sign
        
        # Check for overflow within the 32-bit signed integer range
        if reversed_x < -2**31 or reversed_x > 2**31 - 1:
            return 0
        
        return reversed_x
