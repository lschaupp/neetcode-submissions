class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash_map = {'(': ')','{': '}', '[':']'}
        if len(s) <= 1:
            print("i am here", len(stack))
            return False
        for char in s:
            if char in hash_map:
                stack.append(hash_map[char])
            else:
                if not stack or stack.pop() != char:
                    return False
        return not stack


        