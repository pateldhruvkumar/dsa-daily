class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
myStack = Stack()

myStack.push(1)
myStack.push(2)
myStack.push(3)

print(myStack.stack)
print(myStack.pop())
print(myStack.peek())
print(myStack.size())
print(myStack.isEmpty())