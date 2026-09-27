from collections import Counter

class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        if total_len > len(s):
            return []

        target = Counter(words)
        ans = []

        for offset in range(word_len):
            left = offset
            count = 0
            seen = {}

            for right in range(offset, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word not in target:
                    seen.clear()
                    count = 0
                    left = right + word_len
                    continue

                seen[word] = seen.get(word, 0) + 1
                count += 1

                while seen[word] > target[word]:
                    left_word = s[left:left + word_len]
                    seen[left_word] -= 1
                    left += word_len
                    count -= 1

                if count == word_count:
                    ans.append(left)

                    left_word = s[left:left + word_len]
                    seen[left_word] -= 1
                    left += word_len
                    count -= 1

        return ans
      