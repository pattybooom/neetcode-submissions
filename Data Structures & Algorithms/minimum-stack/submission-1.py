class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        print(f"pushed {val}: {self.stack}")
        
    def pop(self) -> None:
        v = self.stack.pop(len(self.stack)-1)
        print(f"popped {v}: {self.stack}")
        return v

    def top(self) -> int:
        print(self.stack[-1])
        print(f"top is {self.stack[-1]}: {self.stack}")
        return self.stack[-1]
        

    def getMin(self) -> int:
        min = self.stack[-1]
        for x in self.stack:
            if x < min:
                min = x
        print(f"min is {min}: {self.stack}")
        return min
        
