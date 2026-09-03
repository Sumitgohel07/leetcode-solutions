class MinStack:

    def __init__(self):
        self.stack = []
        self.m_stack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        
        if not self.m_stack or value <= self.m_stack[-1]:
            self.m_stack.append(value)
        
    def pop(self) -> None:
        if self.stack[-1] == self.m_stack[-1]:
            self.m_stack.pop()

        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.m_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()