class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Approach 1: 2 Pointers (Sliding Window). Both pointers start at the beginning. Right Pointer moves forward and appends the letter to a subarray. If the letter is the same, add it. If not, change the letter (up to k times within the subarryay). Wehn we hit k, move the left pointer forward to the element such k goes down one. (while k > 2 loop). Stop: Stop when the right pointer reaches the end (len s)). Update max length variable (store the max subarray lengtyh). Use a hash map to count the frequency of the letter. Change the most dominant one.
        count = defaultdict(int)
        max_count = 0
        left = 0
        right = 0
        max_length = 0

        for right in range(len(s)):
            count[s[right]] += 1
            max_count = max(max_count, count[s[right]])

            while right - left + 1 - max_count > k:
                count[s[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length





        
        