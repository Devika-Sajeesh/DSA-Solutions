class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # Handle edge case for division by zero
        if divisor == 0:
            raise ValueError("Cannot divide by zero")

        # Handle the edge case of overflow
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1  # The result would overflow a 32-bit signed integer

        # Determine the sign of the result
        sign = 1 if (dividend >= 0) == (divisor >= 0) else -1
        
        # Use absolute values for the division
        dividend, divisor = abs(dividend), abs(divisor)
        
        result = 0
        while dividend >= divisor:
            temp_divisor, num_divisors = divisor, 1
            while dividend >= (temp_divisor << 1):  # Double the divisor
                temp_divisor <<= 1
                num_divisors <<= 1

            # Subtract the largest multiple of divisor that fits into dividend
            dividend -= temp_divisor
            result += num_divisors

        # Apply the sign to the result
        return sign * result
