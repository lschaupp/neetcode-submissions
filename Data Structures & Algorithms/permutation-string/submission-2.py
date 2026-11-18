from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Approach 1: Hash Maps of s1 and s2 to count char frequencies + Sliding Window. Both pointers start at 0, length of sliding window is len(s1), stop when window reached end of s2.
        m,n = len(s1), len(s2)
        left, right = 0,m
        if m > n:
            return False
        window_size = m
        counter1 = Counter(s1)
        counter2 = Counter(s2[left:right])
        while right <= n:
            if counter1 == counter2:
                return True
            if right == n:
                break
            counter2[s2[left]] -= 1
            if counter2[s2[left]] == 0:
                del counter2[s2[left]]
            counter2[s2[right]] += 1
            right += 1
            left += 1
        return False
            
            




        

        