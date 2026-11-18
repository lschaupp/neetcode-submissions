class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Approach 1: Sliding Window Approach with 2 pointers, both pointers start at 0. Then increase pointer B and add the char to the subarray. Check if the char is already within the subarray. If so, move the first pointer A +1 (or more until duplicate is removed) and remove the char. Stop when the 
        left, right = 0,0
        subarray = set()
        max_length = 0
        while right < len(s):
            left_element = s[left]
            right_element = s[right]
            while right_element in subarray:
                subarray.remove(s[left])
                left += 1
            subarray.add(right_element)
            right += 1
            max_length = max(len(subarray), max_length)
        return max_length

        


        