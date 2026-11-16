class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = []
        for i, num in enumerate(nums):
            sorted_nums.append([num, i])
        sorted_nums.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            summed = sorted_nums[left][0] + sorted_nums[right][0]
            if summed == target:
                return sorted([sorted_nums[left][1], sorted_nums[right][1]])
            elif summed < target:
                left += 1
            elif summed > target:
                right -= 1
        return []
        