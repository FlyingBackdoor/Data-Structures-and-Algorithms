class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class dLinkedList:
    """docstring for DLinkedList."""

    def __init__(self, value):
        super(dLinkedList, self).__init__()
        self.value = value
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def printList(self):
        listData = []
        current_node = self.head

        while current_node != None:
            listData.append(current_node.value)
            current_node = current_node.next

        return listData

    def append(self, value):
        new_node = Node(value)
        self.tail.previous = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head.previous = new_node
        self.head = new_node
        self.length += 1

    def traverseToPoint(self, position):
        node = self.head
        for i in range(position):
            node = node.next
        return node

    def insert(self, position, value):
        if position == 0:
            self.prepend(value)
            return 1
        elif position >= self.length:
            self.append(value)
            return 1

        new_node = Node(value)
        leader_node = self.traverseToPoint(position-1)
        follower = leader_node.next
        leader_node.next = new_node
        new_node.previous = leader_node
        new_node.next = follower
        follower.previous = new_node
        
        self.length += 1

    def remove(self, position):
        if position> self.length:
            return "Index out of range"
        elif position in [0, 1]:
            self.head = self.head.next
            self.length -= 1
            return 0
        else:
            leader_node = self.traverseToPoint(position-2)
            pointer = leader_node.next
            pointer = pointer.next
            prevPointer = pointer.previous
            leader_node.next = pointer
            leader_node.previous = prevPointer
            self.length -= 1

if __name__ == '__main__':
    object = dLinkedList(10)

    object.append(11)
    object.append(12)
    object.prepend(9)
    object.insert(2, "zero")
    object.prepend(8)
    print(object.printList())

    object.remove(4)
    object.remove(0)
    object.remove(4)

    print(object.printList())
    print("Length:", object.length)
