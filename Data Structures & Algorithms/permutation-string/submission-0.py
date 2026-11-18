from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Approach 1: Sliding Window, Idea: Create set of s1 chars. Iterate through s2 and check for each char whether it is in set of s1. If so remove it from the set. If so, adjust the sliding window (left and right) and chec for the other letters. If set is empty, we have a solution. Do th above iteration until we iterated through s2.
        # Approach 2: Use two frequency arrays (s1 and s2), use sliding window of Len(s1) over s2
        n, m = len(s1), len(s2)
        # The case where s1 would bigger, so we return False right away
        if n > m:
            return False
        
        # Count characters 
        s1_count = Counter(s1)
        window_count = Counter(s2[:n])

        for i in range(m-n):
            if s1_count == window_count:
                return True
            window_count[s2[i]] -= 1
            if window_count[s2[i]] == 0:
                del window_count[s2[i]]
            window_count[s2[i+n]] += 1
        return s1_count == window_count


        

        