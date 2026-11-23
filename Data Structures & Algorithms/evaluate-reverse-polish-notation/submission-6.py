class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        final = 0
        stack = []
        arith = ["+", "-", "*", "/"]
        for token in tokens:
            if token in arith:
                # Take the current stack and calc
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    final = a + b
                elif token == "-":
                    final = a - b
                elif token == "*":
                    final = a * b
                elif token == "/":
                    final = int(a / b)
                stack.append(final)
            else:
                stack.append(int(token))
        return stack[-1]
        