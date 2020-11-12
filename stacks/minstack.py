"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

"""

class minStack:
    
    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    def push(self,x):
        if len(self.min_stack) == 0 or self.min_stack[-1] <= x:
            self.min_stack.append(x)
        self.stack.append(x)
        
    def pop(self):
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()
        
    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.min_stack[-1]