class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
def findLowestValue(value):
    minValue = value.data
    
    #address of the particular node
    currentNode = value.next

    while currentNode:
        print("Current node data: ", currentNode.data)
        print("currentNode.next: ", currentNode.next)
        if currentNode.data < minValue:
            minValue = currentNode.data
        currentNode = currentNode.next
    print("Minimum value: ", minValue)

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4

print(findLowestValue(node1))