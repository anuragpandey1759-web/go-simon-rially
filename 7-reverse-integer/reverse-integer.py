class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Store the sign
        sign = -1 if x < 0 else 1

        # Work with positive number
        x = abs(x)

        result = 0

        while x > 0:
            digit = x % 10
            x //= 10

            result = result * 10 + digit

        # Put the sign back
        result *= sign

        # Check 32-bit integer range
        if result < INT_MIN or result > INT_MAX:
            return 0

        return result