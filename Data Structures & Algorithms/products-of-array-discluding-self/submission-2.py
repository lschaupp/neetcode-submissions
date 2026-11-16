class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Approach 1: Naive: Iteratore thoruhg array and multiply each number, Time: O(n2)
        # Approach 2: Calculate only the first product, then use divison to calculate the next ones (48, 24, 12, 8), Time: O(n), Issue: 0 division
        # Approach 3: Prefix multiply, calc left and right multiplciaton, then use both arrays and multiply each elemenet. Time O(n)
        left_multiply = [1] * len(nums)
        right_multiply = [1] * len(nums)
        final = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            right_multiply[i] = right_multiply[i+1] * nums[i+1]
        for i in range(1, len(nums)):
            left_multiply[i] = left_multiply[i-1] * nums[i-1]
        for i, num in enumerate(nums):
            final[i] = left_multiply[i] * right_multiply[i]
        return final



            
        