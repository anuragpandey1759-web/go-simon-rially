from collections import Counter

class Solution:
    def longestSubstring(self, s, k):
        if len(s) < k:
            return 0

        count = Counter(s)

        # Find a character whose frequency is less than k
        for i, ch in enumerate(s):
            if count[ch] < k:
                # Split around this invalid character
                left = self.longestSubstring(s[:i], k)
                right = self.longestSubstring(s[i + 1:], k)

                return max(left, right)

        # Every character occurs at least k times
        return len(s)