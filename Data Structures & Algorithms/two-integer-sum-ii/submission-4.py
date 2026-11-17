class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right = len(numbers) - 1
        left = 0
        pot_target = 0
        while left < right:
            left_elem = numbers[left]
            right_elem = numbers[right]
            pot_target = left_elem + right_elem
            if target == pot_target:
                return [left + 1, right + 1]
            if pot_target < target:
                left += 1
            if pot_target > target:
                right -= 1