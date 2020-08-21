class Node:
    def __init__(self, value):
        super(Node, self).__init__()
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def isEmpty(self): #check if stack is empty or not
         return True if self.top is None and self.length == 0 else False

    def push(self, value): #insert new item at top
        self.bottom = self.top
        self.top = Node(value)
        self.top.next = self.bottom
        self.length += 1

    def pop(self): #remove top item
        if not self.isEmpty():
            self.top = self.top.next
            if self.bottom.next is None:
                self.length -=1
                return 0
            self.bottom = self.bottom.next
            self.length -= 1
        else:
            pass

    def peek(self): #this will return the top value of stack
        return self.top.value if self.top is not None else None

    #optional
    def printStack(self):
        listData = []
        current_node = self.top
        while current_node != None:
            listData.append(current_node.value)
            current_node = current_node.next
        print(listData)


myStack = Stack()
myStack.push("Java")
myStack.push("Kotlin")
myStack.push("Python")

myStack.pop();myStack.pop();myStack.pop();myStack.pop()


print(myStack.peek())
print(myStack.length)
