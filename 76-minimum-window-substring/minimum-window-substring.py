from collections import Counter

class Solution:
    def minWindow(self, s, t):
        if len(t) > len(s):
            return ""

        # Frequency of characters required from t
        need = Counter(t)

        window = {}
        have = 0
        required = len(need)

        left = 0
        min_len = float('inf')
        min_start = 0

        for right in range(len(s)):
            char = s[right]

            # Add current character to window
            window[char] = window.get(char, 0) + 1

            # Character requirement is now completely satisfied
            if char in need and window[char] == need[char]:
                have += 1

            # Try shrinking the window
            while have == required:
                # Update minimum window
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left

                # Remove leftmost character
                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1

        if min_len == float('inf'):
            return ""

        return s[min_start:min_start + min_len]