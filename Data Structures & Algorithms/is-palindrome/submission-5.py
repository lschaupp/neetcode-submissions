class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Approach 1: lower(), clear non alphanumeric chars + reverse(), check if strings are matching (each O(n) -> O(3n)) probably
        # Approach 2: Two pointers (one left, one right, check each letter) Time: (O(n)) -> Skiup specia chars (Space/?, etc...)
        right = len(s) - 1
        for left, elem_left in enumerate(s):
            # Check whether elem is alphanumeric or not (Cleanup)
            elem_left = elem_left.lower()
            if not elem_left.isalnum():
                continue
            elem_right = s[right].lower()
            while left < right and not s[right].isalnum():
                right -= 1
            if left >= right:
                return True
            elem_right = s[right].lower()
            if elem_left != elem_right:
                return False
            right -= 1
        return True





        