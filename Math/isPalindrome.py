class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Negative numbers are not palindromes
        if x < 0:
            return False
        
        # Convert the number to a string and check if it's the same forward and backward
        return str(x) == str(x)[::-1]
