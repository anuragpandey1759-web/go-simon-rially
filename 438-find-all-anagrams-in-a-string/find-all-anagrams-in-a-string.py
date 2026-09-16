class Solution:
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []

        # Frequency of characters in p
        need = [0] * 26

        for ch in p:
            need[ord(ch) - ord('a')] += 1

        window = [0] * 26
        result = []

        left = 0

        for right in range(len(s)):
            # Add current character
            window[ord(s[right]) - ord('a')] += 1

            # Keep window size equal to len(p)
            if right - left + 1 > len(p):
                window[ord(s[left]) - ord('a')] -= 1
                left += 1

            # Check if current window is an anagram
            if right - left + 1 == len(p) and window == need:
                result.append(left)

        return result