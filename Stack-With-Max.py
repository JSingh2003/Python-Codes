class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.max_stack or value >= self.max_stack[-1]:
            self.max_stack.append(value)

    def pop(self):
        if not self.stack:
            raise IndexError("Stack is empty")
        if self.stack[-1] == self.max_stack[-1]:
            self.max_stack.pop()
        return self.stack.pop()

    def get_max(self):
        if not self.max_stack:
            raise IndexError("Stack is empty")
        return self.max_stack[-1]

max_stack = MaxStack()
max_stack.push(5)
max_stack.push(2)
max_stack.push(10)

print(max_stack.get_max())  

max_stack.pop()
print(max_stack.get_max())