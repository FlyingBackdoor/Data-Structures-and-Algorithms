class Node:
    def __init__(self, value):
        super(Node, self).__init__()
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        super(Queue, self).__init__()
        self.first = None
        self.last = None
        self.length = 0


    def isEmpty(self):
        return True if self.last is None else False


    def peek(self):
        return self.last

    def enqueue(self, value):
        node = Node(value)

        if self.length == 0:
            self.first = node
            self.last = self.first
            self.length += 1

        self.last.next = node
        self.length += 1


    def dequeue(self):
        self.first.

myQueue = Queue()

myQueue.enqueue("Amar");
myQueue.enqueue("Akbar");
myQueue.enqueue("Anthony")
print(myQueue.peek().value)
