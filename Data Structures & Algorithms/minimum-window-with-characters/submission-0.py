from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #Approach: Sliding Window with 2 pointers (left, right) to find the min window
        # Use a hash map to count the chars and for the window
        if not t or not s:
            return ""
        
        # Count each character in t
        t_count = Counter(t)
        window_count = {}
        left = 0
        have, need = 0, len(t_count)
        res, res_len = [-1, -1], float("inf")

        # Expand the window
        for right in range(len(s)):
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1

            if char in t_count and window_count[char] == t_count[char]:
                have += 1 

            while have == need:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1
                window_count[s[left]] -= 1
                if s[left] in t_count and window_count[s[left]] < t_count[s[left]]:
                    have -= 1
                left += 1
        l, r = res
        return s[l:r+1] if res_len != float('inf') else ""
