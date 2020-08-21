class Stack:
    def __init__(self):
        super(Stack, self).__init__()
        self.array = []

    def push(self, value):
        self.array.append(value)

    def pop(self):
        if len(self.array) != 0:
            self.array.pop()

    def peek(self):
        return self.array[len(self.array)-1] if self.array != [] else None

myStack = Stack()

myStack.push(1);myStack.push(2);myStack.push(3)
myStack.pop()
print(myStack.peek())
