class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Approach 1: Sort the array, then use two pointers (Time O(n log n for sorting, use three pointers, start left at 0 and at the end. Add to target (which is 0), if above or below the target adjust the third pointer. If no goal reached, then adjust depending whether target is baove or below, the firsst or the 2nd pointer. Then repeat.
        finals = []
        nums.sort()
        print(nums)
        for idx, fixed in enumerate(nums):
            if idx > 0 and fixed == nums[idx - 1]:
                continue
            left = idx + 1
            right = len(nums) - 1
            while left < right:
                target = nums[left] + nums[right] + nums[idx]
                if target == 0:
                    finals.append([nums[idx], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                if target < 0:
                    left += 1
                if target > 0:
                    right -= 1
        return finals