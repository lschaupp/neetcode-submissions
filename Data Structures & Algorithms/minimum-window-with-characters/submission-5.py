
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(s) < len(t):
            return ""

        t_counter = Counter(t)
        window_counter = {}

        l = 0
        have = 0
        need = len(t_counter)

        min_chars = ""
        min_length = float('inf')

        for r in range(len(s)):
            char = s[r]
            window_counter[char] = window_counter.get(char, 0) + 1

            # A character's required frequency is satisfied
            if char in t_counter and window_counter[char] == t_counter[char]:
                have += 1

            # Shrink as long as window remains valid
            while have == need:
                if r - l + 1 < min_length:
                    min_length = r - l + 1
                    min_chars = s[l:r+1]

                left_char = s[l]
                window_counter[left_char] -= 1

                # A required frequency is no longer satisfied
                if left_char in t_counter and window_counter[left_char] < t_counter[left_char]:
                    have -= 1

                l += 1

        return min_chars
