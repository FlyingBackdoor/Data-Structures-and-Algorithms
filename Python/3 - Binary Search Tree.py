class Node(object):
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = Node(value)

        if self.root is None:
            self.root = newNode
            return self.root.value

        currentNode = self.root
        while True:
            if currentNode.value == value:
                return "Already Exist"

            if currentNode.value < value:
                #print("going right")
                if currentNode.right is None:
                    currentNode.right = newNode
                    return "Inserted"
                currentNode = currentNode.right
            else:
                if currentNode.left is None:
                    currentNode.left = newNode
                    return "Inserted"
                currentNode = currentNode.left



    def lookup(self, value):
        currentNode = self.root

        while True:
            if currentNode.value == value:
                return True

            if currentNode.value < value:
                if currentNode.right is None:
                    return False
                currentNode = currentNode.right

            if currentNode.value > value:
                if currentNode.left is None:
                    return False
                currentNode = currentNode.left

    def remove(self):
        pass


myBST = BinarySearchTree()
print(myBST.insert(5))
print(myBST.insert(7))
print(myBST.insert(3))

print(myBST.lookup(3))
