from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Approach 1: Deque to store indices of useful elements for each window
        # then remove indices from the deque that are out of the current window
        # The front of the dequeu -> max element of the current window
        # Approach 2: Sliding Window with fixed size k + use max() operation to get the max number via 2 pointers (left, right)
        dq = deque()
        result = []

        for i in range(len(nums)):
            
            # Remove indices out of the current window
            if dq and dq[0] == i - k:
                dq.popleft()

            # Remove indices with values that are less than nums[i]
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # Add current index
            dq.append(i)

            # Append max for the window to result
            if i >= k - 1:
                result.append(nums[dq[0]])
        return result


