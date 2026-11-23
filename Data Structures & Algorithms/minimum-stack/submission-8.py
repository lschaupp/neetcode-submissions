class MinStack:

    def __init__(self):
        self.stack = []
        self.min = [float('inf')]
        self.hash_map = {}
        

    def push(self, val: int) -> None:
        if val <= self.min[-1]:
            self.min.append(val)
        self.stack.append(val)
        

    def pop(self) -> None:
        # Update the min value during pop
        num = self.stack.pop()
        print(num)
        if num == self.min[-1]:
            print("Pop min", num, self.min[-1])
            self.min.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min[-1]

        
