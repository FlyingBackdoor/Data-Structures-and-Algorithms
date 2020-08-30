class Node:
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
            return "Inserted! but try to plant a real tree :)"

        currentNode = self.root
        while True:
            if currentNode.value == value:
                return "Already Exist"

            if currentNode.value < value:
                if currentNode.right is None:
                    currentNode.right = newNode
                    return f"Inserted: {value}"
                currentNode = currentNode.right
            else:
                if currentNode.left is None:
                    currentNode.left = newNode
                    return f"Inserted: {value}"
                currentNode = currentNode.left

    def lookup(self, value):
        if self.root is None:
            return False

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

    def remove(self, value):
        if self.root is None:
            return "Grow some tree first ;p"

        currentNode = self.root

        while True:
            if currentNode.value == value:
                if currentNode.right is None and currentNode.left is None:
                    currentNode = None
                    return f"{value} Removed (Leaf Node)"
                elif currentNode.right is None or currentNode.left is None:
                    pass




tree = BinarySearchTree()
print(
f'''{tree.insert(9)}
{tree.insert(4)}
{tree.insert(6)}
{tree.insert(20)}
{tree.insert(170)}
{tree.insert(15)}
{tree.insert(1)}
{tree.insert(20)}
''')

print(f'''{tree.lookup(9)}
{tree.lookup(100)}''')
