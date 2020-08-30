class Graph:
    def __init__(self):
        self.numberOfNodes = 0
        self.adjecentList = {}

    def addVertex(self, node):
        self.adjecentList[node] = []
        self.numberOfNodes += 1

    def addEdge(self, node1, node2):
        #undirected graph
        try:
            #for node1
            currentConnection = self.adjecentList[node1]
            currentConnection.append(node2)
            #for node2
            currentConnection = self.adjecentList[node2]
            currentConnection.append(node1)
        except KeyError:
            print("Given node dosen't exist")




    def showConnections(self):
        allNodes = self.adjecentList.keys()
        for node in allNodes:
            nodeConnections = self.adjecentList[node]
            connections = ""
            for vertex in nodeConnections:
                connections += vertex + " "
            print(f"{node} --> {connections}")

myGraph = Graph()

myGraph.addVertex('0')
myGraph.addVertex('1')
myGraph.addVertex('2')
myGraph.addVertex('3')
myGraph.addVertex('4')
myGraph.addVertex('5')
myGraph.addVertex('6')
myGraph.addEdge('3', '1')
myGraph.addEdge('3', '4')
myGraph.addEdge('4', '2')
myGraph.addEdge('4', '5')
myGraph.addEdge('1', '2')
myGraph.addEdge('1', '0')
myGraph.addEdge('0', '2')
myGraph.addEdge('6', '5')

myGraph.showConnections()
#print(myGraph.adjecentList)
