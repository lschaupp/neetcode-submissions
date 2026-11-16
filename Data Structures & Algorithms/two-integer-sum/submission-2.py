class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n1 in enumerate(nums):
            for j, n2 in enumerate(nums):
                if i != j:
                    summed = nums[i] + nums[j]
                    if summed == target:
                        return [i,j]
        