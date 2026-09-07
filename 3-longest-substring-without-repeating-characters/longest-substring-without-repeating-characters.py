class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            # Remove duplicates
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])

            # Update maximum length
            max_length = max(max_length, right - left + 1)

        return max_length
