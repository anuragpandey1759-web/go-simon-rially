class Solution:
    def countCommas(self, n: int) -> int:
        # Every number from 1,000 to n has at least one comma.
        if n < 1000:
            return 0

        ans = n - 999

        # Numbers >= 1,000,000 have a second comma.
        if n >= 1_000_000:
            ans += n - 999_999

        # Given n <= 10^5, this second part is never needed,
        # but the logic is included for completeness.
        return ans
