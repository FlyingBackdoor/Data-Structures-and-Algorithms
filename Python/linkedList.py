class LinkedList:
    """docstring for LinkedList."""

    def __init__(self, value):
        super(LinkedList, self).__init__()
        self.value = value
        self.head = {"value": self.value,
                     "next": None}
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = {"value": value, "next": None}
        self.tail["next"] = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        '''currentTail = self.tail #storing current data
        self.tail = self.head #setting tail to begining

        new_node = {"value": value, "next": self.tail} #this is new data

        self.head = new_node #adding new node at start and previous will follow it
        self.tail = currentTail #changing the tail value so if new append used it wont override data
        self.length +=1'''

        #andre solution
        new_node = {"value": value, "next": None}
        new_node['next'] = self.head
        self.head = new_node
        self.length += 1

    def printList(self):
        listData = []
        current_node = self.head

        while current_node != None:
            listData.append(current_node["value"])
            current_node = current_node["next"]

        return listData

    def traverseToPoint(self, position):
        node = self.head

        for i in range(position):
            node = node["next"]

        return node

    def insert(self, position, value):
        if position == 0:
            self.prepend(value)
            return 1
        elif position >= self.length:
            self.append(value)
            return 1

        new_node = {"value": value, "next": None}

        leader_node = self.traverseToPoint(position-1)
        #print("leader:", leader_node)
        holdingPointer = leader_node["next"]
        #print("hoaldingP:", holdingPointer)

        leader_node['next'] = new_node

        #print("leader after:", leader_node)
        new_node['next'] = holdingPointer
        self.length += 1

    def remove(self, position):
        if position> self.length:
            return "Index out of range"
        elif position in [0, 1]:
            self.head = self.head["next"]
            self.length -= 1
            return 0
        else:
            leader_node = self.traverseToPoint(position-2)
            pointer = leader_node["next"]
            pointer = pointer["next"]
            leader_node["next"] = pointer
            self.length -= 1

    def reversed(self):





myLL = LinkedList(12)
myLL.append(13)

myLL.prepend(11)

myLL.append(14)

myLL.prepend(10)
myLL.append(15)

myLL.prepend(9)
myLL.append(16)

myLL.insert(6, "fifteen")
myLL.insert(108, 88)

print(myLL.printList())

myLL.remove(2)
#myLL.prepend("one")
myLL.remove(myLL.length)
print(myLL.printList())

print("Length:", myLL.length)
